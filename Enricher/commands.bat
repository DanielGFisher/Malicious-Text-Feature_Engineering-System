
#bild the image
1. docker build -t enricher-service ./Enricher

#test the image
2.docker run --rm -it enricher-service

#creat right tag
3.docker tag isaac/enricher-service isaac100/enricher-service

#push to the docker-hub
4.docker push isaac100/enricher-service