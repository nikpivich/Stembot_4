import json
import requests
import config
from kandinski import save_image

class KandinskiGen:
    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}'
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate_image(self, prompt, model, images = 1, width = 1024, height = 1024):
        params = {
            'type': 'GENERATE',
            'numImages': images,
            'width': width,
            'height': height,
            'generateParams': {
                'query': f'{prompt}'
            }
        }

        data = {
            'model_id': (None,  model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        print(data)
        return data['uuid']

    def chech_gen(self, request_id, attempts = 10 , delay = 10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            print(data)
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            import time
            time.sleep(delay)


def generate(prompt):
    api = KandinskiGen('https://api-key.fusionbrain.ai/', config.KANDINSKI_API_KEY, config.KANDINSKI_SECRET_KEY)
    model_id = api.get_model()
    uuid = api.generate_image(prompt, model_id)
    image = api.chech_gen(uuid)
    name = save_image.save_image_from_base64(image[0], 'imageGen')
    return name