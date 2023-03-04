import pandas as pd
import matplotlib.pyplot as plt

# create a pandas dataframe with the data
data = {'Year': [2015, 2016, 2017, 2018, 2019, 2020],
        'Internet Users (millions)': [3185, 3424, 3750, 4087, 4388, 4660],
        'YouTube Active Users (millions)': [1000, 1300, 1500, 1800, 2000, 2000],
        'Facebook Active Users (millions)': [1590, 1790, 2070, 2320, 2410, 2740],
        'Instagram Active Users (millions)': [400, 600, 800, 1000, 1100, 1150]}
df = pd.DataFrame(data)

# set the Year column as the index
df.set_index('Year', inplace=True)

# create the bar plot
df.plot(kind='bar', figsize=(10, 6))

# set the title and labels for the plot
plt.title('Number of Internet Users and Social Media Users (2015-2020)')
plt.xlabel('Year')
plt.ylabel('Number of Users (millions)')

# display the plot
plt.show()


