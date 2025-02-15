# Utiliser une image de base
FROM ubuntu:20.04

# Installer VLC, PulseAudio, ping et d'autres utilitaires
RUN apt-get update && \
    apt-get install -y vlc pulseaudio alsa-utils iputils-ping && \
    apt-get clean

# Définir l'utilisateur
RUN useradd -ms /bin/bash vlcuser
USER vlcuser

# Commande par défaut
CMD ["bash"]
