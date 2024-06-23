from data_manager import DataManager
from analysis import DataAnalysis
from visualization import DataVisualization
from resolvers.CommandResolver import CommandResolver


def main():
    # file_path = input("Enter the path to the CSV file: ")
    file_path = 'data/olympic_committee_2022.csv'

    data_manager = DataManager(file_path)
    analyzer = DataAnalysis(data_manager.data)
    visualizer = DataVisualization(data_manager.data)

    resolver = CommandResolver(data_manager, analyzer, visualizer)
    resolver.run()


if __name__ == "__main__":
    main()
