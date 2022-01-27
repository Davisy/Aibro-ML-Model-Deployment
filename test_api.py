import requests
import json

review = {"data": "A truly beautiful film that will having you crying with joy and pride. The (few) poor reviews cite a lack of authenticity regarding Richards character and a lack of screen time for the other major family members, including Serena. While I admittedly don’t know exactly the kind of person and father Richard was"}

prediction = requests.post(
    "http://api.aipaca.ai/v1/DavisDavid/public/my_movie_sentiment_classifier/predict",
    data=review,
)

result = prediction.text

print(result)


