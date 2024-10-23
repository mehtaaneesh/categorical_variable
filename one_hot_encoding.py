import numpy as np
import pandas as pd

data = {
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red'],
    'Size': ['S', 'M', 'L', 'S', 'M']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

def one_hot_encoding(col):
    unique_values = list(set(col))
    one_hot_matrix = np.zeros((len(col), len(unique_values)))
    mapping = {value: idx for idx, value in enumerate(unique_values)}

    for i, val in enumerate(col):
        one_hot_matrix[i, mapping[val]] = 1

    one_hot_df = pd.DataFrame(one_hot_matrix, columns=unique_values)
    return one_hot_df

color_one_hot = one_hot_encoding(df['Color'])
size_one_hot = one_hot_encoding(df['Size'])

print("\nOne-Hot Encoded Data for 'Color':")
print(color_one_hot)
print("\nOne-Hot Encoded Data for 'Size':")
print(size_one_hot)