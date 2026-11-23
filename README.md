# IZAM TOURS ONE

Landing page locale en HTML5, CSS3 et JavaScript natif. Ouvrir `index.html` ou lancer `python -m http.server 8080` dans ce dossier, puis visiter http://localhost:8080.

## Fonctionnement

- Français, anglais et espagnol, choix mémorisé localement.
- Réservation dans une boîte de dialogue accessible ; détails transmis uniquement à l’ouverture volontaire de WhatsApp.
- Toutes les réservations utilisent **212660114045**. Messages distincts par service et langue dans `js/app.js`.
- Navigation mobile, liens téléphoniques, cartes cliquables, prise en compte des mouvements réduits.
- Aucune dépendance, aucun suivi, aucune API externe.

## Images et avis

Cette version remplace les extractions photographiques par dix images g?n?r?es pour le projet : le h?ros avec taxi jaune et Koutoubia, Ourika, Essaouira, Ouzoud, Agafay, quad, chameau, d?ner, Merzouga et la carte d?corative. Les images sont des illustrations touristiques g?n?r?es, pas des photos documentaires des prestations. Le taxi du h?ros est une reconstitution visuelle d?apr?s la r?f?rence, pas une nouvelle photographie du v?hicule r?el. Le logo et les avatars des avis restent extraits de la r?f?rence fournie pour conserver les ?l?ments originaux ; aucun faux client ni t?moignage n?a ?t? g?n?r?. Les originaux g?n?r?s sont conserv?s par ImageGen ; les WebP optimis?s sont dans `assets/images/`.

Les textes, boutons, titres, cartes, ic?nes SVG, trac?s de voyage, formulaires et menus sont de vrais ?l?ments HTML/CSS/JS. Les photos ne contiennent pas les textes de l?interface. Les versions FR/EN/ES et les r?servations WhatsApp restent fonctionnelles.

Les avis sont retranscrits de la r?f?rence et conservent leur langue d?origine ; les libell?s de l?interface sont traduits. La note est statique ; aucune URL Google Maps v?rifi?e n?a ?t? fournie.

## Publication

Copier `index.html`, `css`, `js` et `assets` sur un hébergeur statique HTTPS. Mettre à jour les métadonnées Open Graph avec l’URL absolue du domaine une fois connu. Le projet n’a pas été publié.

## Vérifications effectuées

Syntaxe JavaScript validée avec `node --check`. Ressources HTML locales et réponses HTTP vérifiées. Contrôle des trois dictionnaires de traduction et des 36 messages WhatsApp, du numéro, de l’encodage des détails et de l’ouverture avec `noopener,noreferrer`. L’accès au navigateur étant indisponible dans cette session, les captures comparatives, les essais aux sept largeurs demandées et les interactions réelles du formulaire restent à vérifier dans un navigateur.

## Correction PC et mobile

`css/reference.css` conserve les proportions mobiles et applique une mise en page d?di?e d?s 769 px. Le h?ros et Merzouga utilisent des photographies g?n?r?es continues pour ?viter les d?coupes visibles dans les captures pr?c?dentes. Les photos des destinations et activit?s restent extraites de la r?f?rence. Les boutons et les d?tails du circuit ont ?t? redimensionn?s pour ?viter les d?bordements. La syntaxe JavaScript, les ressources locales et les accolades CSS ont ?t? v?rifi?es. La nouvelle comparaison visuelle dans Chrome n?a pas pu ?tre men?e : la fen?tre renvoie une erreur de fen?tre minimis?e dans l?outil de contr?le.

## Ic?nes

Les ic?nes utilisent des SVG locaux Font Awesome Free, Material Design Icons et Game-icons.net. Drapeaux SVG Flag Icons. Sources et licences : `assets/icons/ATTRIBUTION.md`. Le symbole Excursions combine une vraie ?pingle et un trac? pointill?. Aper?u : `icons-preview.html`. Les ic?nes restent vectorielles ? toutes les tailles.

T?l?phone pour les appels : **0666 408 104** (`+212666408104`). WhatsApp : **+212660114045**, inchang?.
