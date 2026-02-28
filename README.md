#  HR-Pulse — Intelligence Artificielle & Recrutement

> **HR-Pulse** est une plateforme SaaS innovante de Data Engineering et d'Intelligence Artificielle conçue pour moderniser et automatiser le processus de recrutement. En s'appuyant sur des modèles de Machine Learning et de Traitement du Langage Naturel (NLP), elle optimise la mise en relation entre candidats et opportunités professionnelles.

---

##  Points Forts

*   **Extraction NER (Azure AI)** : Identification automatique des compétences techniques depuis les descriptions de poste.
*   **Prédiction Salariale ML** : Modèles de régression prédisant les fourchettes de rémunération basées sur le marché.
*   **Architecture Cloud Native** : Prêt pour Azure avec infrastructure gérée par Terraform.
*   **Observabilité Full-Stack** : Monitoring en temps réel via OpenTelemetry et Jaeger.
*   **Performance & Sécurité** : Authentification robuste (JWT) et gestionnaire de paquets ultra-rapide (`uv`).

--



---

##  Structure du Projet

```bash
HR-PULSE/
├── app/
│   ├── ml/             
│   ├── models/        
│   ├── schemas/        
│   ├── services/      
│   ├── auth.py         
│   ├── database.py    
│   └── main.py         
├── infra/              
├── data/              
├── test/               
├── docker-compose.yml  
├── Dockerfile         
├── pyproject.toml      
└── .env                
```

---

##  Démarrage Rapide

### 1. Prérequis
- Python 3.12+
- Manager [uv](https://github.com/astral-sh/uv) installé
- Docker & Docker Compose
- Accès à une instance Azure SQL & Azure AI Language

### 2. Installation & Configuration
```bash
# Cloner le dépôt
git clone https://github.com/votre-compte/HR-Pulse.git
cd HR-Pulse

# Installer les dépendances avec uv
uv sync

# Configurer l'environnement
cp .env.example .env
# Éditez le fichier .env avec vos credentials
```

### 3. Lancer l'API
```bash
# Mode développement
uv run uvicorn app.main:app --reload --port 8000
```

### 4. Docker (Optionnel)
```bash
docker-compose up --build
```

---

##  Documentation de l'API (Endpoints)

| Méthode | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/register` | Inscription d'un nouvel utilisateur |
| `POST` | `/login` | Authentification & génération de token JWT |
| `POST` | `/predict` | Prédiction du salaire estimé |
| `GET` | `/skills` | Liste toutes les compétences extraites |
| `GET` | `/jobs` | Liste toutes les offres d'emploi |
| `GET` | `/jobs_by_skill/{skill}` | Recherche d'offres par compétence spécifique |

> La documentation interactive (Swagger) est disponible sur : `http://localhost:8000/docs`

---

## Variables d'Environnement

Le fichier `.env` doit contenir les informations suivantes :

```ini
# Database
DATABASE_URL=mssql+pyodbc://user:pass@server.database.windows.net/db?driver=ODBC+Driver+18+for+SQL+Server

# Azure AI
AZURE_AI_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
AZURE_AI_KEY=votre_cle_azure_ai

# Security
SECRET_KEY=votre_cle_secrete_pour_jwt
ALGORITHM=HS256
```

---

## Observabilité

Le projet intègre **OpenTelemetry** pour le tracking distribué. Les traces sont exportées vers un collecteur OTLP (ex: Jaeger).
Vous pouvez visualiser les performances des requêtes SQL et des appels aux services Azure AI en temps réel.

