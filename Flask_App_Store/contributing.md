# CONTRIBUTING

## How to run the Dockerfile

```
docker build -t flask-smorest-api .

docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api

flask-run

flask run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run --host 0.0.0.0" 


```

