
cd ..

docker build -t products_parser .

docker tag products_parser andermatheus/products_parser:latest

docker push andermatheus/products_parser:latest