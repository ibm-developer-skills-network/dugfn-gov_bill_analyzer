# First must acquire auth to use the congress.gov api and store in password vault.
# Example below is for 1Password

import subprocess
import json
import pandas as pd
import urllib
import urllib.request
from urllib.error import HTTPError, URLError

import click

opassword_vault = 'Personal'
opassword_item = 'congress.gov api key'
API = 'https://api.congress.gov/v3'


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




def get_api_results(URL):
    try:
        with urllib.request.urlopen(URL) as response:
            return json.loads(response.read())
    except HTTPError as error:
        breakpoint()
        print(error.status, error.reason)
    except URLError as error:
        breakpoint()
        print(error.reason)
    except TimeoutError:
        breakpoint()
        print("Request timed out")


def bill_details(api_key, congress, bill_type, bill_number):
    endpoint = 'bill'
    auth_parameters = urllib.parse.urlencode({'limit': 1, 'api_key': api_key})
    url = f'{API}/{endpoint}/{congress}/{bill_type}/{bill_number}?{auth_parameters}'
    # address of the specific endpoint
    return get_api_results(url)


@click.command()
@click.option("--congress-number", help="file with student data", required=True, type=str)
@click.option("--bill-type", help="hr, ...", required=True, type=str)
@click.option("--bill-number", help="bill number digits", required=True, type=int)
def congress_bill_api(congress_number, bill_type, bill_number):
    api_key = opass_get_vault_item_value(item=opassword_item, vault=opassword_vault, label='api_key')
    result = bill_details(api_key, congress_number, bill_type, bill_number)
    print(result)


if __name__ == '__main__':
    congress_bill_api()
