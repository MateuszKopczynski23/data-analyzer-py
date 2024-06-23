import matplotlib.pyplot as plt
from helpers.columns_info import ColumnsInfo


class DataVisualization:
    _LABELS = ['Gold', 'Silver', 'Bronze']

    def __init__(self, data):
        self.data = data
        self.column_info = ColumnsInfo()
        self.data.columns = self.data.columns.str.strip()

    @staticmethod
    def _calculate_medal_totals(country_data):
        total_gold = country_data['SOG_gold'].sum()
        total_silver = country_data['SOG_silver'].sum()
        total_bronze = country_data['SOG_bronze'].sum()

        sizes = [total_gold, total_silver, total_bronze]
        return sizes

    def plot_medals_per_country(self, num_results=None):
        try:
            self.column_info.validate_columns(self.data, ['team', 'SOG_total_medals'])
            self.column_info.convert_columns_to_numeric(self.data, ['SOG_total_medals'])

            if num_results is None:
                num_results = len(self.data)

            sorted_data = self.data[['team', 'SOG_total_medals']].nlargest(num_results, 'SOG_total_medals')

            plt.figure(figsize=(12, 6))
            plt.bar(sorted_data['team'], sorted_data['SOG_total_medals'])
            plt.xlabel('Country')
            plt.ylabel('Total Medals')
            plt.title(f'Top {num_results} Countries by Total Medals')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        except KeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def plot_medal_comparison(self, num_results=None):
        try:
            self.column_info.validate_columns(self.data, ['team', 'SOG_total_medals', 'WOG_total_medals'])
            self.column_info.convert_columns_to_numeric(self.data, ['SOG_total_medals', 'WOG_total_medals'])

            self.data['Total_medals'] = self.data['SOG_total_medals'] + self.data['WOG_total_medals']
            sorted_data = self.data.sort_values(by='Total_medals', ascending=False)

            if num_results:
                sorted_data = sorted_data.head(num_results)

            selected_data = sorted_data[['team', 'SOG_total_medals', 'WOG_total_medals']].set_index('team')
            ax = selected_data.plot(kind='bar', figsize=(12, 8), color=['skyblue', 'salmon'])

            ax.set_xlabel('Country')
            ax.set_ylabel('Number of Medals')
            ax.set_title('Total Medals in Summer vs Winter Olympics')
            ax.legend(['Summer Olympics', 'Winter Olympics'])

            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except KeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def plot_medal_ratio_pie(self):
        try:
            self.column_info.validate_columns(self.data, ['SOG_gold', 'SOG_silver', 'SOG_bronze'])
            self.column_info.convert_columns_to_numeric(self.data, ['SOG_gold', 'SOG_silver', 'SOG_bronze'])

            sizes = self._calculate_medal_totals(self.data)
            colors = ['gold', 'silver', 'brown']
            explode = (0.1, 0, 0)

            plt.figure(figsize=(8, 8))
            plt.pie(sizes, explode=explode, labels=self._LABELS, colors=colors, autopct='%1.1f%%', shadow=True,
                    startangle=140)
            plt.title('Ratio of Gold, Silver, and Bronze Medals')
            plt.axis('equal')
            plt.show()
        except KeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def plot_medals_per_country_pie(self, country_name):
        try:
            self.column_info.validate_columns(self.data, ['team', 'SOG_gold', 'SOG_silver', 'SOG_bronze'])
            self.column_info.convert_columns_to_numeric(self.data, ['SOG_gold', 'SOG_silver', 'SOG_bronze'])

            matching_countries = self.data[self.data['team'].str.contains(country_name, case=False, na=False)]

            if matching_countries.empty:
                print(f"No data found for country: {country_name}")
                return

            if len(matching_countries) > 1:
                print(f"Multiple matches found for '{country_name}':")
                print(matching_countries['team'].unique())
                chosen_team = input("Enter the full team name from the list above: ").strip()
                country_data = self.data[self.data['team'] == chosen_team]
            else:
                country_data = matching_countries

            if country_data.empty:
                print(f"No data found for country: {country_name}")
                return

            sizes = self._calculate_medal_totals(country_data)
            colors = ['gold', 'silver', 'brown']
            explode = (0.1, 0, 0)

            plt.figure(figsize=(8, 8))
            plt.pie(sizes, explode=explode, labels=self._LABELS, colors=colors, autopct='%1.1f%%', shadow=True,
                    startangle=140)
            plt.title(f'Medal Composition for {country_name}')
            plt.axis('equal')
            plt.show()
        except KeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
