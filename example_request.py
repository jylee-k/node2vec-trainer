import networkx as nx
import pickle
import requests
import base64

# Random graph G
G = nx.complete_graph(100) # Replace with actual graph object built from data

# The target URL 
TARGET_URL = "http://0.0.0.0:8001/receive_graph"

# Send the graph to the target URL
def send_graph(G):
    # Serialize the graph
    graph_data = base64.b64encode(pickle.dumps(G)).decode()

    # Send the graph to the target URL
    response = requests.post(TARGET_URL, json={"graph": graph_data})
    print(response.json())
    
if __name__ == "__main__": 
    send_graph(G)