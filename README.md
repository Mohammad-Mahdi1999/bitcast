بسم الله الرحمن الرحیم

## Bitcoin Forecasting Competition
This repository contains the core components for a Bitcoin forecasting competition using various machine learning algorithms. The project is structured to fetch Bitcoin prices, generate competition source files, create test competition submissions, and calculate results to produce a leaderboard.
Project Structure- two-weeks.py: Script to fetch Bitcoin prices and generate source files for the competition.
- algorithms.py: Implementation of different machine learning algorithms for forecasting.
- bitcoin_competition.py: Script to process submissions and calculate the leaderboard.
- submissions/: Directory containing submission files.
- Bitcoin.csv: Dataset with Bitcoin prices.
- leaderboard.json: Leaderboard data.
## Getting Started
Prerequisites- Python 3.x
- Required packages (listed in requirements.txt)
## Installation
- Clone the repository:
```
git clone https://github.com/yourusername/bitcoin-forecasting-competition.git
```
- Install the required packages:
```
pip install -r requirements.txt
```
## Usage
## Generating Competition Source Files
Use two-weeks.py to fetch Bitcoin prices and generate source files:

```
python two-weeks.py -d YYYY-MM-DD -t HH:MM:SS
```
Replace YYYY-MM-DD with the desired end date and HH:MM:SS with the desired time.

- Example
```
python two-weeks.py -d "2024-10-30" -t "10:00:00"
```
Here's a README file for your project:
Bitcoin Price FetcherThis project fetches Bitcoin prices for a given date range and saves the data into CSV files. It uses the yfinance library to download historical Bitcoin prices of two weeks before the date and processes the data to create two CSV files: window.csv and forecast_actual.csv.

## Making Test Competition Submissions
Use algorithms.py to generate test competition submissions. This script contains implementations of various machine learning algorithms.

# Calculating Results and Generating Leaderboard
Use bitcoin_competition.py to process submissions and calculate the leaderboard. This project processes Bitcoin price submissions, calculates the Root Mean Squared Error (RMSE) for each submission, and generates a leaderboard. It uses the pandas library for data manipulation, numpy for numerical operations, and scikit-learn for calculating RMSE. 

```
python submission_processor.py submission_folder submission_json output_file
```
- Example
```
python bitcoin_competition.py submissions submission.json leaderboard.json
```
## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change. If you have any specific details or sections you'd like to add, let me know.
