import yfinance as yf
import pandas as pd
import argparse
from datetime import datetime, timedelta

# Define the ticker symbol for Bitcoin
ticker = "BTC-USD"

def get_prices(end_date, time):    
    # Combine end date and time, then add one day
    
    end_date_time_delta = (datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = (datetime.strptime(end_date, '%Y-%m-%d') - timedelta(days=14)).strftime('%Y-%m-%d')

    print("start_date", start_date)
    print("end_date", end_date)
    print("end_date_time_delta", end_date_time_delta)
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

def save_to_csv(df, end_date, time):
    
    end_date_time_delta = (datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')

    # Calculate the midpoint date
    midpoint_date = (datetime.strptime(end_date_time_delta, '%Y-%m-%d') - timedelta(days=7)).strftime('%Y-%m-%d')
    start_date = (datetime.strptime(midpoint_date, '%Y-%m-%d') - timedelta(days=7) + timedelta(days=1)).strftime('%Y-%m-%d')
    
    
    print("start_date",start_date)
    print("midpoint_date",midpoint_date)
    print("end_date",end_date)
    print("end_date_time_delta",end_date_time_delta)
    
    start_filter = f"{start_date} {time}"
    mid_filter = f"{midpoint_date} {time}"
    end_date_time_delta_filter = f"{end_date_time_delta} {time}"

    print("start_filter",start_filter)
    print("mid_filter",mid_filter)
    print("end_date_time_delta_filter",end_date_time_delta_filter)
    
    # Split the DataFrame into two parts
    window_df = df.loc[start_filter :mid_filter][:-1]
    forecast_actual_df = df.loc[mid_filter:end_date_time_delta_filter]
    
    print(window_df)
    print(forecast_actual_df)

    # Save the DataFrames to CSV files
    window_df.to_csv("window.csv")
    forecast_actual_df.to_csv("forecast_actual.csv")
    
    print("Saved window.csv and forecast_actual.csv!!")

# Argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch Bitcoin prices for a given date range.')
    parser.add_argument('-d', '--date', type=str, required=True, help='Date in YYYY-MM-DD format')
    parser.add_argument('-t', '--time', type=str, required=True, help='Time in HH:MM:SS format')

    args = parser.parse_args()
    
    
    df = get_prices(args.date, args.time)
    
    # Save the DataFrame with 'Close' prices to CSV files
    save_to_csv(df, args.date, args.time)
