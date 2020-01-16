import folium
from folium.plugins import HeatMap


class Lateness_map:

    def init_map(self, data):
        converted_data = self.convert_data_for_heat_map(data).tolist()
        print(converted_data)
        m = folium.Map(location=[65.192059, 24.945831], tiles='stamentoner', zoom_start=5)
        HeatMap(converted_data).add_to(m)
        m.save('map.html')
        print('map.html saved to disk')

    def convert_data_for_heat_map(self, data):
        print('convert data for heat map')
        return data.iloc[:, 2:5].to_numpy()
