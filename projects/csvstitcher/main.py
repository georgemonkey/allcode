import pandas as pd
import glob
import os

# adjust the path to your csv folder
path = '/Users/parthamradkar/Downloads/Direct Messages/log'
all_csvs = glob.glob(os.path.join(path, "*.csv"))

df_list = [pd.read_csv(file) for file in all_csvs]
combined = pd.concat(df_list, ignore_index=True)


combined.to_csv("stitched.csv", index=False)
print('FINISHED JOB')