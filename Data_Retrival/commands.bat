#bild the image
1. docker build -t data-retrival ./Data_Retrival

#test the image
2.docker run --rm -it data-retrival

#creat right tag
3.docker tag isaac/data-retrival isaac100/data-retrival

#push to the docker-hub
4.docker push isaac100/data-retrival