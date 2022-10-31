import requests
import json
import time
import random
from os import makedirs

def get_track_by_tags(tags, pat, duration, maxit=20, loop=False):
    if loop:
        mode = "loop"
    else:
        mode = "track"
    r = requests.post('https://api-b2b.mubert.com/v2/RecordTrackTTM',
                   json={
                       "method": "RecordTrackTTM",
                       "params": {
                           "pat": pat,
                           "duration": duration,
                           "tags": tags,
                           "mode": mode
                       }
                   })

    rdata = json.loads(r.text)
    assert rdata['status'] == 1, rdata['error']['text']
    trackurl = rdata['data']['tasks'][0]['download_link']

    print('Generating track ', end='')
    for i in range(maxit):
        r = requests.get(trackurl)
        if r.status_code == 200:
            return trackurl
        time.sleep(1)

def download(url):
    makedirs("outputs", exist_ok=True)
    filename = f"outputs/{time.time()}.mp3"
    with requests.get(url, stream=True) as req:
        req.raise_for_status()
        with open(filename, "wb") as file:
            for chunk in req.iter_content(chunk_size=8192):
                file.write(chunk)