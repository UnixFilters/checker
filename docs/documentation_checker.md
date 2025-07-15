# Documentation du checker

Ce projet permet d'évaluer le code envoyé depuis l'[interface](https://github.com/UnixFilters/unixfilters-franceIOI/tree/main), en comparant la sortie produite par le code avec une sortie attendue.

## Architecture

```bash
.
├── blocklyUnixFilters_lib.js
├── docs
│ ├── documentation_checker.md
│ └── documentation_checker.py
├── exemple_checker
│ ├── blocklyUnixFilters_lib.js
│ ├── index.css
│ ├── index.html
│ ├── jsongenerator.js
│ ├── taskSettings.json
│ ├── tests
│ │ ├── files
│ │ │ ├── test01.in # fichier pris en entrée par le checker
│ │ │ ├── test01.out # json obtenu après exécution du code
│ │ │ └── test01.solout # résultat attendu
│ │ └── gen
│ │ ├── checker.py # logique permettant d'évaluer le score et renvoyer le feedback
│ │ ├── commands.py # librairie exécutant les commandes
│ │ ├── livres.txt # exemple de fichier d'entrée
│ │ └── solution.py # contient le code généré par les blocs
│ └── unixfilters.js
├── index.css
├── index.html
├── jsongenerator.js
├── task.js
└── unixfilters.js
```
