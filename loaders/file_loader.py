import pandas as pd


class FileLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print(f"Data successfully loaded from {self.file_path}")
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except pd.errors.EmptyDataError:
            print(f"No data: {self.file_path}")
        except pd.errors.ParserError:
            print(f"Error parsing data from {self.file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_data(self):
        return self.data
