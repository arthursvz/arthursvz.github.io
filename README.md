# E-portfolio d'Arthur Sauvezie

Site statique (HTML, CSS, un peu de JavaScript) publié sur GitHub Pages : https://arthursvz.github.io

## Modifier le contenu

Les pages HTML sont **générées** par `_src/build.py`. Tout le contenu (expériences, engagements,
formation, certifications, compétences, liens, logos) est dans ce fichier, en français et en anglais.

```
python _src/build.py
```

Ne modifiez pas les `.html` à la main : ils seraient écrasés à la prochaine génération.
Le dossier `_src/` n'est pas publié par GitHub Pages.

## Publier

```
git add .
git commit -m "Mise à jour du portfolio"
git push
```

## Structure

```
index.html  experiences.html  engagements.html  parcours.html  cv.html  contact.html   (français)
en/index.html  experience.html  commitments.html  background.html  cv.html  contact.html   (anglais)
projets.html, en/projects.html   redirections depuis les anciennes adresses
css/style.css        styles, thèmes clair/sombre, mise en page mobile
js/theme.js          bouton clair/sombre, menu mobile, affichage protégé de l'e-mail
assets/logos/        logos des structures citées
assets/              photo.jpg, cv.pdf, cv-en.pdf
_src/build.py        générateur des pages
```

L'adresse e-mail n'apparaît jamais en clair dans le HTML : elle est stockée à l'envers et
reconstituée au clic sur « Afficher l'adresse ».
