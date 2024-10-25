import yfinance as yf
import pandas as pd
import argparse
from datetime import datetime, timedelta

# Define the ticker symbol for Bitcoin
ticker = "BTC-USD"

import yfinance as yf
import pandas as pd
import argparse
from datetime import datetime, timedelta

# Define the ticker symbol for Bitcoin
ticker = "BTC-USD"

def get_prices(start_date, end_date, time):    
    # Combine end date and time, then add one day
    end_date_time_delta = (datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    
    # Fetch the data
    data = yf.download(ticker, start=start_date, end=end_date_time_delta, interval="1h")
    
    # Create a DataFrame with only 'Close' prices and reset the index to get 'Datetime'
    df = data[['Close']].reset_index()
    
    # Format the datetime column
    df['Datetime'] = df['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # Set 'Datetime' as the index
    df.set_index('Datetime', inplace=True) 
    
    # Filter the DataFrame from start date and time to end date and time
    start_filter = f"{start_date} {time}"
    end_filter = f"{end_date} {time}"
    filtered_df = df.loc[start_filter:end_filter][:-1]
    
    print(filtered_df)
    
    return filtered_df

# Argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch Bitcoin prices for a given date range.')
    parser.add_argument('-s', '--start', type=str, required=True, help='Start date in YYYY-MM-DD format')
    parser.add_argument('-e', '--end', type=str, required=True, help='End date in YYYY-MM-DD format')
    parser.add_argument('-t', '--time', type=str, required=True, help='Time in HH:MM:SS format')

    args = parser.parse_args()
    
    df = get_prices(args.start, args.end, args.time)
    
    # Save the DataFrame with 'Close' prices to a CSV file
    df.to_csv("actual_prices.csv")
    print("Saved at actual_prices.csv!!")
