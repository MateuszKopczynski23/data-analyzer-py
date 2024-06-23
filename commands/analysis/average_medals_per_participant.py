class AverageMedalsPerParticipant:
    def __init__(self, data_manager, analyzer, visualizer):
        self.analyzer = analyzer

    def execute(self):
        num_results = int(input("Enter the number of results to display: "))
        average_medals_df = self.analyzer.average_medals_per_participant(num_results)
        if average_medals_df:
            print("\nAverage Medals per Participant:")
            print(average_medals_df)
        else:
            print("Unable to calculate average medals per participant.")
