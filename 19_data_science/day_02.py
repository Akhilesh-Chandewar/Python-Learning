import pandas as pd
import numpy as np

np.random.seed(42)

years = np.random.uniform(0.5, 10, 100).round(2)
salaries = (30000 + (years * 5000) + np.random.normal(0, 5000, 100)).round(2)

pd.DataFrame({
    'YearsExperience': years,
    'Salary': salaries
}).to_csv('day_2_salaries.csv', index=False)

print("Dataset 'day_2_salaries.csv' created with 100 entries.")
