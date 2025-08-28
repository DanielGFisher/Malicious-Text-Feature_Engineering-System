
#bild the image
1. docker build -t isaac/retriever:latest .

#test the image
2.docker run --rm -e CONNECTION_STRING="mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/" itzch/retriever:latest

#creat right tag
3.docker tag isaac/retriever:latest isaac100/retriever:latest

#push to the docker-hub
4.docker push isaac100/retriever:latest