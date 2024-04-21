import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_curve, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv("transaction_data.csv") # swap it out with database for actual implementation
data["amount"] = data["amount"].str.replace("$", "").astype(float)

# Create LabelEncoder objects for each categorical column
le_merchant_id = LabelEncoder()
le_sector = LabelEncoder()

# Encode the categorical columns
data["merchant id"] = le_merchant_id.fit_transform(data["merchant id"])
data["sector in company"] = le_sector.fit_transform(data["sector in company"])

X = data[["Transaction id", "amount", "merchant id", "sector in company", "day in month"]]

# Split data
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Define and train Isolation Forest model
model = IsolationForest(n_estimators=200, max_samples='auto', contamination=0.03, random_state=42)
model.fit(X_train)

# Predict outliers on testing data
y_predicted = model.predict(X_test)
anomaly_scores = model.decision_function(X_test)

# Analyze results: y_predicted will contain -1 for anomalies and 1 for normal transactions
# anomaly_scores can be used to further analyze potential fraud based on score








#new data


new_transaction = pd.read_csv("new_transaction_data.csv")
new_transaction["amount"] = new_transaction["amount"].str.replace("$", "").astype(float)

# Create LabelEncoder objects for each categorical column
le_merchant_id = LabelEncoder()
le_sector = LabelEncoder()

# Encode the categorical columns
new_transaction["merchant id"] = le_merchant_id.fit_transform(new_transaction["merchant id"])
new_transaction["sector in company"] = le_sector.fit_transform(new_transaction["sector in company"])

new_transaction_encoded = new_transaction[["Transaction id", "amount", "merchant id", "sector in company", "day in month"]]

new_prediction = model.predict(new_transaction_encoded)
new_score = model.decision_function(new_transaction_encoded)
print(new_score)




