from covid import Covid
import pandas as  pd
import time

covid = Covid()

covid.get_data()

cases = covid.get_status_by_country_name("india")

s = pd.Series(cases)

print(s)
