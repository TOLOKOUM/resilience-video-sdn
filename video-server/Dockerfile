FROM nginx:latest

# Installe ffmpeg pour la conversion des vidéos
RUN apt update && apt install -y ffmpeg

# Copie la configuration Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Crée un dossier pour les vidéos
RUN mkdir -p /var/www/html/videos
COPY videos/ /var/www/html/videos/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

