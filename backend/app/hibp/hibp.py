# Author/Ilija

import hashlib
import requests

def check_pwned(password):
    # 1. SHA1 hash password
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    # 2. Call HIBP API with prefix
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    headers = {
        "User-Agent": "#"
    }
    res = requests.get(url, headers=headers)
    # res = requests.get(url)

    if res.status_code != 200:
        return {"error": "HIBP API error"}

    hashes = res.text.splitlines()
    for h in hashes:
        hash_suffix, count = h.split(":")
        if hash_suffix == suffix:
            return {
                "pwned": True,
                "count": int(count),
                "message": f"This password has been seen {count} times in data breaches. Change it immediately."
            }

    return {
        "pwned": False,
        "count": 0,
        "message": "This password has not been seen in known data breaches."
    }
