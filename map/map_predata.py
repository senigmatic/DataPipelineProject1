import pandas as pd
import numpy as np
import json

df = pd.read_csv("reduced_data_updated.csv")

selected_columns = ['course_name','certified','final_cc_cname_DI','grade','nevents','ndays_act','nplay_video','nchapters','nforum_posts']
df = df[selected_columns].dropna()

grouped = df.groupby(['certified','final_cc_cname_DI','course_name'])

result = grouped.mean()