import matplotlib.pyplot as plt
import pandas as pd
from covid import Covid

covid = Covid()
covid.get_data()

indcases = covid.get_status_by_country_name("india")
print(indcases)

s = pd.Series(indcases)

print(s)

s.plot.bar()

plt.show()
