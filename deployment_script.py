import requests

review = {"data": "this movie was the best movie ever "}

result = requests.post(
    "http://api.aipaca.ai/v1/DavisDavid/public/sentiment_classifier/predict",
    params=review,
)

print(result)
