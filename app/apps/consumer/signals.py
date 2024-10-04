from apps.consumer.tasks import import_list


def post_save_consumerlog(sender, instance, created, **kwargs):
    if created:
        import_list.delay(instance.id)
