import requests
import time

# URL de Prometheus pour récupérer les métriques réseau
prometheus_url = "http://localhost:9090/api/v1/query"
query = 'rate(node_network_receive_bytes_total[1m])'

# Fonction pour obtenir la bande passante de Prometheus
def get_bandwidth():
    response = requests.get(prometheus_url, params={'query': query})
    if response.status_code == 200:
        result = response.json()
        return float(result['data']['result'][0]['value'][1])  # Donne la bande passante en bytes/sec
    return 0

# URL OpenDaylight pour envoyer la requête REST
odl_url = "http://localhost:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow/flow1"
odl_auth = ('admin', 'admin')

# Fonction pour adapter le routage avec OpenDaylight
def adjust_routing():
    flow_data = {
        "flow": {
            "id": "flow1",
            "match": {
                "in_port": "1"
            },
            "actions": [
                {
                    "order": 0,
                    "output-action": {
                        "output-node-connector": "2"
                    }
                }
            ]
        }
    }
    response = requests.post(odl_url, json=flow_data, auth=odl_auth, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        print("Flux modifié avec succès!")
    else:
        print(f"Erreur lors de la modification des flux: {response.status_code}")

# Surveillance continue de la bande passante
threshold = 1e6  # 1 Mbps (en bytes par seconde)
while True:
    bandwidth = get_bandwidth()
    print(f"Bande passante actuelle: {bandwidth} bytes/sec")
    if bandwidth < threshold:
        print("Bande passante trop faible, modification du routage...")
        adjust_routing()
    time.sleep(60)  # Attente de 60 secondes avant de vérifier à nouveau
