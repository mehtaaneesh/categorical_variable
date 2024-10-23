import numpy as np
import pandas as pd

data = {
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red'],
    'Size': ['S', 'M', 'L', 'S', 'M']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)


def ordinal_encoding(col):
    unique_values = list(set(col))
    mapping = {value: idx + 1 for idx, value in enumerate(unique_values)}
    encoded_col = [mapping[val] for val in col]
    return encoded_col, mapping

df['Color Ordinal'],color_mapping = ordinal_encoding(df['Color'])
df['Size_Ordinal'], size_mapping = ordinal_encoding(df['Size'])

print("\nDataFrame with Ordinal Encoding:")
print(df)
print("\nColor Mapping:", color_mapping)
print("Size Mapping:", size_mapping)
