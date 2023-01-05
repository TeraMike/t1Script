import pandas as pd
from os import path

csv_file_name = 'last_test_alberto.csv'

data_path = path.join('data', csv_file_name)
cleaned_data_path = path.join('data', f'cleaned-{csv_file_name}')
df = pd.read_csv(data_path)

list_of_column_names = list(df.columns)

df_no_empty_rows = df.dropna(axis=0, how='all', subset=list_of_column_names[1:])  #Drop rows that have all cells empty

row_iterator = df_no_empty_rows.iterrows()
iNextRow, nextRow = next(row_iterator)
# Iterate through rows and merge any two rows that have the same time
for i, row in row_iterator:
    if row['Time'] == nextRow['Time']:
        df_no_empty_rows.at[i, 'ceph-gw3.gridpp.rl.ac.uk'] += nextRow['ceph-gw3.gridpp.rl.ac.uk']
        df_no_empty_rows = df_no_empty_rows[df_no_empty_rows[i] == row['Time']]
# Mika: it doesn't look like the above 7 lines do anything, which is why they're not present in ./performanceChecker.py.

df_no_empty_rows.to_csv(cleaned_data_path, index=False)
