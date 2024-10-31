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

git clone https://github.com/yourusername/bitcoin-forecasting-competition.git

- Install the required packages:

pip install -r requirements.txt

## Usage
## Generating Competition Source Files
Use two-weeks.py to fetch Bitcoin prices and generate source files:

python two-weeks.py -d "2024-10-30" -t "10:00:00"

it will make last two weeks prices as first week 

## Making Test Competition Submissions
Use algorithms.py to generate test competition submissions. This script contains implementations of various machine learning algorithms.

#Calculating Results and Generating Leaderboard
Use bitcoin_competition.py to process submissions and calculate the leaderboard:

python bitcoin_competition.py submissions submission.json leaderboard.json

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change. If you have any specific details or sections you'd like to add, let me know.
