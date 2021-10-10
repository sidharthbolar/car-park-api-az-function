import os
import requests
import logging
import time
print('Begin weather status retrieval')

facility_geocode_dict={
  0: (-33.7975740872452, 151.28550482490462),
  1: (-33.69094554904233, 150.90601054936448),
  2: (-33.713422735697385, 150.93518498072186),
  3: (-33.72988985113614, 150.94368340400078),
  4: (-33.72788721169284, 150.98681377886973),
  5: (-33.737282628426485, 151.0330138402472),
  6: (-33.75685526114473, 151.15471226908386),
  7: (-34.669763303216996, 150.8609573691102),
  10: (-33.690026196015936, 151.29608658442615),
  11: (-33.71438099393689, 151.29962400794756),
  12: (-33.677219572079615, 151.30318135373724),
  13: (-33.75475841712716, 151.28504281141164),
  486: (-33.888062992368596, 151.1267107537433),
  487: (-33.96345520423756, 151.13190534025364),
  488: (-33.77309338853848, 150.9363869212484),
  489: (-33.78473102103219, 151.26719956717682)
}


url = 'https://api.tomorrow.io/v4/timelines?location={}&fields=weatherCode&timesteps=current&units=metric'
headers = {'content-type': 'application/json',
            'apikey':'{}'.format(os.environ["WeatherAPIKey"])}

def get_weather_carpark(data=facility_geocode_dict)  -> dict:
    '''
    Keyword Arguments:
    Pass input dict containing the mapping of carparks facility id to geocodes
    The key represents the carpark facility id and value represents the geocode

    Returns:
    json response captured in dict 
    '''
    weather_response_items_dict={}
    for facility,weather in data.items():
        facility_geocode=str(weather[0])+","+str(weather[1])
        print(facility_geocode)
        print(url.format(facility_geocode))
        logging.info(url.format(facility_geocode))
        response = requests.get(url.format(facility_geocode), headers=headers)
        time.sleep(5)
        logging.info(response.headers)
        logging.info(response.json())
        weather_response_items_dict[facility]=response.json()
    return weather_response_items_dict  