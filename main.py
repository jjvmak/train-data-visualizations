from dataloader import Dataloader
from lateness_map import Lateness_map


class Main:
    if __name__ == "__main__":
        data_loader = Dataloader()
        # data_loader.get_and_save_stations()
        # data_loader.calculate_total_lateness()

        # load from disk
        df = data_loader.load_total_lateness()
        lm = Lateness_map()
        lm.init_map(df)
