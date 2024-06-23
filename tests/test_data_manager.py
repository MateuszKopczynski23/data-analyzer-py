import unittest
from data_manager import DataManager
import pandas as pd


class TestDataManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.csv_path = 'test_data.csv'
        cls.data_manager = DataManager(cls.csv_path)

    def test_load_data_invalid_path(self):
        invalid_path = 'invalid_path.csv'
        with self.assertRaises(FileNotFoundError):
            DataManager(invalid_path)

    def test_explore_data(self):
        data, describe = self.data_manager.explore_data()
        self.assertIsInstance(data, pd.DataFrame)
        self.assertIsInstance(describe, str)
        self.assertIn("SOG_total_medals", data.columns)
        self.assertIn("count", describe)

    def test_filter_data_existing_value(self):
        filtered_data = self.data_manager.filter_data('NO_WOG_participated', 8)
        self.assertIsInstance(filtered_data, str)
        self.assertIn('8', filtered_data)

    def test_filter_data_non_existing_value(self):
        filtered_data = self.data_manager.filter_data('NO_SOG_participated', 100)
        self.assertIsInstance(filtered_data, str)
        self.assertIn('Empty DataFrame', filtered_data)

    def test_filter_data_non_existing_column(self):
        filtered_data = self.data_manager.filter_data('NonExistingColumn', 'value')
        self.assertIsNone(filtered_data)

    def test_sort_data_invalid_column(self):
        sorted_data = self.data_manager.sort_data('invalid_column')
        self.assertIsNone(sorted_data)


if __name__ == '__main__':
    unittest.main()
