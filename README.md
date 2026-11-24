# E-portfolio d'Arthur Sauvezie

Site statique (HTML, CSS, un peu de JavaScript), prêt pour GitHub Pages.

## Mettre en ligne

1. Dans votre dépôt `arthursvz.github.io`, supprimez l'ancien contenu (gardez le dossier `.git`).
2. Copiez-y tous les fichiers de ce dossier.
3. Ajoutez vos fichiers dans `assets/` : `photo.jpg` (portrait, idéalement 760 × 920 px), `cv.pdf` (français) et `cv-en.pdf` (anglais).
4. Publiez :
   ```
   git add .
   git commit -m "Nouvelle version de l'e-portfolio"
   git push
   ```
5. Le site est en ligne quelques minutes plus tard sur https://arthursvz.github.io

## À compléter

Les textes en italique entre crochets sont des emplacements à remplacer :

- Les deux langues : chaque texte à compléter existe en français (racine) et en anglais (dossier `en/`).
- `index.html` : type et période de stage recherché.
- `projets.html` : description, technologies et résultat de chacun des quatre projets.
- `contact.html` : adresse e-mail et lien LinkedIn (le lien GitHub est à vérifier).
- `assets/photo.jpg` et `assets/cv.pdf`.
- Retirez la classe `todo` d'un élément une fois son texte écrit, pour qu'il reprenne le style normal.

## Structure

```
index.html  cv.html  projets.html  parcours.html  contact.html   (français)
en/index.html  cv.html  projects.html  background.html  contact.html   (anglais)
css/style.css     styles et thèmes clair/sombre
js/theme.js       bouton clair/sombre (choix mémorisé)
assets/           photo.jpg, cv.pdf, cv-en.pdf

Le sélecteur FR / EN du menu renvoie vers la page équivalente dans l'autre langue.
```
