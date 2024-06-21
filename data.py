import requests

url_base = "https://opentdb.com/api.php?"
amount = "10"


response = requests.get(url_base + "amount=" + amount)
data = response.json()
question_data = data["results"]
