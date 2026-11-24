import numpy as np
import pandas as pd
# Cricket Match Datapy
data = {
    "Match": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Runs": [45, 67, 23, 89, 100, 56, 78, 34, 90, 65],
    "Balls": [30, 45, 20, 55, 60, 35, 50, 25, 58, 40],
}
# Create DataFrame
df = pd.DataFrame(data)
# NumPy Array 
runs = np.array(df["Runs"])
# Calculations
total_runs = np.sum(runs) 
average_runs = np.mean(runs)
highest_score = np.max(runs)
lowest_score = np.min(runs)
#Count 50+ Score
fifty_plus = np.sum(runs >= 50)
# Highest Performance 
best_match = np.argmax(runs) + 1
# Display Results
print("===== CRICKET PERFORMANCE ANALYZER =====")
print("\nMatch Details:")
print(df)
print("\n===== PERFORMANCE REPORT =====")
print("Total Runs:", total_runs)
print("Average Runs:", average_runs)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("50+ Score:", fifty_plus)
print("Best Performance: Match", best_match)
print("\n===== Sorted Performance =====")
print(df.sort_values(by="Runs", ascending=False))