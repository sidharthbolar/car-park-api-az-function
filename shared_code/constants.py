import os

FACILITY_DICT={
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

URL_CARPARK = 'https://api.transport.nsw.gov.au/v1/carpark?facility='

URL_CARPARK_HISTORY='https://api.transport.nsw.gov.au/v1/carpark/history?'

#HEADERS = {'content-type': 'application/json',
#          'Authorization':'apikey {}'.format(os.environ["NSWAPIKey"])}

