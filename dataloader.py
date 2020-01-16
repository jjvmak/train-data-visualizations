import pandas as pd
import requests


class Dataloader:
    STATIONS_PATH = 'data/stations.pkl'
    STATIONS_URL = 'https://rata.digitraffic.fi/api/v1/metadata/stations'
    TRAINS_URL = 'https://rata.digitraffic.fi/api/v1/live-trains/station/'
    TRAINS_PARAMETERS = '?arrived_trains=10&arriving_trains=0&departed_trains=10&departing_trains=0&include_nonstopping=false'

    def get_and_save_stations(self):
        df = pd.DataFrame(columns=['stationName', 'stationShortCode', 'longitude', 'latitude'])
        response = requests.get(self.STATIONS_URL)
        stations = response.json()
        for s in stations:
            df = df.append({'stationName': s['stationName'],
                            'stationShortCode': s['stationShortCode'],
                            'longitude': s['longitude'],
                            'latitude': s['latitude']},
                           ignore_index=True)

        df.to_pickle(self.STATIONS_PATH)
        return df

    def load_stations(self):
        df = pd.read_pickle(self.STATIONS_PATH)
        return df

    def calculate_lateness_of_station(self, station_code):
        response = requests.get(self.TRAINS_URL + station_code + self.TRAINS_PARAMETERS)
        trains = response.json()
        diff = 0
        for train in trains:
            time_tables = train['timeTableRows']
            for time_table in time_tables:
                if time_table['stationShortCode'] == station_code:
                    if 'differenceInMinutes' not in time_table:
                        continue
                    if time_table['differenceInMinutes'] > 0:
                        diff += time_table['differenceInMinutes']
        print(diff)
        return diff
