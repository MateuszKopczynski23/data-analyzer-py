from commands import (
    AverageMedalsPerParticipant,
    CountriesWithMostParticipations,
    ExploreData,
    FilterData,
    MedalsByCountry,
    PlotMedalComparison,
    PlotMedalRatioPie,
    PlotMedalsPerCountry,
    PlotMedalsPerCountryPie,
    SortData,
    Exit
)


class CommandResolver:
    def __init__(self, data_manager, analyzer, visualizer):
        self.data_manager = data_manager
        self.analyzer = analyzer
        self.visualizer = visualizer
        self.choices = {
            '1': ExploreData,
            '2': FilterData,
            '3': SortData,
            '4': MedalsByCountry,
            '5': AverageMedalsPerParticipant,
            '6': CountriesWithMostParticipations,
            '7': PlotMedalsPerCountry,
            '8': PlotMedalComparison,
            '9': PlotMedalRatioPie,
            '10': PlotMedalsPerCountryPie,
            '11': Exit
        }

    @staticmethod
    def display():
        print("\n### Olympic Data Analyzer ###")
        print("1. Explore Data")
        print("2. Filter Data")
        print("3. Sort Data")
        print("4. Medals by Country")
        print("5. Average Medals per Participant")
        print("6. Countries with Most Participations")
        print("7. Plot Medals per Country")
        print("8. Plot Medals comparison")
        print("9. Plot Medal Ratio Pie")
        print("10. Plot Medals per Country Pie")
        print("11. Exit")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice (1-11): ")
            command_class = self.choices.get(choice)

            if isinstance(command_class, type):
                command_instance = command_class(self.data_manager, self.analyzer, self.visualizer)
                command_instance.execute()
            else:
                print("Invalid choice. Please enter a number from 1 to 11.")
