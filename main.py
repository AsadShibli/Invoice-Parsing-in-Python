import json
import requests

url = "https://ocr.asprise.com/api/receipt"
image = "data/p1.png"

res = requests.post(url, data=
                    {
                        'api-key':'TEST',
                        'recognizer':'auto',
                        'ref_no':'oct_python_123'

                    },
                    files = {
                        'file':open(image , 'rb')
                    })
with open("response1.json", "w") as f:
    json.dump(json.loads(res.text), f )
