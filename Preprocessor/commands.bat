
#bild the image
1. docker build -t preprocessor-service ./Preprocessor

#test the image
2.docker run --rm -it preprocessor-service

#creat right tag
3.docker tag isaac/preprocessor-service isaac100/preprocessor-service

#push to the docker-hub
4.docker push isaac100/preprocessor-service