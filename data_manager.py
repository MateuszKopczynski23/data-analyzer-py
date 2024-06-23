import pandas as pd


class DataManager:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def explore_data(self):
        info = self.data.info()
        describe = self.data.describe().to_string(float_format="{:.2f}".format)
        return info, describe

    def filter_data(self, column, value):
        try:
            filtered_data = self.data[self.data[column] == value]
            return filtered_data.to_string()
        except KeyError:
            return None

    def sort_data(self, column):
        try:
            sorted_data = self.data.sort_values(by=column)
            return sorted_data.to_string()
        except KeyError:
            return None
