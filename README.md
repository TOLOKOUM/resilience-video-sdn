# Résilience d'un Système Vidéo Conteneurisé en Environnement SDN

## Description du projet

Ce projet a pour objectif de démontrer la **résilience d'un système vidéo conteneurisé** face aux fluctuations de bande passante dans un environnement **SDN (Software-Defined Networking)**. En utilisant des outils modernes tels que **Docker**, **OpenDaylight**, et des outils de **monitoring** comme **Prometheus** et **Grafana**, nous avons conçu une solution permettant d'adapter le streaming vidéo à la variation dynamique de la bande passante.

Le système met en œuvre une architecture de réseau virtuelle (SDN) permettant de réagir en temps réel aux conditions changeantes de la bande passante, tout en maintenant une qualité vidéo optimale. L'application de cette solution est particulièrement pertinente pour les réseaux à haute demande de bande passante, tels que ceux utilisés pour le **streaming vidéo en haute définition**.

Le projet est un projet académique de fin de semestre dans le cadre de l'unité d'enseignement "Cloud Computing".
Il a été réalisé par les étudiants : TOLOKOUM David Rive, BIKOURI BI BEP Henri, DJOUKOUO KALLA Vanessa, DONGMO Prince Williams, MBOLANG TIDANG Henri, avec C comme chef de groupe.

## Table des matières

- [Technologies utilisées](#technologies-utilisées)
- [Architecture du projet](#architecture-du-projet)
- [Prérequis](#prérequis)
- [Installation et Déploiement](#installation-et-déploiement)
- [Structure des dossiers](#structure-des-dossiers)
- [Configuration de la topologie réseau](#configuration-de-la-topologie-réseau)
- [Monitoring et Résilience](#monitoring-et-résilience)
- [Exécution du projet](#exécution-du-projet)
- [Contribution](#contribution)
- [Licences](#licences)

## Technologies utilisées

- **Docker** : Conteneurisation des applications (serveur vidéo, client VLC, etc.)
- **SDN** (Software-Defined Networking) : Gestion centralisée du réseau via OpenDaylight.
- **Prometheus** : Surveillance des métriques réseau.
- **Grafana** : Visualisation des métriques et des données collectées.
- **OpenDaylight** : Contrôleur SDN permettant la gestion dynamique des flux de trafic.
- **eBPF** : Pour collecter les tailles de paquets et filtrer les paquets HTTPS et les paquets de grande taille (supérieurs à 400 MB).
- **Mininet** : Simulation d'un réseau SDN.
- **nginx** : Serveur web pour héberger les vidéos.

## Architecture du projet

L'architecture du projet repose sur une structure conteneurisée, où chaque composant du système est isolé dans son propre conteneur Docker. La communication entre les conteneurs est gérée via **Docker Compose**. Les principaux composants sont les suivants :

- **Serveur vidéo** : Conteneur contenant le serveur vidéo DASH, avec un serveur web Nginx pour la diffusion des vidéos.
- **Client VLC** : Conteneur contenant un client VLC pour la lecture des vidéos en streaming.
- **Contrôleur OpenDaylight** : Gestion du routage dynamique du trafic via un contrôleur SDN.
- **Monitoring Prometheus et Grafana** : Collecte et visualisation des métriques réseau, et surveillance de la bande passante.
- **Adaptation dynamique du routage** : Grâce à OpenDaylight, le routage est modifié en fonction des variations de bande passante détectées.

## Prérequis

Avant de commencer, assurez-vous que votre machine répond aux prérequis suivants :

- **Ubuntu** (ou une autre distribution Linux compatible)
- **Docker** et **Docker Compose** installés
- **Python 3.x** (pour le script d'adaptation dynamique du routage)
- **OpenDaylight** installé et configuré
- **Prometheus** et **Grafana** installés pour le monitoring

## Installation et Déploiement

1. Clonez le dépôt du projet :

    ```bash
    git clone https://github.com/TOLOKOUM/resilience-video-sdn.git
    cd resilience-video-sdn
    ```

2. Construisez les conteneurs Docker à l'aide de Docker Compose :

    ```bash
    docker-compose build
    ```

3. Lancez les conteneurs :

    ```bash
    docker-compose up
    ```

4. Accédez au serveur vidéo via l'adresse `http://localhost:8080` dans votre navigateur. Le client VLC est automatiquement configuré pour se connecter au serveur vidéo et commencer le streaming.

5. Pour surveiller les métriques, ouvrez **Grafana** sur `http://localhost:3000` et connectez-vous avec les identifiants par défaut. Vous pouvez visualiser l'état du réseau et les variations de bande passante en temps réel.

## Structure des dossiers

Voici la structure des dossiers du projet :

resilience-video-sdn/
├── adaptive_routing.py       # Script pour l'adaptation dynamique du routage
├── docker-compose.yml        # Fichier de configuration Docker Compose
├── prometheus.yml            # Configuration de Prometheus
├── video-server/             # Conteneur pour le serveur vidéo
│   ├── Dockerfile            # Dockerfile du serveur vidéo
│   ├── nginx.conf            # Configuration du serveur Nginx
│   └── videos/               # Vidéos stockées pour le streaming
├── vlc-client/               # Conteneur pour le client VLC
│   └── Dockerfile            # Dockerfile du client VLC
### Émulation de la perte de bande passante

Pour émuler les variations de bande passante, nous utilisons `tc` (Traffic Control), un outil de gestion du trafic réseau sous Linux. Cela permet de simuler des situations où la bande passante du réseau fluctue, forçant le système à réagir et à ajuster les flux dynamiquement.

## Monitoring et Résilience

### Prometheus et Grafana

Les métriques de performance et la bande passante sont surveillées à l'aide de **Prometheus**, qui collecte les données des différents composants du système. **Grafana** est utilisé pour afficher ces données sous forme de graphiques interactifs, permettant de suivre l'état du système en temps réel.

### Adaptation dynamique du routage

L'adaptation du routage est réalisée via le contrôleur **OpenDaylight**, qui ajuste les flux réseau en fonction des conditions de bande passante collectées par Prometheus. Cela permet de maintenir une qualité vidéo stable, même en cas de fluctuations importantes de la bande passante.

## Exécution du projet

Une fois le projet déployé, les étapes suivantes décrivent l'exécution typique du projet :

1. Lancer les conteneurs avec `docker-compose up`.
2. Accéder au serveur vidéo via un navigateur.
3. Le client VLC commence à lire les vidéos en streaming.
4. Surveiller l'état du réseau et la bande passante via Grafana.
5. Tester la résilience en simulant des pertes de bande passante avec `tc`.

## Contribution

Les contributions au projet sont les bienvenues. Si vous souhaitez contribuer, suivez les étapes suivantes :

1. Fork ce dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/nom-de-la-fonctionnalité`).
3. Faites vos modifications et commitez-les (`git commit -m "Ajout de la fonctionnalité X"`).
4. Poussez la branche sur votre fork (`git push origin feature/nom-de-la-fonctionnalité`).
5. Créez une pull request pour que vos modifications soient intégrées.

## Licences

Ce projet est sous la licence **MIT**. Vous pouvez l'utiliser, le modifier et le distribuer librement, sous réserve de respecter les termes de cette licence.

---

## Contacts

Pour toute question ou problème, n'hésitez pas à ouvrir un **issue** sur GitHub, ou à me contacter directement à **davidtolokoum8@gmail.com**.
