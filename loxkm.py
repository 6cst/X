# -*- coding: utf-8 -*-
"""LOxKM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g2UsD3KY7FeY0rBVyKT4hADaFng1k_L4

LINEARxREGRESSIONxOWNDATSET
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import math

data=pd.read_csv('/content/employee_data.csv')

# -------------------------------
# Step 3: Display basic information, nulls and duplicates
# -------------------------------
print("\n--- CSV Data: Head ---")
print(data.head())

print("\n--- CSV Data: Tail ---")
print(data.tail())

print("\n--- CSV Data: Description ---")
print(data.describe(include='all'))

print("\n--- CSV Data: Null counts ---")
print(data.isnull().sum())

# Drop rows with null values
data.dropna(inplace=True)

print("\nAfter dropping null values:")
print(data.isnull().sum())

# Check for duplicates and drop them
duplicate_count = data.duplicated().sum()
print(f"\nNumber of duplicate rows before removal: {duplicate_count}")
data.drop_duplicates(inplace=True)
print(f"Number of duplicate rows after removal: {data.duplicated().sum()}")

le = LabelEncoder()
data['gender'] = le.fit_transform(data['gender'])

target_counts = Counter(data['car_purchased'])
print("\nFrequency of car_purchased values:")
print(target_counts)

# -------------------------------
# Step 5: Data Visualization
# -------------------------------
# Pie chart for the target variable frequencies (using Counter)
plt.figure(figsize=(6,6))
plt.pie(list(target_counts.values()), labels=list(target_counts.keys()), autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Car Purchased Amounts")
plt.show()

# Bar graph: Salary vs. Car Purchased
plt.figure(figsize=(8,6))
sns.barplot(x="salary", y="car_purchased", data=data)
plt.title("Salary vs Car Purchased")
plt.show()

# Scatter plot: Age vs. Car Purchased
plt.figure(figsize=(8,6))
sns.scatterplot(x="age", y="car_purchased", data=data)
plt.title("Age vs Car Purchased")
plt.show()

X = data[['salary']]
y = data['car_purchased']

# Split into training and test sets for simple regression
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X, y, test_size=0.3, random_state=42)

simple_model = LinearRegression()

simple_model.fit(X_train_s, y_train_s)

y_pred_simple = simple_model.predict(X_test_s)

# Performance metrics for Simple Linear Regression
print("\n--- Simple Linear Regression Metrics ---")
print("Intercept:", simple_model.intercept_)
print("Coefficient for salary:", simple_model.coef_[0])
print("R² Score:", r2_score(y_test_s, y_pred_simple))
print("MAE:", mean_absolute_error(y_test_s, y_pred_simple))
print("MSE:", mean_squared_error(y_test_s, y_pred_simple))
print("RMSE:", math.sqrt(mean_squared_error(y_test_s, y_pred_simple)))

# Plot actual vs predicted for Simple Linear Regression
plt.figure(figsize=(8,6))
sns.scatterplot(x=y_test_s, y=y_pred_simple, color='blue', alpha=0.6)
sns.regplot(x=y_test_s, y=y_pred_simple, scatter=False, color='red')
plt.xlabel("Actual Car Purchased")
plt.ylabel("Predicted Car Purchased")
plt.title("Simple Linear Regression: Actual vs Predicted")
plt.show()

# For Multiple Linear Regression, we use all predictors: salary, gender, and age.
X_multiple = data[['salary', 'gender', 'age']]
# Split into training and test sets for multiple regression
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multiple, y, test_size=0.3, random_state=42)

multiple_model = LinearRegression()
multiple_model.fit(X_train_m, y_train_m)
y_pred_multiple = multiple_model.predict(X_test_m)

print("\n--- Multiple Linear Regression Metrics ---")
print("Intercept:", multiple_model.intercept_)
print("Coefficients:", multiple_model.coef_)
print("R² Score:", r2_score(y_test_m, y_pred_multiple))
print("MAE:", mean_absolute_error(y_test_m, y_pred_multiple))
print("MSE:", mean_squared_error(y_test_m, y_pred_multiple))
print("RMSE:", math.sqrt(mean_squared_error(y_test_m, y_pred_multiple)))

# For multiple regression, plotting best fit lines for each predictor individually:
features = ['salary', 'gender', 'age']
y_pred_all = multiple_model.predict(X_multiple)
for feature in features:
    plt.figure(figsize=(8, 5))
    plt.scatter(data[feature], data['car_purchased'], color='grey', alpha=0.6, label='Actual Data')
    plt.scatter(data[feature], y_pred_all, color='red', alpha=0.6, label='Predicted Data')
    # Partial best-fit line
    feature_range = np.linspace(data[feature].min(), data[feature].max(), 100)
    temp_data = {col: np.full(100, data[col].mean()) for col in features}
    temp_data[feature] = feature_range
    X_temp = pd.DataFrame(temp_data)
    y_temp = multiple_model.predict(X_temp)
    plt.plot(feature_range, y_temp, color='blue', linewidth=2, label='Best Fit (Partial)')
    plt.xlabel(feature)
    plt.ylabel('Car Purchased')
    plt.title(f'Car Purchased vs {feature}')
    plt.legend()
    plt.show()

print("\nExperiment: EXPERIMENTx6 BY 229X1A2856")

"""#VERSIONx2"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import math

# -------------------------------
# Step 1: Create the DataFrame manually
# -------------------------------
data_manual = pd.DataFrame({
    'eid': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210,
            201, 212, 213, 214, 215, 216, 217, 218, 219, 220],
    'salary': [48000, 52000, 50000, 58000, 54000, None, 60000, 63000, 57000, 56000,
               48000, 51000, 53000, 59000, None, 61000, 62000, 58000, 60000, 63000],
    'gender': ['Female', 'Male', 'Male', 'Female', 'Female',
               'Male', 'Female', None, 'Male', 'Male',
               'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female'],
    'age': [26, 30, 28, 33, 27, 29, 32, 31, None, 30,
            26, 29, 30, 33, 27, 28, 32, 31, 30, 29],
    'car_purchased': [14000, 16000, 15000, 18000, 17000, 15500, None, 19000, 16500, 16000,
                      14000, 15500, 16500, 17500, 17000, 16000, 18500, 18000, 17500, 19000]
})

print("Manually created DataFrame:")
print(data_manual)

# -------------------------------
# Step 2: Display basic information, nulls and duplicates
# -------------------------------
print("\n--- Manual Data: Head ---")
print(data_manual.head())

print("\n--- Manual Data: Tail ---")
print(data_manual.tail())

print("\n--- Manual Data: Description ---")
print(data_manual.describe(include='all'))

print("\n--- Manual Data: Null counts ---")
print(data_manual.isnull().sum())

# Drop rows with null values
data_manual.dropna(inplace=True)
print("\nAfter dropping null values:")
print(data_manual.isnull().sum())

# Check for duplicates and remove them
duplicate_count_manual = data_manual.duplicated().sum()
print(f"\nNumber of duplicate rows before removal: {duplicate_count_manual}")
data_manual.drop_duplicates(inplace=True)
print(f"Number of duplicate rows after removal: {data_manual.duplicated().sum()}")

# -------------------------------
# Step 3: Encode categorical variables (e.g., 'gender')
# -------------------------------
le_manual = LabelEncoder()
data_manual['gender'] = le_manual.fit_transform(data_manual['gender'])

# -------------------------------
# Step 4: EDA – Count target and Visualizations
# -------------------------------
target_counts_manual = Counter(data_manual['car_purchased'])
print("\nFrequency of car_purchased values in manual DataFrame:")
print(target_counts_manual)

# Pie chart of car_purchased frequencies
plt.figure(figsize=(6,6))
plt.pie(list(target_counts_manual.values()), labels=list(target_counts_manual.keys()), autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Car Purchased Amounts (Manual DataFrame)")
plt.show()

# Bar graph: Salary vs Car Purchased
plt.figure(figsize=(8,6))
sns.barplot(x="salary", y="car_purchased", data=data_manual)
plt.title("Salary vs Car Purchased (Manual DataFrame)")
plt.show()

# Scatter plot: Age vs Car Purchased
plt.figure(figsize=(8,6))
sns.scatterplot(x="age", y="car_purchased", data=data_manual)
plt.title("Age vs Car Purchased (Manual DataFrame)")
plt.show()

# -------------------------------
# Step 5: Data Processing & Model Training
# -------------------------------
# Simple Linear Regression: Use salary as predictor
X_simple_manual = data_manual[['salary']]
y_manual = data_manual['car_purchased']

X_train_s_m, X_test_s_m, y_train_s_m, y_test_s_m = train_test_split(X_simple_manual, y_manual, test_size=0.3, random_state=42)

simple_model_manual = LinearRegression()
simple_model_manual.fit(X_train_s_m, y_train_s_m)
y_pred_simple_manual = simple_model_manual.predict(X_test_s_m)

print("\n--- Simple Linear Regression Metrics (Manual DataFrame) ---")
print("Intercept:", simple_model_manual.intercept_)
print("Coefficient for salary:", simple_model_manual.coef_[0])
print("R² Score:", r2_score(y_test_s_m, y_pred_simple_manual))
print("MAE:", mean_absolute_error(y_test_s_m, y_pred_simple_manual))
print("MSE:", mean_squared_error(y_test_s_m, y_pred_simple_manual))
print("RMSE:", math.sqrt(mean_squared_error(y_test_s_m, y_pred_simple_manual)))

plt.figure(figsize=(8,6))
sns.scatterplot(x=y_test_s_m, y=y_pred_simple_manual, color='blue', alpha=0.6)
sns.regplot(x=y_test_s_m, y=y_pred_simple_manual, scatter=False, color='red')
plt.xlabel("Actual Car Purchased")
plt.ylabel("Predicted Car Purchased")
plt.title("Simple Linear Regression (Manual DataFrame): Actual vs Predicted")
plt.show()

# Multiple Linear Regression: Use salary, gender, and age as predictors
X_multiple_manual = data_manual[['salary', 'gender', 'age']]
X_train_m_m, X_test_m_m, y_train_m_m, y_test_m_m = train_test_split(X_multiple_manual, y_manual, test_size=0.3, random_state=42)

multiple_model_manual = LinearRegression()
multiple_model_manual.fit(X_train_m_m, y_train_m_m)
y_pred_multiple_manual = multiple_model_manual.predict(X_test_m_m)

print("\n--- Multiple Linear Regression Metrics (Manual DataFrame) ---")
print("Intercept:", multiple_model_manual.intercept_)
print("Coefficients:", multiple_model_manual.coef_)
print("R² Score:", r2_score(y_test_m_m, y_pred_multiple_manual))
print("MAE:", mean_absolute_error(y_test_m_m, y_pred_multiple_manual))
print("MSE:", mean_squared_error(y_test_m_m, y_pred_multiple_manual))
print("RMSE:", math.sqrt(mean_squared_error(y_test_m_m, y_pred_multiple_manual)))

# Plotting best-fit lines for each feature for the multiple regression model
features_manual = ['salary', 'gender', 'age']
y_pred_all_manual = multiple_model_manual.predict(X_multiple_manual)
for feature in features_manual:
    plt.figure(figsize=(8,5))
    plt.scatter(data_manual[feature], data_manual['car_purchased'], color='grey', alpha=0.6, label='Actual Data')
    plt.scatter(data_manual[feature], y_pred_all_manual, color='red', alpha=0.6, label='Predicted Data')
    feature_range_manual = np.linspace(data_manual[feature].min(), data_manual[feature].max(), 100)
    temp_data_manual = {col: np.full(100, data_manual[col].mean()) for col in features_manual}
    temp_data_manual[feature] = feature_range_manual
    X_temp_manual = pd.DataFrame(temp_data_manual)
    y_temp_manual = multiple_model_manual.predict(X_temp_manual)
    plt.plot(feature_range_manual, y_temp_manual, color='blue', linewidth=2, label='Best Fit (Partial)')
    plt.xlabel(feature)
    plt.ylabel('Car Purchased')
    plt.title(f'Car Purchased vs {feature} (Manual DataFrame)')
    plt.legend()
    plt.show()

print("\nExperiment: EXPERIMENTx6 BY 229X1A2856")

"""**KNNxIRIS**"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

df=pd.read_csv("/content/iris (3).csv")

# Step 2: Dataset info
print(df.info())
print(df.head())
print(df.describe())
print("Missing values:\n", df.isnull().sum())

# Step 3: Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Step 4: Features and Target
X = df.drop("target", axis=1)
y = df["target"]

# Step 5: Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 6: Split the data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 7: KNN Classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Step 8: Prediction and Evaluation
y_pred = knn.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Step 9: Cross-validation
cv_scores = cross_val_score(knn, X_scaled, y, cv=5)
print("Cross-validation scores:", cv_scores)
print("Mean CV Accuracy:", np.mean(cv_scores))















