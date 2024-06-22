import pandas as pd
import matplotlib.pyplot as plt


class OlympicAnalyzer:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def explore_data(self):
        info = self.data.info()
        describe = self.data.describe().to_string(float_format="{:.2f}".format)
        return info, describe

    def filter_data(self, column, value):
        try:
            filtered_data = self.data[self.data[column] == value]
            return filtered_data.to_string()
        except KeyError:
            return None

    def sort_data(self, column):
        try:
            sorted_data = self.data.sort_values(by=column)
            return sorted_data.to_string()
        except KeyError:
            return None

    def medals_by_country(self, medal="gold", num_results=None):
        try:
            self.data.columns = self.data.columns.str.strip()

            valid_medals = ['gold', 'silver', 'bronze']
            if medal.lower() not in valid_medals:
                return print("Invalid medal type. Please choose from 'gold', 'silver', or 'bronze'.")

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
            print("Required columns for average medals calculation not found.")
        except TypeError as e:
            print(f"Error: {e}")

    def countries_with_most_participations(self, num_results=None):
        try:
            self.data['Total_participations'] = self.data['NO_SOG_participated'] + self.data['NO_WOG_participated']
            most_participations = self.data[['team', 'Total_participations']].nlargest(num_results,
                                                                                       'Total_participations')
            return most_participations.to_string(index=False)
        except KeyError:
            print("Required columns for most participations calculation not found.")

    def plot_medals_per_country(self):
        try:
            self.data['SOG_total_medals'] = pd.to_numeric(self.data['SOG_total_medals'], errors='coerce')
            self.data[['team', 'SOG_total_medals']].set_index('team').plot(kind='bar', figsize=(12, 6))
            plt.xlabel('Country')
            plt.ylabel('Total Medals')
            plt.title('Total Medals Won by Each Country')
            plt.show()
        except KeyError:
            print("Required columns 'team' or 'SOG_total_medals' not found.")
        except TypeError:
            print("Unable to convert 'SOG_total_medals' to numeric.")

    def plot_medal_comparison(self, num_results=None):
        try:
            self.data['SOG_total_medals'] = pd.to_numeric(self.data['SOG_total_medals'], errors='coerce')
            self.data['WOG_total_medals'] = pd.to_numeric(self.data['WOG_total_medals'], errors='coerce')

            self.data['Total_medals'] = self.data['SOG_total_medals'] + self.data['WOG_total_medals']
            sorted_data = self.data.sort_values(by='Total_medals', ascending=False)

            if num_results:
                sorted_data = sorted_data.head(num_results)

            selected_data = sorted_data[['team', 'SOG_total_medals', 'WOG_total_medals']]
            selected_data = selected_data.set_index('team')

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
        except TypeError:
            print("Unable to convert medal columns to numeric.")
        except Exception as e:
            print(f"Error: {e}")

    def plot_medal_ratio_pie(self):
        try:
            self.data['SOG_gold'] = pd.to_numeric(self.data['SOG_gold'], errors='coerce')
            self.data['SOG_silver'] = pd.to_numeric(self.data['SOG_silver'], errors='coerce')
            self.data['SOG_bronze'] = pd.to_numeric(self.data['SOG_bronze'], errors='coerce')

            total_gold = self.data['SOG_gold'].sum()
            total_silver = self.data['SOG_silver'].sum()
            total_bronze = self.data['SOG_bronze'].sum()

            labels = ['Gold', 'Silver', 'Bronze']
            sizes = [total_gold, total_silver, total_bronze]
            colors = ['gold', 'silver', 'brown']
            explode = (0.1, 0, 0)

            plt.figure(figsize=(8, 8))
            plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True,
                    startangle=140)
            plt.title('Ratio of Gold, Silver, and Bronze Medals')
            plt.axis('equal')
            plt.show()
        except KeyError:
            print("Required columns 'SOG_gold', 'SOG_silver', or 'SOG_bronze' not found.")
        except TypeError:
            print("Unable to convert medal columns to numeric.")
        except Exception as e:
            print(f"Error: {e}")

    def plot_medals_per_country_pie(self, country_name):
        try:
            if 'team' not in self.data.columns:
                raise KeyError("Missing 'team' column in the dataset.")

            self.data['SOG_gold'] = pd.to_numeric(self.data['SOG_gold'], errors='coerce')
            self.data['SOG_silver'] = pd.to_numeric(self.data['SOG_silver'], errors='coerce')
            self.data['SOG_bronze'] = pd.to_numeric(self.data['SOG_bronze'], errors='coerce')

            country_data = self.data[self.data['team'] == country_name]

            if country_data.empty:
                print(f"No data found for country: {country_name}")
                return

            total_gold = country_data['SOG_gold'].sum()
            total_silver = country_data['SOG_silver'].sum()
            total_bronze = country_data['SOG_bronze'].sum()

            labels = ['Gold', 'Silver', 'Bronze']
            sizes = [total_gold, total_silver, total_bronze]
            colors = ['gold', 'silver', 'brown']
            explode = (0.1, 0, 0)

            plt.figure(figsize=(8, 8))
            plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True,
                    startangle=140)
            plt.title(f'Medal Composition for {country_name}')
            plt.axis('equal')
            plt.show()

        except KeyError as e:
            print(f"Error: {e}. Required columns 'team', 'SOG_gold', 'SOG_silver', or 'SOG_bronze' not found.")
        except TypeError:
            print("Unable to convert medal columns to numeric.")
        except Exception as e:
            print(f"Error: {e}")
