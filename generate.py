import os
import subprocess
import shutil

# Fonction pour exécuter des commandes shell avec affichage en temps réel
def run_command(command, cwd=None):
    process = subprocess.Popen(command, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    while True:
        output = process.stdout.readline()
        if output:
            print(output.strip())
        return_code = process.poll()
        if return_code is not None:
            # Process terminé, lire les dernières lignes
            for output in process.stdout.readlines():
                if output:
                    print(output.strip())
            break
    if return_code != 0:
        print(f"Erreur lors de l'exécution de la commande: {command}")
        stderr = process.stderr.read()
        print(stderr)
    return return_code

# Définir le nom du projet
project_name = "LeMaitreDuCodeReact"

# Définir les tâches
tasks = {
    "Tache1_Componentisation": {
        "description.md": """# Tâche 1 : Componentisation et Props

## Instructions

Vous devez refactoriser l'application pour extraire certains éléments en composants réutilisables. L'objectif est d'améliorer la maintenabilité et la réutilisabilité du code.

### Objectifs

- Créer des composants fonctionnels avec TypeScript.
- Utiliser les **props** pour passer des données aux composants.
- Appliquer les meilleures pratiques de componentisation.

### Livrables

- Le code refactorisé.
- Un document `Rapport.md` expliquant les modifications apportées et les raisons de ces changements.

### Évaluation

- Respect des exigences fonctionnelles (30%)
- Qualité du code et respect des conventions (25%)
- Application des meilleures pratiques React (25%)
- Documentation et commentaires (20%)

Bonne chance !
""",
    },
    "Tache2_EtatEtHooks": {
        "description.md": """# Tâche 2 : Gestion de l'État et Hooks

## Instructions

Vous devez implémenter la gestion de l'état dans l'application en utilisant les Hooks de React. L'objectif est de permettre à l'utilisateur d'ajouter, de modifier et de supprimer des éléments dans une liste.

### Objectifs

- Utiliser le Hook `useState` pour gérer l'état local.
- Implémenter des fonctions pour ajouter, modifier et supprimer des éléments.
- Assurer une mise à jour correcte de l'interface utilisateur.

### Livrables

- Le code avec la gestion de l'état.
- Un document `Rapport.md` expliquant votre implémentation.

### Évaluation

- Fonctionnalité complète (40%)
- Utilisation correcte des Hooks (30%)
- Qualité du code (20%)
- Documentation (10%)

Bonne chance !
""",
    },
    "Tache3_EffetsDeBord": {
        "description.md": """# Tâche 3 : Effets de Bord et API

## Instructions

Vous devez intégrer une API externe pour récupérer des données lors du chargement de l'application. Utilisez le Hook `useEffect` pour gérer les effets de bord.

### Objectifs

- Utiliser `useEffect` pour effectuer des appels API.
- Gérer les états de chargement et les erreurs.
- Afficher les données récupérées dans l'interface.

### Livrables

- Le code avec l'intégration de l'API.
- Un document `Rapport.md` expliquant votre approche.

### Évaluation

- Intégration correcte de l'API (40%)
- Gestion des états de chargement et des erreurs (30%)
- Qualité du code (20%)
- Documentation (10%)

Bonne chance !
""",
    },
    "Tache4_Routage": {
        "description.md": """# Tâche 4 : Routage avec React Router

## Instructions

Ajoutez le routage à l'application pour naviguer entre différentes pages (par exemple, Accueil, Liste, Détails).

### Objectifs

- Installer et configurer React Router.
- Créer des composants pour les différentes pages.
- Implémenter la navigation entre les pages.

### Livrables

- Le code avec le routage implémenté.
- Un document `Rapport.md` décrivant votre implémentation.

### Évaluation

- Fonctionnalité du routage (40%)
- Structure et organisation du code (30%)
- Qualité du code (20%)
- Documentation (10%)

Bonne chance !
""",
    },
    "Tache5_Testing": {
        "description.md": """# Tâche 5 : Tests Unitaires avec Jest et React Testing Library

## Instructions

Écrire des tests unitaires pour les composants de l'application en utilisant Jest et React Testing Library.

### Objectifs

- Configurer Jest et React Testing Library.
- Écrire des tests pour les composants principaux.
- Atteindre une couverture de code significative.

### Livrables

- Le code avec les tests unitaires.
- Un rapport de couverture de code.
- Un document `Rapport.md` expliquant votre approche de test.

### Évaluation

- Qualité et pertinence des tests (50%)
- Couverture de code atteinte (30%)
- Configuration correcte des outils de test (10%)
- Documentation (10%)

Bonne chance !
""",
    }
}

# Création du projet React avec TypeScript en utilisant Vite
print("Création du projet React avec TypeScript en utilisant Vite...")
run_command(f"npm create vite@latest {project_name} -- --template react-ts")

# Installation des dépendances supplémentaires (React Router, etc.)
print("Installation des dépendances supplémentaires...")
additional_packages = [
    "react-router-dom@6",
    "@types/react-router-dom",
    "jest",
    "@testing-library/react",
    "@testing-library/jest-dom",
    "@testing-library/user-event"
]
run_command(f"npm install {' '.join(additional_packages)}", cwd=project_name)

# Installer Jest et configurer le testing avec Vite
print("Configuration de Jest pour les tests...")
run_command("npm install --save-dev jest ts-jest babel-jest @types/jest", cwd=project_name)
run_command("npx ts-jest config:init", cwd=project_name)

# Création des dossiers pour les tâches
for task_name, contents in tasks.items():
    # Créer un dossier pour chaque tâche
    task_dir = os.path.join(project_name, task_name)
    os.makedirs(task_dir, exist_ok=True)

    # Créer le fichier description.md
    description_path = os.path.join(task_dir, "description.md")
    with open(description_path, "w", encoding="utf-8") as desc_file:
        desc_file.write(contents.get("description.md", ""))

    # Créer un dossier pour les livrables du participant
    your_solution_dir = os.path.join(task_dir, "YourSolution")
    os.makedirs(your_solution_dir, exist_ok=True)

    # Ajouter un .gitignore dans le dossier de la tâche
    gitignore_path = os.path.join(task_dir, ".gitignore")
    with open(gitignore_path, "w", encoding="utf-8") as gitignore_file:
        gitignore_file.write("node_modules/\ndist/\n")

# Mise à jour du README principal
readme_path = os.path.join(project_name, "README.md")
with open(readme_path, "a", encoding="utf-8") as readme_file:
    readme_file.write("\n## Tâches du Défi\n")
    for task_name in tasks:
        readme_file.write(f"- [{task_name}](./{task_name}/description.md)\n")

print(f"Le projet '{project_name}' a été créé avec succès.")
