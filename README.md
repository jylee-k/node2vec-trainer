# node2vec-trainer

```example_request.py``` holds a sample POST request to be sent to the trainer docker.

Set up node2vec trainer container with:

```bash
docker build 
docker run --name node2vec-container -p 8001:8001 node2vec-image

```