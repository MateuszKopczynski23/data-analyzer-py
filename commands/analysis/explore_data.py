class ExploreData:
    def __init__(self, data_manager, analyzer, visualizer):
        self.data_manager = data_manager

    def execute(self):
        data, describe = self.data_manager.explore_data()
        print("\nData Info:")
        print(data)
        print("\nData Description:")
        print(describe)
