#bild the image
1. docker build -t data-persister ./Persister

#test the image
2.docker run --rm -it data-persister

#creat right tag
3.docker tag isaac/data-persister isaac100/data-persister

#push to the docker-hub
4.docker push isaac100/persister