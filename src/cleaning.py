import pandas as pd

def clean_temperature_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df.columns = ['year', 'temperature']
    df.dropna(inplace=True)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    clean_temperature_data(
        '../data/raw/annual_mean_temperature.csv',
        '../data/processed/annual_mean_temperature_clean.csv'
    )
