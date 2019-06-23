import requests
import time
from datetime import datetime

time = str(datetime.utcnow())

json_time = time.replace(" ", "T")

payload = {
    "embeds": [
        {
            "color": 64154,
            "description": "PBE Live!",
            "title": "Test Notification",
            "timestamp": json_time,
            "url": "",
            "image": {"url": ""},
            "thumbnail": {},
            "footer": {"text": "By Jin Yi", "icon_url": ""}
        }
    ]
}

r = requests.post(
    "https://discordapp.com/api/webhooks/591393163902713858/k34FyjV-LgX6ZswWFAK3VSFxKXPVx75gG2Iq3wHDO97EalvOnTqLvM1wip6bUWmtSZtl", json=payload)

"""
while True:

    status = requests.get(
        "https://status.pbe.leagueoflegends.com/shards/pbe").json()
    if status["services"][0]["status"] != "offline":
        print("online")
        r = requests.post(
            "https://discordapp.com/api/webhooks/591393163902713858/k34FyjV-LgX6ZswWFAK3VSFxKXPVx75gG2Iq3wHDO97EalvOnTqLvM1wip6bUWmtSZtl", json=payload)
    else:
        # print(status["services"][0])
        print("offline")
    # for service in status["services"]:
    #    print(f"{service['name']}: {service['status']}")

    time.sleep(2)
"""
