import pandas as pd
import matplotlib.pyplot as plt


def analyze_flight_kilometers_vs_load_factor(file_path):
    """
    This function analyzes the correlation between Flight Kilometers and Load Factor.
    It requires 'Kms (Thousands)(AF)' and 'PAX load %' columns in the dataset.
    """
    try:
        # Load the dataset into a pandas DataFrame
        df = pd.read_csv(file_path)
        
        # Check if necessary columns exist
        if 'Kms (Thousands)(AF)' in df.columns and 'PAX load %' in df.columns:
            # Plot the correlation between Flight Kilometers and Load Factor
            plt.figure(figsize=(10, 6))
            plt.scatter(df['Kms (Thousands)(AF)'], df['PAX load %'])
            plt.title('Correlation Between Flight Kilometers and Load Factor')
            plt.xlabel('Flight Kilometers (Thousands)')
            plt.ylabel('Load Factor (%)')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            
            # Calculate and print the correlation coefficient
            correlation = df['Kms (Thousands)(AF)'].corr(df['PAX load %'])
            print(f"Correlation between Flight Kilometers and Load Factor: {correlation}")
        else:
            print("Error: 'Kms (Thousands)(AF)' or 'PAX load %' column not found in the dataset.")
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")




def analyze_total_ton_kilometers(file_path):
    """
    This function analyzes the Total Ton-Kilometers Performance over time.
    It requires 'Avail TONNE KMS (Millions)' and 'Month' columns in the dataset.
    """
    try:
        # Load the dataset
        df = pd.read_csv(file_path)

        # Check if necessary columns exist
        if 'Avail TONNE KMS (Millions)' in df.columns and 'Month' in df.columns:
            # Plot the total ton-kilometers performance over time
            plt.figure(figsize=(10, 6))
            plt.plot(df['Month'], df['Avail TONNE KMS (Millions)'], marker='o')
            plt.title('Total Ton-Kilometers Performance Over Time')
            plt.xlabel('Month')
            plt.ylabel('Available Tonne-Kilometers (Millions)')
            plt.xticks(rotation=45, ha='right')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        else:
            print("Error: 'Avail TONNE KMS (Millions)' or 'Month' column not found in the dataset.")
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def analyze_freight_months(file_path):
    """
    This function analyzes the months with the highest and lowest Freight Ton Kilometers.
    It requires 'Freight TON KM Performed' and 'Month' columns in the dataset.
    """
    try:
        # Load the dataset
        df = pd.read_csv(file_path)

        # Check if necessary columns exist
        if 'Freight TON KM Performed' in df.columns and 'Month' in df.columns:
            # Find the months with the highest and lowest freight ton kilometers
            highest_freight_month = df.loc[df['Freight TON KM Performed'].idxmax()]
            lowest_freight_month = df.loc[df['Freight TON KM Performed'].idxmin()]
            
            print(f"Month with Highest Freight Ton Kilometers: {highest_freight_month['Month']}")
            print(f"Month with Lowest Freight Ton Kilometers: {lowest_freight_month['Month']}")
        else:
            print("Error: 'Freight TON KM Performed' or 'Month' column not found in the dataset.")
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

#analyze_flight_kilometers_vs_load_factor('haekathon\DGCA_DATA.csv')
#analyze_total_ton_kilometers('haekathon\DGCA_DATA.csv')
analyze_freight_months('haekathon\DGCA_DATA.csv')