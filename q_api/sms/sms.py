import json
import platform
import requests
import config
import auth


default_agent = {
    'sdkVersion': 'python/4.2.0',
    'osPlatform': platform.platform() + " | " + platform.python_version()
}


url = "http://api.coolsms.co.kr/messages/v4/send"
headers = auth.get_headers('API KEY', 'API SECRET')

data = {
    "message": {
        "to": "01058073170",
        "from": "01058073170",
        "text": "랑꾸는 못말려><!"
    }
}
print(json.dumps(data, ensure_ascii=False))
response = requests.post(config.get_url('/messages/v4/send'),
                         headers=auth.get_headers(config.api_key, config.api_secret),
                         json=data)
print(response.status_code)
print(response.text)
