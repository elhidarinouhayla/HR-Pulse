import time
import pandas as pd
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from app.config import ENDPOINT, KEY


# creer le client Azure
def create_client():
    credential = AzureKeyCredential(KEY)
    client = TextAnalyticsClient(endpoint=ENDPOINT, credential=credential)
    return client



def extract_skills(data_path, output_path, limit=100):

    # connexion a azure
    client = create_client()

    # lire le fichier CSV
    df = pd.read_csv(data_path)

    # prendre seulement les premieres lignes 
    df = df.head(limit)

    extracted_skills_list = []

    # parcourir chaque ligne
    for index, row in df.iterrows():

        # recuperer la description du job
        description = str(row["Job Description"])[:1000]

        # envoyer a Azure NER
        response = client.recognize_entities([description])
        document = response[0]

        skills = []

        # verifier qu’il n’y a pas d’erreur
        if not document.is_error:

            for entity in document.entities:

                # Garder seulement Skill et Product
                if entity.category == "Skill":
                    skills.append(entity.text)

        # supprimer les doublons
        skills = list(set(skills))

        # convertir en texte separe par virgule
        skills_text = ", ".join(skills)

        extracted_skills_list.append(skills_text)

        # pause pour eviter le blocage
        time.sleep(1)

    # ajouter la nouvelle colonne
    df["extracted_skills"] = extracted_skills_list

    # sauvegarder le nouveau fichier
    df.to_csv(output_path, index=False)


#  lancer le script
if __name__ == "__main__":
    extract_skills(
        "data/raw/jobs_data_cleaned.csv",
        "data/processed/skills_data.csv",
        limit=100
    )