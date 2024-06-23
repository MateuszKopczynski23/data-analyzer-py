class PlotMedalsPerCountry:
    def __init__(self, data_manager, analyzer, visualizer):
        self.visualizer = visualizer

    def execute(self):
        num_results = int(input("Enter the number of results to display: "))
        self.visualizer.plot_medals_per_country(num_results)
