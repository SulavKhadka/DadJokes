import requests
import json


def get_joke():
	r = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})

	if r.status_code == 200:
		joke = json.loads(r.text)['joke']
		return joke
	else:
		return "Couldn't retrieve joke. Response status code {}".format(r.status_code)


if __name__ == "__main__":
	print(get_joke())

