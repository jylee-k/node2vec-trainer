from receive_graph import receive_graph
import node2vec

# receive the graph via POST request


G = receive_graph()
print (G)

# train the node2vec model
