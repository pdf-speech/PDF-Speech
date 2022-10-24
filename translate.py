import requests
import uuid

# Add your key and endpoint
key = "e080665c75bc4281819fa6c7b56330e9"
endpoint = "https://api.cognitive.microsofttranslator.com"


class MyTranslate:
    def __init__(self, text_input, translate_to_language):
        self.location = "centralindia"
        self.path = '/translate'
        self.constructed_url = endpoint + self.path
        self.params = {
            'api-version': '3.0',
            'from': 'en',
            'to': translate_to_language
        }
        self.constructed_url = endpoint + self.path

        self.headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        self.input_text = text_input
        self.body = [{
            'text': self.input_text
        }]

    def connection(self):
        request = requests.post(self.constructed_url, params=self.params, headers=self.headers, json=self.body)
        response = request.json()
        return response[0]["translations"][0]["text"]


