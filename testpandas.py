import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['John', 'Jane', 'Mike', 'Alice'],
    'Age': [25, 30, 22, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}
df = pd.DataFrame(data)
print("---------------------------------------------------------------------------------")
# Using loc to select rows by label
print(df.loc[0])  # Accesses the first row by its label
print("---------------------------------------------------------------------------------")
# Using iloc to select rows by integer position
print(df.iloc[0])  # Accesses the first row by its position
print("---------------------------------------------------------------------------------")
# Using loc for inclusive slicing
print(df.loc[0:2])  # Includes rows with labels 0, 1, and 2
print("---------------------------------------------------------------------------------")
# Using iloc for exclusive slicing
print(df.iloc[0:2])  # Includes rows at positions 0 and 1, excludes position 2
