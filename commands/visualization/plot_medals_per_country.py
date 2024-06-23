class PlotMedalsPerCountry:
    def __init__(self, data_manager, analyzer, visualizer):
        self.visualizer = visualizer

    def execute(self):
        self.visualizer.plot_medals_per_country()
