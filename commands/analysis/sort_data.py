class SortData:
    def __init__(self, data_manager, analyzer, visualizer):
        self.data_manager = data_manager

    def execute(self):
        column = input("Enter column name to sort: ")
        sort_type = input("Enter sort type (asc for ascending, desc for descending): ").strip().lower()

        if sort_type not in ['asc', 'desc']:
            print("Invalid sort type. Please enter 'asc' or 'desc'.")
            return

        is_ascending = sort_type == 'asc'
        sorted_data = self.data_manager.sort_data(column, is_ascending)
        if sorted_data:
            print("\nSorted Data:")
            print(sorted_data)
        else:
            print(f"Column '{column}' not found.")
