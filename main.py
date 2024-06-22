from analyzer import OlympicAnalyzer


def main():
    # file_path = input("Enter the path to the CSV file: ")
    file_path = 'National_Olympic_Committee_2022_medals.csv'
    analyzer = OlympicAnalyzer(file_path)

    while True:
        print("\n### Olympic Data Analyzer ###")
        print("1. Explore Data")
        print("2. Filter Data")
        print("3. Sort Data")
        print("4. Medals by Country")
        print("5. Average Medals per Participant")
        print("6. Countries with Most Participations")
        print("7. Plot Medals per Country")
        print("8. Plot Medals comparison")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            info, describe = analyzer.explore_data()
            print("\nData Info:")
            print(info)
            print("\nData Description:")
            print(describe)

        elif choice == '2':
            column = input("Enter column name to filter: ")
            value = int(input(f"Enter value to filter in {column}: "))
            filtered_data = analyzer.filter_data(column, value)
            if filtered_data:
                print("\nFiltered Data:")
                print(filtered_data)
            else:
                print(f"Column '{column}' not found.")

        elif choice == '3':
            column = input("Enter column name to sort: ")
            sorted_data = analyzer.sort_data(column)
            if sorted_data:
                print("\nSorted Data:")
                print(sorted_data)
            else:
                print(f"Column '{column}' not found.")

        elif choice == '4':
            medal = str(input("Enter the medal [gold, silver, bronze]: "))
            num_results = int(input("Enter the number of results to display: "))
            medals_by_country_df = analyzer.medals_by_country(medal, num_results)
            if medals_by_country_df is not None:
                print("\nMedals by Country:")
                print(medals_by_country_df)
            else:
                print("No data available for the selected medal type.")

        elif choice == '5':
            num_results = int(input("Enter the number of results to display: "))
            average_medals_df = analyzer.average_medals_per_participant(num_results)
            if average_medals_df is not None:
                print("\nAverage Medals per Participant:")
                print(average_medals_df)
            else:
                print("Unable to calculate average medals per participant.")

        elif choice == '6':
            num_results = int(input("Enter the number of results to display: "))
            most_participations_df = analyzer.countries_with_most_participations(num_results)
            if most_participations_df is not None:
                print("\nCountries with Most Participations:")
                print(most_participations_df)
            else:
                print("Unable to find countries with most participations.")

        elif choice == '7':
            analyzer.plot_medals_per_country()

        elif choice == '8':
            num_results = int(input("Enter the number of results to display: "))
            analyzer.plot_medal_comparison(num_results)

        elif choice == '9':
            analyzer.plot_medal_ratio_pie()

        elif choice == '10':
            country_name = str(input("Enter the country name with code [Brazil (BRA)]: "))
            analyzer.plot_medals_per_country_pie(country_name)

        elif choice == '11':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
