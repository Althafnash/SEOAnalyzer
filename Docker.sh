sudo docker build -t seo .
sudo docker run -it --rm -p 8501:8501 seo
sudo firefox http://localhost:8501