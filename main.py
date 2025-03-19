import node2vec
from fastapi import FastAPI
from pydantic import BaseModel
# import networkx as nx
import pickle
import base64
import os

app = FastAPI()

MODEL_DIR = "/app/model"
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

class GraphData(BaseModel):
    graph: str  # Base64 encoded graph

@app.post("/receive_graph")
def receive_graph(data: GraphData):
    # Deserialize the graph
    G = pickle.loads(base64.b64decode(data.graph))

    # Print for debugging 
    print("Received Graph:", G.nodes, G.edges)

    # train the node2vec model
    n2v = node2vec.Node2Vec(G, dimensions=64, walk_length=30, num_walks=10)
    model = n2v.fit(window=10, min_count=1, batch_words=4)

    # save the model
    model_path = os.path.join(MODEL_DIR, "node2vec_model.kv")
    model.wv.save_word2vec_format(model_path)

    return {"message": "node2vec model trained", "num_nodes": G.number_of_nodes()}



