#!/bin/bash
# Aller dans le dossier du projet
cd "$(dirname "$0")"

echo "--- Récupération des dernières modifications ---"
git pull origin main

echo "--- Reconstruction et redémarrage du conteneur ---"
# --build force la reconstruction même si l'image existe déjà
docker compose up -d --build

echo "--- Nettoyage des anciennes images (Lightweightness) ---"
docker image prune -f
