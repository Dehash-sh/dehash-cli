#/usr/bin python3
import requests
import sys
import json

def dehash_crack(hash_value):
    url = "https://dehash.sh/api/search"
    headers = {'Content-Type': 'application/json'}
    payload = {"hashes": [hash_value], "algorithm": None}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        result = data.get('results', [])[0]
        plaintext = result.get('plaintext')
        if plaintext:
            print(f'Hash found: {plaintext}')
        else:
            print('Not found. Cracking it in the cloud.')
    else:
        print('Error in API request')

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != '-crack':
        print("Usage: dehash -crack <hash>")
    else:
        dehash_crack(sys.argv[2])
