import pandas as pd
import requests


class Dataloader:
    STATIONS_PATH = 'data/stations.pkl'
    STATIONS_URL = 'https://rata.digitraffic.fi/api/v1/metadata/stations'
    TRAINS_URL = 'https://rata.digitraffic.fi/api/v1/live-trains/station/'
    TRAINS_PARAMETERS = '?arrived_trains=10&arriving_trains=0&departed_trains=10&departing_trains=0&include_nonstopping=false'
    LATENESS_PATH = 'data/lateness.pkl'

    def get_and_save_stations(self):
        print('get and save stations')
        df = pd.DataFrame(columns=['stationName', 'stationShortCode', 'latitude', 'longitude', 'lateness'])
        response = requests.get(self.STATIONS_URL)
        stations = response.json()
        for s in stations:
            df = df.append({'stationName': s['stationName'],
                            'stationShortCode': s['stationShortCode'],
                            'latitude': s['latitude'],
                            'longitude': s['longitude']},
                           ignore_index=True)

        df.to_pickle(self.STATIONS_PATH)
        print('done!')
        return df

    def load_stations(self):
        print('load stations')
        df = pd.read_pickle(self.STATIONS_PATH)
        print('done')
        return df

    def calculate_lateness_of_station(self, station_code):
        print('calculate lateness for: ' + station_code)
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

        return diff

    def calculate_total_lateness(self):
        df = self.load_stations()
        for index, row in df.iterrows():
            station_code = row['stationShortCode']
            lateness = self.calculate_lateness_of_station(station_code)
            df.at[index, 'lateness'] = lateness

        df.to_pickle(self.LATENESS_PATH)
        print('total lateness calculated!')

    def load_total_lateness(self):
        print('loading total lateness')
        df = pd.read_pickle(self.LATENESS_PATH)
        print('done!')
        return df

    @staticmethod
    def convert_data_for_heat_map(data):
        print('convert data for heat map')
        converted = data.iloc[:, 2:5].to_numpy()
        v = converted[:, 2]
        converted[:, 2] = (v - v.min()) / (v.max() - v.min())

        # print(converted)

        return converted
