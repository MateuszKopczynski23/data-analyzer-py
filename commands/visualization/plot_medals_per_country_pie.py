class PlotMedalsPerCountryPie:
    def __init__(self, data_manager, analyzer, visualizer):
        self.visualizer = visualizer

    def execute(self):
        country_name = input("Enter the country name with code [Brazil (BRA)]: ")
        self.visualizer.plot_medals_per_country_pie(country_name)
