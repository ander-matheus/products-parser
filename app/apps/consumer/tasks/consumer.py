import gzip
import json
import os
import tempfile

import requests
from celery import shared_task

from apps.consumer.models import ConsumerLog
from apps.products.api.serializers import ProductSerializer
from apps.products.models import Product


@shared_task(name="get_importer_list")
def get_importer_list():
    url = "https://challenges.coode.sh/food/data/json/index.txt"
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        file_list = response.text.splitlines()
        for filename in file_list:
            ConsumerLog.objects.create(
                url=f"https://challenges.coode.sh/food/data/json/{filename}"
            )


@shared_task(name="import_list")
def import_list(id: int):
    consumer = ConsumerLog.objects.get(id=id)
    try:
        response = requests.get(consumer.url, stream=True)

        with tempfile.NamedTemporaryFile(suffix=".gz", delete=False) as temp_file:
            temp_file.write(response.content)
            temp_file.flush()  # Ensure all data is written to the file
            temp_file_path = temp_file.name

            with gzip.open(temp_file.name, "rb") as f_in:
                decompressed_data = f_in.read()

                json_objects = []
                for line in decompressed_data.decode("utf-8").splitlines():
                    if line.strip():
                        json_objects.append(json.loads(line))

        os.remove(temp_file_path)
        Product.objects.bulk_create(
            [
                Product(
                    **ProductSerializer(
                        {**p, "code": p["code"].replace("\\", "").replace('"', "")}
                    ).data
                )
                for p in json_objects[:100]
            ]
        )
        consumer.status = ConsumerLog.COMPLETED
        consumer.save()
    except BaseException as e:
        consumer.exception_description = e
        consumer.status = ConsumerLog.ERROR
        consumer.save()
