# First must acquire auth to use the congress.gov api and store in password vault.
# Example below is for 1Password

import subprocess
import json
import pandas as pd
import urllib
import urllib.request
from urllib.error import HTTPError, URLError

URL = 'https://developer.nrel.gov/api/alt-fuel-stations/v1.json'
opassword_vault = 'Personal'
opassword_item = 'congress.gov api key'


def opass_get_vault_item_value(item, vault, label):
    '''Return the 1password item's label out of vault'''
    # must have logged into 1Password cli for this to work

    result = subprocess.run(['op', 'item', 'get', f'{item}', '--vault', f'{vault}', '--format', 'json'],
                            check=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    id = json.loads(result.stdout)['id']
    result = subprocess.run(f'op item get {id} --format json'.split(' '),
                            check=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    df = pd.DataFrame(json.loads(result.stdout)['fields'])
    return df[df['label'] == label]['value'].values[0]


api_key = opass_get_vault_item_value(item=opassword_item, vault=opassword_vault, label='api_key')
parameters = urllib.parse.urlencode({'limit': 1, 'api_key': api_key})

try:
    URL = f'{URL}?{parameters}'
    print(f'opening {URL}...')
    with urllib.request.urlopen(URL) as response:
        print(response.status)
        print(response.read())
        print(response)
except HTTPError as error:
    breakpoint()
    print(error.status, error.reason)
except URLError as error:
    breakpoint()
    print(error.reason)
except TimeoutError:
    breakpoint()
    print("Request timed out")
