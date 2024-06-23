import matplotlib.pyplot as plt
import pandas as pd


class DataVisualization:
    def __init__(self, data):
        self.data = data

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
