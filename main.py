from dataloader import Dataloader


class Main:
    if __name__ == "__main__":
        data_loader = Dataloader()
        df = data_loader.load_total_lateness()
        print(df)
