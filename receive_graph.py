from fastapi import FastAPI
from pydantic import BaseModel
import networkx as nx
import pickle
import base64

app = FastAPI()

class GraphData(BaseModel):
    graph: str  # Base64 encoded graph

@app.post("/receive_graph")
def receive_graph(data: GraphData):
    # Deserialize the graph
    G = pickle.loads(base64.b64decode(data.graph))

    # Print for debugging (optional)
    print("Received Graph:", G.nodes, G.edges)

    return {"message": "Graph received successfully", "num_nodes": G.number_of_nodes()}
