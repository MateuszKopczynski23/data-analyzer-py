import pandas as pd


class ColumnsInfo:
    def __init__(self):
        self.medals_columns = ['SOG_gold', 'SOG_silver', 'SOG_bronze', 'SOG_total_medals', 'WOG_total_medals']
        self.participations_columns = ['NO_SOG_participated', 'NO_WOG_participated']

    @staticmethod
    def convert_columns_to_numeric(data, columns):
        for column in columns:
            data[column] = pd.to_numeric(data[column], errors='coerce')

    @staticmethod
    def validate_columns(data, required_columns):
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise KeyError(f"Missing columns: {', '.join(missing_columns)}")
