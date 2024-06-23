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
        print("4. Get the top countries based on the specified medal type")
        print("5. Calculate the average medals per participant for each country")
        print("6. Get the countries with the most participations")
        print("7. Plot total medals won by each country")
        print("8. Plot comparison of Summer and Winter Olympic medals")
        print("9. Plot the ratio of gold, silver, and bronze medals")
        print("10. Plot medal composition for a specific country")
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
