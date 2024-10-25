import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
import datetime

# Load the data
bitcoin_data = pd.read_csv('Bitcoin.csv')
window_data = pd.read_csv('window.csv')

# Prepare the data
def create_features(data, window_size=7):
    features = []
    labels = []
    for i in range(len(data) - window_size):
        features.append(data[i:i + window_size])
        labels.append(data[i + window_size])
    return features, labels

# Extract features and labels
X, y = create_features(bitcoin_data['Close'].values)
X_window, _ = create_features(window_data['Close'].values)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_window = scaler.transform(X_window)

print(X_train.shape)
print(X_test.shape)

# Initialize models
models = {
    'LinearRegression': LinearRegression(),
    'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42),
    'SVR': SVR(kernel='rbf')
}

# Train and predict
predictions = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_window)
    predictions[name] = y_pred

# Save predictions to CSV
results = pd.DataFrame({'Datetime': window_data['Datetime'][7:]})
for name, pred in predictions.items():
    results[name] = pred

results.to_csv('predictions.csv', index=False)

print("Predictions saved to predictions.csv")
