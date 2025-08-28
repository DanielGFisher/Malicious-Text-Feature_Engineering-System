
#bild the image
1. docker build -t isaac/retriever:latest .

#test the image
2.docker run --rm -e CONNECTION_STRING="mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/" itzch/retriever:latest

