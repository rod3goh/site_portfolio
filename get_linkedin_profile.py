import sys
sys.path.append('/opt/.manus/.sandbox-runtime')
from data_api import ApiClient
import json

client = ApiClient()

# Chamar a API do LinkedIn para obter dados do perfil
profile_data = client.call_api('LinkedIn/get_user_profile_by_username', query={'username': 'rodrigoeasytec'})

# Salvar os dados em um arquivo JSON
with open('/home/ubuntu/linkedin_profile_rodrigoeasytec.json', 'w') as f:
    json.dump(profile_data, f, indent=2)

print("Dados do perfil do LinkedIn salvos em /home/ubuntu/linkedin_profile_rodrigoeasytec.json")

