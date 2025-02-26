# to make changes on giving dataset change file_path variable present at line 116

import sys
import pandas as pd
import matplotlib.pyplot as plt


class Flight:
    def analyze_flight_kilometers_vs_load_factor(self, df):
        """
        This function analyzes the correlation between 'Kms (Thousands)(AF)' and 'PAX load %'.
        """
        try:
            # Check if necessary columns exist
            if 'Kms (Thousands)(AF)' in df.columns and 'PAX load %' in df.columns:
                # Plot the correlation between 'Kms (Thousands)(AF)' and 'PAX load %'
                plt.figure(figsize=(10, 6))
                plt.scatter(df['Kms (Thousands)(AF)'], df['PAX load %'])
                plt.title('Correlation Between Kms (Thousands)(AF) and PAX load %')
                plt.xlabel('Kms (Thousands)(AF)')
                plt.ylabel('PAX load %')
                plt.grid(True)
                plt.tight_layout()
                plt.show()
                
                # Calculate and print the correlation coefficient
                correlation = df['Kms (Thousands)(AF)'].corr(df['PAX load %'])
                print(f"Correlation between Kms (Thousands)(AF) and PAX load %: {correlation}")
            else:
                print("Error: 'Kms (Thousands)(AF)' or 'PAX load %' column not found in the dataset.")
        
        except Exception as e:
            print(f"An error occurred: {e}")


    def analyze_total_ton_kilometers(self, df):
        """
        This function analyzes the Total Ton-Kilometers Performance over time.
        It requires 'Avail TONNE KMS (Millions)' and 'Month' columns in the dataset.
        """
        try:
            # Check if necessary columns exist
            if 'Avail TONNE KMS (Millions)' in df.columns and 'Month' in df.columns:
                # Plot the total ton-kilometers performance over time
                plt.figure(figsize=(10, 6))
                plt.plot(df['Month'], df['Avail TONNE KMS (Millions)'], marker='o')
                plt.title('Total Ton-Kilometers Performance Over Time')
                plt.xlabel('Month')
                plt.ylabel('Avail TONNE KMS (Millions)')
                plt.xticks(rotation=45, ha='right')
                plt.grid(True)
                plt.tight_layout()
                plt.show()
            else:
                print("Error: 'Avail TONNE KMS (Millions)' or 'Month' column not found in the dataset.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

    def analyze_freight_months(self, df):
        """
        This function analyzes the months with the highest and lowest 'Freight TON KM Performed'.
        It requires 'Month' and 'Freight TON KM Performed' columns in the dataset.
        """
        try:
            # Check if necessary columns exist
            if 'Freight TON KM Performed' in df.columns and 'Month' in df.columns:
                # Find the months with the highest and lowest 'Freight TON KM Performed'
                highest_freight_month = df.loc[df['Freight TON KM Performed'].idxmax()]
                lowest_freight_month = df.loc[df['Freight TON KM Performed'].idxmin()]
                
                print(f"Month with Highest Freight Ton Kilometers: {highest_freight_month['Month']}")
                print(f"Month with Lowest Freight Ton Kilometers: {lowest_freight_month['Month']}")
            else:
                print("Error: 'Freight TON KM Performed' or 'Month' column not found in the dataset.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

class Menu:
    def match_choice(self, choice, df, f):
        match choice:
            case 1:
                f.analyze_flight_kilometers_vs_load_factor(df)
            case 2:
                f.analyze_total_ton_kilometers(df)
            case 3:
                f.analyze_freight_months(df)
            case 4:
                self.sys_exit()
            case _:
                self.invalid_choice()
    
    def run_menu(self, df):
        fl = Flight()
        while True:
            choice = int(input('''Enter 
                               1.analyze flight kilometers vs load factor
                               2.analyze total ton kilometers
                               3.analyze freight months
                               4.exit:'''))
            self.match_choice(choice, df, fl)
    
    def invalid_choice(self):
        print("Invalid choice")

    def sys_exit(self):
        sys.exit("End of program")

def start_app(file_path):
    df = pd.read_csv(file_path)
    menu = Menu()
    menu.run_menu(df)


file_path = 'sam_python\\hackaethon_func_10_11_12\\DGCA_DATA.csv'
start_app(file_path)
