import pandas as pd
import matplotlib.pyplot as plt


def analyze_flight_kilometers_vs_load_factor(file_path):
    """
    This function analyzes the correlation between Flight Kilometers and Load Factor.
    It requires 'Flight Kilometers' and 'Load Factor' columns in the dataset.
    """
    try:
        # Load the dataset into a pandas DataFrame
        df = pd.read_csv(file_path)
        
        # Check if necessary columns exist
        if 'Flight Kilometers' in df.columns and 'Load Factor' in df.columns:
            # Plot the correlation between Flight Kilometers and Load Factor
            plt.figure(figsize=(10, 6))
            plt.scatter(df['Flight Kilometers'], df['Load Factor'])
            plt.title('Correlation Between Flight Kilometers and Load Factor')
            plt.xlabel('Flight Kilometers')
            plt.ylabel('Load Factor (%)')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            
            # Calculate and print the correlation coefficient
            correlation = df['Flight Kilometers'].corr(df['Load Factor'])
            print(f"Correlation between Flight Kilometers and Load Factor: {correlation}")
        else:
            print("Error: 'Flight Kilometers' or 'Load Factor' column not found in the dataset.")
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")




def analyze_total_ton_kilometers(file_path):
    """
    This function analyzes the Total Ton-Kilometers Performance over time.
    It requires 'Available Tonne-Kilometers' and 'Month' columns in the dataset.
    """
    try:
        # Load the dataset
        df = pd.read_csv(file_path)

        # Check if necessary columns exist
        if 'Available Tonne-Kilometers' in df.columns and 'Month' in df.columns:
            # Plot the total ton-kilometers performance over time
            plt.figure(figsize=(10, 6))
            plt.plot(df['Month'], df['Available Tonne-Kilometers'], marker='o')
            plt.title('Total Ton-Kilometers Performance Over Time')
            plt.xlabel('Month')
            plt.ylabel('Available Tonne-Kilometers')
            plt.xticks(rotation=45, ha='right')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        else:
            print("Error: 'Available Tonne-Kilometers' or 'Month' column not found in the dataset.")
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def analyze_freight_months(file_path):
    """
    This function analyzes the months with the highest and lowest Freight Ton Kilometers.
    It requires 'Freight Tonnes' and 'Month' columns in the dataset.
    """
    try:
        # Load the dataset
        df = pd.read_csv(file_path)

        # Check if necessary columns exist
        if 'Freight Tonnes' in df.columns and 'Month' in df.columns:
            # Find the months with the highest and lowest freight ton kilometers
            highest_freight_month = df.loc[df['Freight Tonnes'].idxmax()]
            lowest_freight_month = df.loc[df['Freight Tonnes'].idxmin()]
            
            print(f"Month with Highest Freight Ton Kilometers: {highest_freight_month['Month']}")
            print(f"Month with Lowest Freight Ton Kilometers: {lowest_freight_month['Month']}")
        else:
            print("Error: 'Freight Tonnes' or 'Month' column not found in the dataset.")
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

analyze_flight_kilometers_vs_load_factor('DGCA_DATA.csv')
#analyze_total_ton_kilometers('DGCA_DATA.csv')
#analyze_freight_months('DGCA_DATA.csv')