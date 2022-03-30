import os
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = os.path.basename(file_path)
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': file_name, 'overwrite': 'true'}
        r = requests.get(upload_url, headers=headers, params=params).json()
        href = r['href']
        response = requests.put(href, data=open('test.txt', 'rb'))

token = ''
path = ''

uploader = YaUploader(token)
result = uploader.upload(path)