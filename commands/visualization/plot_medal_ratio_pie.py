class PlotMedalRatioPie:
    def __init__(self, data_manager, analyzer, visualizer):
        self.visualizer = visualizer

    def execute(self):
        self.visualizer.plot_medal_ratio_pie()
