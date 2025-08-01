#Understanding Polars Data types
import polars as pl
from datetime import date


def generate_all_datatype():
    print("Polars Data Types:")
    for dtype in pl.datatypes.__all__:
        print(dtype)

generate_all_datatype()

#Array Data Structures
# In Polars, arrays are represented as List type columns in DataFrames.

df = pl.DataFrame({
    "numbers": [[1, 2, 3], [4, 5], [6]],
    "names": [["Alice", "Bob"], ["Charlie"], ["Dave", "Eve"]]
})
print(df)
print(df.schema)
#Struct Data Structures
# In Polars, struct columns can hold multiple fields of different types.

df_struct = pl.DataFrame({
    "person": [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
})
print(df_struct)
print(df_struct.schema)
print(df_struct["person"].to_list())

#Series Data Structures
# series is a 1-dimensional homogeneous data structure. By “homogeneous” we mean that all elements inside a series have the same data type.

series1 = pl.Series("numbers", [1, 2, 3, 4, 5])
print(series1)
print(series1.dtype)  # Output: Int64

series2 = pl.Series("names", ["Alice", "Bob", "Charlie"])
print(series2)
print(series2.dtype)  # Output: Utf8

# When creating a series, Polars will infer the data type from the values you provide.
# You can specify a concrete data type to override the inference mechanism:
s1 = pl.Series("ints", [1, 2, 3, 4, 5])
s2 = pl.Series("uints", [1, 2, 3, 4, 5], dtype=pl.UInt64)
print(s1.dtype, s2.dtype)

# A dataframe is a 2-dimensional heterogeneous data structure that contains uniquely named series.
df = pl.DataFrame(
    {
        "name": ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"],
        "birthdate": [
            date(1997, 1, 10),
            date(1985, 2, 15),
            date(1983, 3, 22),
            date(1981, 4, 30),
        ],
        "weight": [57.9, 72.5, 53.6, 83.1],  # (kg)
        "height": [1.56, 1.77, 1.65, 1.75],  # (m)
    }
)

print(df)
print(df.schema)  # Output: {'name': Utf8, 'birthdate': Date, 'weight': Float64, 'height': Float64}
print(df.head(2))
print(df.tail(2))
print(df.describe())

# In Python, you can specify an explicit schema by using a dictionary to map column names to data types.
# You can use the value None if you do not wish to override inference for a given column.

# Example of specifying an explicit schema in Polars:
df_explicit = pl.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [30, 25, 35],
        "height": [1.56, 1.77, 1.65],
    },
    schema={
        "name": pl.Utf8,
        "age": pl.Int32,
        "height": None  # Let Polars infer the type for 'height'
    }
)

print(df_explicit)
print(df_explicit.schema)

# If you only need to override the inference of some columns, the parameter schema_overrides tends to be more convenient because it lets you omit columns for which you do not want to override the inference

df = pl.DataFrame(
    {
        "name": ["Alice", "Ben", "Chloe", "Daniel"],
        "age": [27, 39, 41, 43],
    },
    schema_overrides={"age": pl.UInt8},
)

print(df)




