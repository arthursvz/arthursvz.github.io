FROM nginx:alpine

# 1. Nettoyage du dossier par défaut de Nginx pour éviter les conflits
RUN rm -rf /usr/share/nginx/html/*

# 2. Copie du contenu de ton projet
# Conseil : utilise un fichier .dockerignore pour ne pas copier les fichiers de config Docker
COPY . /usr/share/nginx/html

# 3. Sécurité : Ajuster les permissions pour que Nginx puisse lire les fichiers
RUN chmod -R 755 /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
