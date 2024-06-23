from data_manager import DataManager
from analysis import DataAnalysis
from loaders.file_loader import FileLoader
from visualization import DataVisualization
from resolvers.command_resolver import CommandResolver


def main():
    file_path = input("Enter the path to the CSV file: ").strip()

    file_loader = FileLoader(file_path)
    file_loader.load_data()

    data = file_loader.get_data()
    if data is None:
        print("Failed to load data. Exiting program.")
        return

    data_manager = DataManager(file_path)
    analyzer = DataAnalysis(data_manager.data)
    visualizer = DataVisualization(data_manager.data)

    resolver = CommandResolver(data_manager, analyzer, visualizer)
    resolver.run()


if __name__ == "__main__":
    main()
