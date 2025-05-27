import pandas as pd
import numpy as np

# Create a synthetic dataset
df = pd.DataFrame({
    'id': range(1, 6),
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'age': np.random.randint(18, 60, size=5),
    'score': np.random.randint(50, 100, size=5)
})

print("DataFrame:")
print(df)

print("\nData Summary:")
print(df.describe())

print("\nGrouping by 'age':")
print(df.groupby('age').size())

print("\nSorting by 'score':")
print(df.sort_values(by='score', ascending=False))

print("\nFiltering rows where 'score' > 75:")
print(df[df['score'] > 75])