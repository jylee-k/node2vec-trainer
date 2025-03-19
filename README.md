# node2vec-trainer

```example_request.py``` holds a sample POST request to be sent to the trainer docker.


Build and run trainer container
```bash
docker build -t node2vec-image .
docker run --name node2vec-container -p 8001:8001 -v $(pwd)/model:/app/model node2vec-image
```
Test the endpoint
```bash
python example_request.py
```

The model should be saved to the ./model directory that is mounted to the container.