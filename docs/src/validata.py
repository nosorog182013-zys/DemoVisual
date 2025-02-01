import pandas as pd
"""Import a tool for structuring data."""
file_path = 'dataset/test_data.csv'
data = pd.read_csv(file_path)
"""Load the CSV file to pandas."""
def validate_data(df):
  df['Open time'] = pd.to_datetime(df['Open time'], errors='coerce')
  numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
  for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
  df['Close time'] = pd.to_datetime(df['Close time'], errors='coerce')
  """Function to validate datetime, numeric format for data inspect its contents."""
  df_cleaned = df.dropna(subset=['Open time', 'Close time'] + numeric_columns)
  """Drop rows values in columns that have an invalid format after validation."""
  return df_cleaned

data_validated = validate_data(data)
print(data_validated)
