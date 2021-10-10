from requests.auth import HTTPBasicAuth
import requests
import os
import logging

url = 'https://api.transport.nsw.gov.au/v1/carpark?facility='
headers = {'content-type': 'application/json',
            'Authorization':'apikey {}'.format(os.environ["NSWAPIKey"])}
facility_dict={
  "0": "Manly Vale Car Park",
  "1": "Tallawong Station Car Park",
  "2": "Kellyville Station Car Park",
  "3": "Bella Vista Station Car Park",
  "4": "Hills Showground Station Car Park",
  "5": "Cherrybrook Station Car Park",
  "6": "Gordon Henry St North Car Park",
  "7": "Kiama Car Park",
  "10": "Warriewood Car Park",
  "11": "Narrabeen Car Park",
  "12": "Mona Vale Car Park",
  "13": "Dee Why Car Park",
  "486": "Ashfield Car Park",
  "487": "Kogarah Car Park",
  "488": "Seven Hills Car Park",
  "489": "Manly Vale Car Park"
}

def get_carpark_data() -> dict:
    '''
    Keyword Arguments:
    Pass input dict containing the mapping of carparks to facility id
    The key represents the carpark facility id and value represents the name

    Returns:
    json response captured in dict  containing the current carpark status

    '''
    response_items_dict = {}
    for facility,carpark in facility_dict.items():
        response = requests.get(url+facility, headers=headers).json()
        response_items_dict[facility]=response
    return response_items_dict