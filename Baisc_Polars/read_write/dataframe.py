import polars as pl
import datetime as dt
import os

def read_df():
    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob", "Charlie"],
            "age": [25, 30, 35],
            "joined": [
                dt.datetime(2020, 1, 1),
                dt.datetime(2021, 6, 15),
                dt.datetime(2022, 3, 10),
            ],
            "active": [True, False, True],
        }
    )
    return df
def write_df(df, file_path):
    df.write_csv(file_path)
    return f"DataFrame written to {file_path}"

def main():
    df = read_df()
    curr_dir = os.getcwd()+'/dest_file'
    dest_path = os.path.join(curr_dir, "dataframe.csv")
    result = write_df(df, dest_path)    
if __name__ == "__main__":
    main()
    
