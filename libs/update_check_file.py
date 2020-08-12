import sys
sys.path.append('../')
import pandas as pd

from family_trace_update import family_trace_update

family_trace_update()

check_file = pd.read_csv('family_time_check_file.csv')
try:
    check_file.drop(columns='yhaplogroup', inplace=True)
except:
    pass
family_trace = pd.read_csv('surnameFamilyTrace.csv')

family_trace = family_trace[(family_trace.beResearching==False) & (family_trace.release) & (family_trace.delete==False)]

new_file = pd.merge(check_file[['id', 'calib_time']], family_trace[['id','title','surname', 'sortNum', 'haplogroup']], on='id', how='right')

new_file.rename(columns={'haplogroup':'yhaplogroup'}, inplace=True)

new_file[new_file.calib_time.isna()]

new_file.to_csv('family_time_check_file.csv', index=False)
print('all update complete.')
