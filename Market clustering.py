# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 07:01:30 2024

@author: Sanket Banerjee
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
# Create a mock dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Income': [15, 16, 16, 18, 20, 25, 30, 33, 40, 50],
    'SpendingScore': [80, 78, 77, 72, 60, 50, 35, 30, 20, 10]
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Display the data
print(df)
# Normalize the data (scaling values)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['Income', 'SpendingScore']])

# Check the scaled data
print(scaled_data)
# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

# Display the DataFrame with clusters
print(df)
# Visualize the clusters
plt.figure(figsize=(8, 6))
for cluster in range(3):
    cluster_data = df[df['Cluster'] == cluster]
    plt.scatter(cluster_data['Income'], cluster_data['SpendingScore'], label=f"Cluster {cluster}")

plt.xlabel('Income')
plt.ylabel('Spending Score')
plt.title('Customer Clusters')
plt.legend()
plt.show()
