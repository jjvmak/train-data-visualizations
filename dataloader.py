import pandas as pd
import requests


class Dataloader:
    def load_stations(self):
        df = pd.DataFrame(columns=['stationName', 'stationShortCode', 'longitude', 'latitude'])
        response = requests.get("https://rata.digitraffic.fi/api/v1/metadata/stations")
        stations = response.json()
        for s in stations:
            df = df.append({'stationName': s['stationName'],
                            'stationShortCode': s['stationShortCode'],
                            'longitude': s['longitude'],
                            'latitude': s['latitude']},
                           ignore_index=True)

        return df

    def __init__(self):
        locations = self.load_stations()
        print(locations)
        # miteeeeen
