import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import glob
import argparse
import json

# Step 1: Load the actual Bitcoin prices
actual_prices = pd.read_csv('actual_prices.csv')
actual_prices.set_index('Datetime', inplace=True)

# Step 2: Function to calculate RMSE
def calculate_rmse(actual, predicted):
    return np.sqrt(mean_squared_error(actual, predicted))

# Step 3: Process submissions
def process_submissions(submission_folder, submission_json):
    results = []
    
    # Load submission details from JSON
    with open(submission_json, 'r') as f:
        submissions = json.load(f)
    
    submission_count = {}
    
    for submission in submissions:
        file_path = os.path.join(submission_folder, submission['submission_file_name'])
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        
        user_predictions = pd.read_csv(file_path)
        user_predictions.set_index('Datetime', inplace=True)
        
        # Ensure the dates match
        if not user_predictions.index.equals(actual_prices.index):
            print(f"Date mismatch in file: {file_path}")
            continue
        
        rmse = calculate_rmse(actual_prices['Close'], user_predictions['Close'])
        user_name = f"{submission['name']} {submission['surname']}"
        student_id = submission['student_id']
        
        # Track submission count
        if student_id not in submission_count:
            submission_count[student_id] = 0
        submission_count[student_id] += 1
        
        results.append((user_name, student_id, submission_count[student_id], os.path.basename(file_path), rmse))
    
    return results

# Step 4: Generate leaderboard and save to JSON
def generate_leaderboard(results, output_file):
    leaderboard = sorted(results, key=lambda x: x[4])
    print("Leaderboard:")
    leaderboard_data = []
    for rank, (user_name, student_id, submission_number, filename, rmse) in enumerate(leaderboard, start=1):
        print(f"{rank}. {user_name} ({student_id}) - Submission {submission_number} - {filename} - RMSE: {rmse:.4f}")
        leaderboard_data.append({
            "rank": rank,
            "user_name": user_name,
            "student_id": student_id,
            "submission_number": submission_number,
            "filename": filename,
            "rmse": rmse
        })
    
    # Save leaderboard to JSON file
    with open(output_file, 'w') as f:
        json.dump(leaderboard_data, f, indent=4)

# Main function to run the competition
def run_competition(submission_folder, submission_json, output_file):
    results = process_submissions(submission_folder, submission_json)
    generate_leaderboard(results, output_file)

# Argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process Bitcoin price submissions.')
    parser.add_argument('submission_folder', type=str, help='Path to the folder containing submission files')
    parser.add_argument('submission_json', type=str, help='Path to the JSON file containing submission details')
    parser.add_argument('output_file', type=str, help='Path to the output JSON file for the leaderboard')
    args = parser.parse_args()
    
    run_competition(args.submission_folder, args.submission_json, args.output_file)
