from dataloader import Dataloader


class Main:
    if __name__ == "__main__":
        data_loader = Dataloader()
        # data_loader.get_and_save_stations()
        # df = data_loader.load_stations()
        # print(df)
        data_loader.calculate_lateness_of_station('SK')
