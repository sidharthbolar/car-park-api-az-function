from requests.auth import HTTPBasicAuth
import requests
import os   
import logging
import constants 
import helper

#Initialise constants

url_carpark=constants.URL_CARPARK
url_carpark_history=constants.URL_CARPARK_HISTORY
facility_dict=constants.FACILITY_DICT
#headers=constants.HEADERS

#for date in helper.create_date_range_fn():
#    print(date.strftime('%Y-%m-%d'))

def get_carpark_data(data=facility_dict) -> dict:
    '''
    Keyword Arguments:
    Pass input dict containing the mapping of carparks to facility id
    The key represents the carpark facility id and value represents the name

    Returns:
    json response captured in dict  containing the current carpark status

    '''
    response_items_dict = {}
    for facility,carpark in data.items():
        response = requests.get(url_carpark+facility, headers=headers).json()
        response_items_dict[facility]=response
    return response_items_dict

def get_carpark_data_history(data=facility_dict,date_range=helper.create_date_range_fn()) -> dict:
    '''
    Keyword Arguments:
    Pass input dict containing the mapping of carparks to facility id
    The key represents the carpark facility id and value represents the name

    Returns:
    json response captured in dict  containing the current carpark status

    '''
    response_items_dict = {}
    for facility,carpark in data.items():
        response = requests.get(url+facility, headers=headers).json()
        response_items_dict[facility]=response
    return response_items_dict
