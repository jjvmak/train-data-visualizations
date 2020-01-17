import folium
from folium.plugins import HeatMap

from dataloader import Dataloader


class Lateness_map:

    def init_map(self, data):
        converted_data = Dataloader.convert_data_for_heat_map(data).tolist()
        print(converted_data)
        m = folium.Map(location=[65.192059, 24.945831], tiles='stamentoner', zoom_start=5)
        HeatMap(converted_data).add_to(m)

        # markers
        # for index, row in data.iterrows():
        #     folium.Marker([row['latitude'], row['longitude']],
        #                   tooltip=row['stationName'], icon=None).add_to(m)

        m.save('map.html')
        print('map.html saved to disk')
