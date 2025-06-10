import json
from random import uniform
from datetime import datetime
import time

registros = []

for id in range(1, 1001):
    dados_pf = uniform(0.7, 1.0)
    dados_hp = uniform(70, 80)
    dados_tp = uniform(20, 25)

    registro = {
        'idtemp': id,
        'powerfactor': round(dados_pf, 3),
        'hydraulicpressure': round(dados_hp, 2),
        'temperature': round(dados_tp, 2),
        'timestamp': datetime.now().isoformat()
    }

    registros.append(registro)

    print(f'Registro {id} gerado.')
    time.sleep(0.1)

#Caminho de saída, altere para o caminho de sua preferência
caminho_arquivo = 'C:/Users/usuario/Desktop/airflow/data/data.json'

with open(caminho_arquivo, 'w') as fp:
    json.dump(registros, fp, indent=2)

print(f'\n{len(registros)} registros salvos em {caminho_arquivo}')
