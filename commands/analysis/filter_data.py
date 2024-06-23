class FilterData:
    def __init__(self, data_manager, analyzer, visualizer):
        self.data_manager = data_manager

    def execute(self):
        column = input("Enter column name to filter: ")
        value = input(f"Enter value to filter in {column}: ")
        filtered_data = self.data_manager.filter_data(column, value)
        if filtered_data:
            print("\nFiltered Data:")
            print(filtered_data)
        else:
            print(f"Column '{column}' not found.")
