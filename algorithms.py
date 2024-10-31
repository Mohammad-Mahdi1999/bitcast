import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
import datetime
import numpy as np

# Load the data
bitcoin_data = pd.read_csv('Bitcoin.csv')
forecast_data = pd.read_csv('forecast_actual.csv')


# Function to create forecasted dataset
def create_forecasted_dataset(df, forecast_size=7*24, forecast_horizon=7*24):
    X, y = [], []
    
    for i in range(len(df) - forecast_size - forecast_horizon + 1):
        X.append(df.iloc[i:(i + forecast_size)].values)
        y.append(df.iloc[(i + forecast_size):(i + forecast_size + forecast_horizon)].values)

    return np.array(X), np.array(y)

# Extract features and labels
X, y = create_forecasted_dataset(bitcoin_data['Close'])
X_forecast = forecast_data['Close'].values

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ensure X_forecast is a 2D array
X_forecast = np.array(X_forecast).reshape(1,-1)
X_train = np.array(X_train)
X_test = np.array(X_test)

print(X_train.shape)
print(X_test.shape)
print(X_forecast.shape)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_forecast = scaler.transform(X_forecast)


# Initialize models
models = {
    # 'LinearRegression': LinearRegression(),
    'RandomForest': RandomForestRegressor(n_estimators=1, random_state=42),
    # 'SVR': SVR(kernel='rbf')
}

# Train and predict
predictions = {}
for name, model in models.items():
    print(f"{name} is fitting ...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_forecast)
    predictions[name] = y_pred

# Save predictions to separate CSV files
for name, pred in predictions.items():
    print(f"{name} is predicting ...")
    print(len(pred))
    print(forecast_data['Datetime'])
    results = pd.DataFrame({'Datetime': forecast_data['Datetime'], 'Close': pred.reshape(-1)})
    results.to_csv(f'./submissions/{name}_predictions.csv', index=False)
    print(f"Predictions saved to {name}_predictions.csv")

print("All predictions saved to separate CSV files.")
