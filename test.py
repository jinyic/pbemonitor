import requests
import time
from datetime import datetime

# for testing
dtime = str(datetime.utcnow())
json_time = dtime.replace(" ", "T")

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

time
while True:

    r = requests.get(
        "https://status.pbe.leagueoflegends.com/shards/pbe")
    print(r.status_code)
    status = r.json()
    if status["services"][0]["status"] != "offline":
        print("online")

    else:
        # print(status["services"][0])
        print("offline")
    # for service in status["services"]:
    #    print(f"{service['name']}: {service['status']}")
    time.sleep(2)
