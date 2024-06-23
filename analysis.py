from helpers.columns_info import ColumnsInfo


class DataAnalysis:
    def __init__(self, data):
        self.data = data
        self.column_info = ColumnsInfo()
        self.data.columns = self.data.columns.str.strip()

    def medals_by_country(self, medal="gold", num_results=None):
        try:
            valid_medals = ['gold', 'silver', 'bronze']
            if medal.lower() not in valid_medals:
                return "Invalid medal type. Please choose from 'gold', 'silver', or 'bronze'."

            column_name = f"SOG_{medal}"
            columns_to_validate = ['team', column_name]
            self.column_info.validate_columns(self.data, columns_to_validate)
            self.column_info.convert_columns_to_numeric(self.data, [column_name])

            medals_by_country = self.data.groupby('team')[column_name].sum().reset_index()
            medals_by_country_sorted = medals_by_country.sort_values(by=column_name, ascending=False)
            top_countries = medals_by_country_sorted[['team', column_name]].nlargest(num_results, column_name)

            return top_countries.to_string(index=False)
        except KeyError as e:
            return f"Error: {e}"

    def average_medals_per_participant(self, num_results=None):
        try:
            required_columns = self.column_info.medals_columns + self.column_info.participations_columns
            self.column_info.validate_columns(self.data, required_columns)
            self.column_info.convert_columns_to_numeric(self.data, required_columns)

            sog_medals = self.data['SOG_total_medals']
            wog_medals = self.data['WOG_total_medals']
            sog_participations = self.data['NO_SOG_participated']
            wog_participations = self.data['NO_WOG_participated']

            self.data['Average_medals_per_participant'] = (sog_medals + wog_medals) / (
                    sog_participations + wog_participations)

            self.data.dropna(subset=['Average_medals_per_participant'], inplace=True)
            top_averages = self.data.nlargest(num_results, 'Average_medals_per_participant')

            return top_averages[['team', 'Average_medals_per_participant']].to_string(index=False)
        except KeyError as e:
            return f"Error: {e}"
        except TypeError as e:
            return f"Error: {e}"

    def countries_with_most_participations(self, num_results=None):
        try:
            self.column_info.validate_columns(self.data, self.column_info.participations_columns)
            self.column_info.convert_columns_to_numeric(self.data, self.column_info.participations_columns)

            sog_participations = self.data['NO_SOG_participated']
            wog_participations = self.data['NO_WOG_participated']

            self.data['Total_participations'] = sog_participations + wog_participations
            most_participations = self.data[['team', 'Total_participations']].nlargest(num_results,
                                                                                       'Total_participations')

            return most_participations.to_string(index=False)
        except KeyError as e:
            return f"Error: {e}"
