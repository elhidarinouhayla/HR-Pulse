FROM ghcr.io/astral-sh/uv:python3.12-bookworm

WORKDIR /app

# copier les fichiers de dependances
COPY pyproject.toml uv.lock ./

# installer les dependances
RUN uv sync --frozen --no-dev

# copier le reste du projet
COPY . .

# exposer le port FastAPI
EXPOSE 8000

# lancer l'application
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]