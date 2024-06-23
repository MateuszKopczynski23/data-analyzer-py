import pandas as pd


class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def medals_by_country(self, medal="gold", num_results=None):
        try:
            self.data.columns = self.data.columns.str.strip()

            valid_medals = ['gold', 'silver', 'bronze']
            if medal.lower() not in valid_medals:
                return "Invalid medal type. Please choose from 'gold', 'silver', or 'bronze'."

            column_name = f"SOG_{medal}"

            if 'team' not in self.data.columns:
                raise KeyError("Missing 'team' column in the dataset.")

            self.data[column_name] = pd.to_numeric(self.data[column_name], errors='coerce')

            medals_by_country = self.data.groupby('team')[column_name].sum().reset_index()
            medals_by_country_sorted = medals_by_country.sort_values(by=column_name, ascending=False)
            num_countries = medals_by_country_sorted[['team', column_name]].nlargest(num_results, column_name)

            return num_countries.to_string(index=False)
        except KeyError:
            return "Brak kolumny 'team' lub 'column_name'."

    def average_medals_per_participant(self, num_results=None):
        try:
            self.data['SOG_total_medals'] = pd.to_numeric(self.data['SOG_total_medals'], errors='coerce')
            self.data['WOG_total_medals'] = pd.to_numeric(self.data['WOG_total_medals'], errors='coerce')
            self.data['NO_SOG_participated'] = pd.to_numeric(self.data['NO_SOG_participated'], errors='coerce')
            self.data['NO_WOG_participated'] = pd.to_numeric(self.data['NO_WOG_participated'], errors='coerce')

            self.data['Average_medals_per_participant'] = (self.data['SOG_total_medals'] + self.data[
                'WOG_total_medals']) / (self.data['NO_SOG_participated'] + self.data['NO_WOG_participated'])

            self.data.dropna(subset=['Average_medals_per_participant'], inplace=True)
            average_medals_sorted = self.data.nlargest(num_results, 'Average_medals_per_participant')

            return average_medals_sorted[['team', 'Average_medals_per_participant']].to_string(index=False)
        except KeyError:
            return "Required columns for average medals calculation not found."
        except TypeError as e:
            return f"Error: {e}"

    def countries_with_most_participations(self, num_results=None):
        try:
            self.data['Total_participations'] = self.data['NO_SOG_participated'] + self.data['NO_WOG_participated']
            most_participations = self.data[['team', 'Total_participations']].nlargest(num_results,
                                                                                       'Total_participations')
            return most_participations.to_string(index=False)
        except KeyError:
            return "Required columns for most participations calculation not found."
