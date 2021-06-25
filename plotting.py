
"""
Created on Jun 12, 2021

@purpose: Create plots of selected COVID-19 Data
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import time #remove later

startTime = time.time() #remove later

# turn this into a dropdown list in GUI later
userInput = input("Enter the Canadian province's name to look at (in lowercase letters): ")
provinces_lowercase = np.array(["alberta", "british columbia", "manitoba", "new brunswick", 
                       "newfoundland and labrador", "northwest territories", "nova scotia", 
                       "nunavut", "ontario", "prince edward island", "quebec", 
                       "saskatchewan", "yukon"])

provinces = np.array(["Alberta", "British Columbia", "Manitoba", "New Brunswick", 
             "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut", 
             "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon"])

timeBeforeLoop = time.time() - startTime #remove later
print("Time before loop: " + str(timeBeforeLoop) + "\n") #remove later

selected_index = 0
validProvince = False

# This loop finds a valid index from the user input; if invalid, prompts user input again
while(not validProvince):
    for i in range(0, provinces.size):
        
        if (provinces_lowercase[i] == userInput):
            selected_index = i
            validProvince = True
            print("Valid province/territory entered.\n") #remove later
    
    if (validProvince == False):
        print("You have entered an invalid Canadian province/territory. Please try again.\n")
        userInput = input("Please enter a valid Canadian province/territory name: ")

print("Reading dataset...\n")
data = pd.read_excel("covid19-dataset-Excel.xlsx")


# Getting all relevant info for the plots
relevant_df = data[["prname", "date"]]
pd.to_datetime(relevant_df["date"])
relevant_df.rename(columns = {"date": "Date"}) #change prname later; something is wrong with the renaming, even for date

df_totalCases = relevant_df.assign(Total_Cases = data["numtotal"]) #total cases includes possible cases
df_confirmedCases = relevant_df.assign(Confirmed_Cases = data["numconf"])

df_newCases = relevant_df.assign(New_Cases = data["numtoday"])
df_activeCases = relevant_df.assign(Active_Cases = data["numactive"])

df_tested = relevant_df.assign(Tested = data["numtested"])
df_recovered = relevant_df.assign(Recovered_Cases = data["numrecover"])
df_deaths = relevant_df.assign(Deaths = data["numdeaths"])


# Getting info for the selected province/territory
df_selected_total = df_totalCases[df_totalCases["prname"] == provinces[selected_index]].reset_index()
df_selected_confirmed = df_confirmedCases[df_confirmedCases["prname"] == provinces[selected_index]].reset_index()

df_selected_newcases = df_newCases[df_newCases["prname"] == provinces[selected_index]].reset_index()
df_selected_active = df_activeCases[df_activeCases["prname"] == provinces[selected_index]].reset_index()

df_selected_tested = df_tested[df_activeCases["prname"] == provinces[selected_index]].reset_index()
df_selected_recovered = df_recovered[df_recovered["prname"] == provinces[selected_index]].reset_index()
df_selected_deaths = df_deaths[df_deaths["prname"] == provinces[selected_index]].reset_index()

# print(df_selected_total.tail()) #remove later
# print(df_selected_confirmed.head()) #remove later
# print(df_selected_newcases.head()) #remove later
# print(df_selected_active.head()) #remove later
# print(df_selected_tested.head()) #remove later
# print(df_selected_recovered.head()) #remove later
# print(df_selected_deaths.head()) #remove later

print("Creating plots...\n")


# Plot 1: Total number of cases
startDate = df_selected_total["date"][0]
endDate = df_selected_total["date"][df_selected_total.shape[0] - 1]

x = df_selected_total["date"].dt.date
y = df_selected_total["Total_Cases"]

fig1 = plt.figure(figsize=(12, 10))
ax1 = fig1.add_subplot()

ax1.plot(x, y)
ax1.set_title("Total Number of Cases in " + provinces[selected_index])

ax1.set_xlabel("Date", labelpad=15)
ax1.set_ylabel("Number of Cases", labelpad=15)

monthInterval = mdates.MonthLocator(interval=1)
ax1.xaxis.set_major_locator(monthInterval)

plt.xticks(rotation = 45) 
plt.show()

timeOfProgram = time.time() - startTime #remove later
print("\nTime of Program: " + str(timeOfProgram) + "\n") #remove later
