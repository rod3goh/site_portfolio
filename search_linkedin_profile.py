import sys
sys.path.append("/opt/.manus/.sandbox-runtime")
from data_api import ApiClient
import json

client = ApiClient()

# Tentar buscar o perfil usando a API de busca
search_results = client.call_api("LinkedIn/search_people", query={"keywords": "Rodrigo Pontes rodrigoeasytec"})

# Salvar os resultados da busca em um arquivo JSON
with open("/home/ubuntu/linkedin_search_rodrigoeasytec.json", "w") as f:
    json.dump(search_results, f, indent=2)

print("Resultados da busca no LinkedIn salvos em /home/ubuntu/linkedin_search_rodrigoeasytec.json")

