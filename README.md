# Prinz Eugen Bot
*Never forgetti RIP in spaghetti...*
## Installation
### VS Code
1. [Version Windows 10 Stable](https://code.visualstudio.com/)
2. Cliquer sur l'icône des extensions à gauche dans VS Code et chercher l'extension Python
3. Virer Jupyter parce que c'est de la merde
### Git
1. Installer git et isok
### Python aka GROS PLAISIR
1. Installer python (options en screenshot) -> https://www.python.org/downloads/

![Screenshot_1](https://user-images.githubusercontent.com/71824529/188321960-08047db0-457e-45a9-a113-89454e5ad8b1.png)
![Screenshot_2](https://user-images.githubusercontent.com/71824529/188321966-77192bdc-99dc-4219-92c8-e11098540247.png)

2. Installer poetry dans PowerShell `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`
3. Chercher path dans Windows -> en bas, variables d'environnement -> modifier 'Path' -> nouveau `%APPDATA%\Python\Scripts`
4. Lancer `poetry --version` dans PowerShell pour checker que c'est pas de la merde
5. Lancer `poetry config virtualenvs.in-project true`
6. Dans VS Code, dans le terminal, lancer `poetry install` pour installer les packages

### Flake8 et Black
1. [Flake8](https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-2#flake8)
2. [Black](https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-2#black)
