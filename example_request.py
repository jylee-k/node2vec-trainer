import networkx as nx
import pickle
import requests
import base64

# Random graph G
G = nx.complete_graph(5) # Replace with actual graph object built from data

# The target URL 
TARGET_URL = "http://node2vec-trainer:8001/receive_graph"

# Send the graph to the target URL
def send_graph():
    # Serialize the graph
    graph_data = base64.b64encode(pickle.dumps(G)).decode()

    # Send the graph to the target URL
    response = requests.post(TARGET_URL, json={"graph": graph_data})
    
    return {"message": "Graph sent", "client_response": response.json()}
