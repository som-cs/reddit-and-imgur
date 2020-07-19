from imgurpython import ImgurClient
import requests
import json

class imgur:
    imgur_client_id = '48a4853a9c844df'
    imgur_client_secret = 'ebe25d36f196cff544aca408e8d7b02283290c50'
    refresh_token = "1750e9d83514f1b4f9c6260ba7974ade9c0ab58a"
    client = None

    def imgur_init(self):
        self.client = ImgurClient(self.imgur_client_id, self.imgur_client_secret)

        url = "https://api.imgur.com/oauth2/token"

        payload = {'refresh_token': self.refresh_token,
        'client_id': self.imgur_client_id,
        'client_secret': self.imgur_client_secret,
        'grant_type': 'refresh_token'}
        headers= {}
        files = []
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        a = json.loads(response.text)
        self.client.set_user_auth(a["access_token"], a["refresh_token"])

    def upload_fking_image(self):
        self.client.upload_from_path(r"pil_text_font2.png", anon=False)
