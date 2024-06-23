class CountriesWithMostParticipations:
    def __init__(self, data_manager, analyzer, visualizer):
        self.analyzer = analyzer

    def execute(self):
        num_results = int(input("Enter the number of results to display: "))
        most_participations_df = self.analyzer.countries_with_most_participations(num_results)
        if most_participations_df:
            print("\nCountries with the most participations:")
            print(most_participations_df)
        else:
            print("Unable to find countries with most participations.")
