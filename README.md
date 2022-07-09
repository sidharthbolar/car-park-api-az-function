:warning: Project under :construction:

# Project Inspiration
The [Car Park API](https://opendata.transport.nsw.gov.au/dataset/car-park-api#:~:text=The%20Car%20Park%20API%20provides,to%20travel%20on%20public%20transport.) provides real time and historical occupancy of selected car parks . 
This API provides the occupancy for Transport Park&Ride car parks and Sydney Metro car parks.
Transport Park&Ride is designed to free-up more spaces at commuter car parks for those who want to travel on public transport. 
The data feed contains the parking occupancy information by type in real time.
The Sydney Metro stations for Tallawong, Bella Vista, Hills Showground, Cherrybrook and Kellyville are reporting real time occupancy levels.

It is intended other car park occupancy data will be enabled via this API in the future.

## Objective of this project is 
1. To capture the status and publish the car park 	:car: availability in Real time in a structured - read to consume manner 
2. Publish the resuls in a public dashboard :chart_with_upwards_trend:

## Solution
* The transport NSW API will be invoked by Azure functions :cloud:
* Azure functions are written in Python :snake: and is configured to be Time Triggered to run every 15 mins
* The Results will be persisted in Azure ADLS2 :file_folder
* The intermedaite results are temporarily passed through :arrow_forward: Azure Event Hub 
* serves as the intermediary decoupling the producer and consumer, for creation a decoupled data pipeline



