class MedalsByCountry:
    def __init__(self, data_manager, analyzer, visualizer):
        self.analyzer = analyzer

    def execute(self):
        medal = input("Enter the medal [gold, silver, bronze]: ")
        num_results = int(input("Enter the number of results to display: "))
        medals_by_country_df = self.analyzer.medals_by_country(medal, num_results)
        if medals_by_country_df:
            print("\nTop countries based on the specified medal type:")
            print(medals_by_country_df)
        else:
            print("No data available for the selected medal type.")
