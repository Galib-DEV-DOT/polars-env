# Way to get polars for python 

### Installing Polars

To install Polars, use pip:

```bash
pip install polars
```

By default, Polars DataFrames support up to approximately 4.3 billion rows. For handling even larger datasets (up to ~18 quintillion rows), enable the big index extension:

```python
import polars as pl

pl.enable_bigidx()
```

This switches DataFrame indexing to 64-bit, greatly increasing the row limit.

Polars supports a wide range of data types, including:

- **Numeric:** Signed/unsigned integers, floating point numbers, decimals
- **Nested:** Lists, structs, arrays
- **Temporal:** Dates, datetimes, times, time deltas
- **Other:** Strings, binary data, booleans, categoricals, enums, objects