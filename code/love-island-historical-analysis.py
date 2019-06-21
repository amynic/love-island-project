
# coding: utf-8

# In[1]:


#Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# Read CSV file
data = pd.read_csv('love-island-historical-dataset.csv')
#print(data)


# In[3]:


shape = data.shape
print(shape)
columns = data.columns.tolist()
print(columns)


# In[5]:


winners = data[data['OUTCOME'].values == 'WINNER']
winners.style


# In[6]:


winners = data[data['OUTCOME'].values == 'RUNNER UP']
winners.style


# In[7]:


winners = data[data['OUTCOME'].values == 'THIRD PLACE']
winners.style


# # Graphs

# In[8]:


#simple histogram
ages = data['Age']
plt.hist(ages, 12, histtype='stepfilled', color='purple')


# In[9]:


# main dataset
daysinvilla = data[['Contestant Name','NUMBER OF DAYS IN VILLA', 'love-island-series', 'First Group to enter villa']]

# Split data by love island series
year2018 = daysinvilla[daysinvilla['love-island-series'].values == 2018].sort_values('NUMBER OF DAYS IN VILLA')
year2017 = daysinvilla[daysinvilla['love-island-series'].values == 2017].sort_values('NUMBER OF DAYS IN VILLA')
year2016 = daysinvilla[daysinvilla['love-island-series'].values == 2016].sort_values('NUMBER OF DAYS IN VILLA')


# Plot all data on sub plot graphs
fig, axs = plt.subplots(2, 2, figsize=(20, 20))
axs[0, 0].barh(year2018['Contestant Name'], year2018['NUMBER OF DAYS IN VILLA'],height= 0.8)
axs[1, 0].barh(year2017['Contestant Name'], year2017['NUMBER OF DAYS IN VILLA'],height= 0.8)
axs[0, 1].barh(year2016['Contestant Name'], year2016['NUMBER OF DAYS IN VILLA'],height= 0.8)


# In[10]:


# simple pie charts
areaofuk = data['Area of UK'].value_counts()
destination = data['From'].value_counts()
print(areaofuk)
plt.pie(areaofuk, labels = areaofuk.index)


# In[11]:


# % chance given historical data
first_to_enter_villa = len(data['First Group to enter villa'])
first_to_enter_villa_yes = len(data[data['First Group to enter villa'].values == 'YES'])
first_to_enter_villa_no = len(data[data['First Group to enter villa'].values == 'NO'])

first_villa = data[(data['First Group to enter villa'].values == 'YES')]
winner = data[data['OUTCOME'].values == 'WINNER']
runnerup = data[data['OUTCOME'].values == 'RUNNER UP']
thirdplace = data[data['OUTCOME'].values == 'THIRD PLACE']
first_villa_and_winner = data[(data['First Group to enter villa'].values == 'YES')&(data['OUTCOME'].values == 'WINNER')]
first_villa_and_runnerup = data[(data['First Group to enter villa'].values == 'YES')&(data['OUTCOME'].values == 'RUNNER UP')]
first_villa_and_thirdplace = data[(data['First Group to enter villa'].values == 'YES')&(data['OUTCOME'].values == 'THIRD PLACE')]



percent_first_villa_and_winner = (len(first_villa_and_winner)/len(winner))*100
print('Percentage of poeple who won and were part of the first group to enter the villa: '+ str(percent_first_villa_and_winner) + '%')

percent_first_villa_inc_runnerup = ((len(first_villa_and_winner)+(len(first_villa_and_runnerup)))/(len(winner)+len(runnerup)))*100
print('Percentage of poeple who won/runner up and were part of the first group to enter the villa: ' + str(percent_first_villa_inc_runnerup) + '%')

percent_first_villa_inc_thirdplace = ((len(first_villa_and_winner)+len(first_villa_and_runnerup)+len(first_villa_and_thirdplace))/(len(winner)+len(runnerup)+len(thirdplace)))*100
print('Percentage of poeple who won/runner up/third place and were part of the first group to enter the villa: ' + str(percent_first_villa_inc_thirdplace) + '%')







# In[19]:


columns = data.columns.tolist()
print(columns)


# In[14]:


#Scatter Plot - day joined villa / no of couple
x1 = data['Day Joined Villa']
y1 = data['Number of Couples']
x2 = data['Age']
y2 = data['Longest couple length']
y3 = data['NUMBER OF DAYS IN VILLA']
y4 = data['Day left Villa']



data_2018 = data[data['love-island-series'] >= 2018]
#print(times_got_pied_days_in_villa_2018)
x5 = data_2018['NUMBER OF DAYS IN VILLA']
y5 = data_2018['Times got Pied']
y6 = data_2018['Number of dates']
y7 = data_2018['Number of Bust Ups']



# In[15]:


plt.figure(figsize=(10,10))
plt.scatter(x1,y1)
plt.xlabel("Day entered the Villa")
plt.ylabel("Number of couples")
plt.title('Day Contestant Joined the Villa by Number of Couples they had - trending down')
plt.show()


# In[16]:


plt.figure(figsize=(10,10))
plt.scatter(x2,y1)
plt.xlabel("Age")
plt.ylabel("Number of couples")
plt.title('A graph to show how age relates to Number of couples across the show')
plt.show()


# In[17]:


plt.figure(figsize=(10,10))
plt.scatter(x2,y4)
plt.xlabel("Age")
plt.ylabel("Day left the Villa")
plt.title('No correlation shown between leaving the villa and age')
plt.show()


# In[18]:


plt.figure(figsize=(10,10))
plt.scatter(x5,y6)
plt.xlabel("Number of days in Villa")
plt.ylabel("Number of times pied")
#plt.title('No correlation shown between leaving the villa and age')
plt.show()

