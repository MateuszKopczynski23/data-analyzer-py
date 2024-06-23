class SortData:
    def __init__(self, data_manager, analyzer, visualizer):
        self.data_manager = data_manager

    def execute(self):
        column = input("Enter column name to sort: ")
        sorted_data = self.data_manager.sort_data(column)
        if sorted_data:
            print("\nSorted Data:")
            print(sorted_data)
        else:
            print(f"Column '{column}' not found.")
