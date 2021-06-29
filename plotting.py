
"""
Created on Jun 12, 2021

@purpose: Create plots of selected COVID-19 Data
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import matplotlib.widgets as widgets
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


print("Creating plots...\n")

startDate = df_selected_total["date"][0]
endDate = df_selected_total["date"][df_selected_total.shape[0] - 1]


"""
Plot 1: Total number of cases
"""
x1 = df_selected_total["date"].dt.date
y1 = df_selected_total["Total_Cases"]

fig1 = plt.figure(figsize=(10, 9))
fig1.canvas.set_window_title('Total Number of Cases Figure')
ax1 = fig1.add_subplot()

ax1.plot(x1, y1)
ax1.set_title("Total Number of COVID-19 Cases in " + provinces[selected_index] + " (Confirmed and Possible Cases)")

ax1.set_xlabel("Date", labelpad=15)
ax1.set_ylabel("Number of Cases", labelpad=15)

monthInterval = mdates.MonthLocator(interval=1)
ax1.xaxis.set_major_locator(monthInterval)
plt.xticks(rotation = 45)

yticks1 = mticker.MaxNLocator(15)
ax1.yaxis.set_major_locator(yticks1)

cursor1 = widgets.Cursor(ax1, horizOn=True, vertOn=True,useblit=True, color='red', linewidth=0.5)
plt.show()


"""
Plot 2: Number of Confirmed Cases per day
"""
x2 = df_selected_confirmed["date"].dt.date
y2 = df_selected_confirmed["Confirmed_Cases"]

fig2 = plt.figure(figsize=(10, 9))
fig2.canvas.set_window_title('Total Confirmed Cases Figure')
ax2 = fig2.add_subplot()

ax2.plot(x2, y2)
ax2.set_title("Total Number of Confirmed COVID-19 Cases in " + provinces[selected_index])

ax2.set_xlabel("Date", labelpad=15)
ax2.set_ylabel("Number of Confirmed Cases", labelpad=15)

ax2.xaxis.set_major_locator(monthInterval)
plt.xticks(rotation = 45)

yticks2 = mticker.MaxNLocator(15)
ax2.yaxis.set_major_locator(yticks2)

cursor2 = widgets.Cursor(ax2, horizOn=True, vertOn=True,useblit=True, color='red', linewidth=0.5)
plt.show()


"""
Plot 3: Number of Newly Confirmed Cases
"""
x3 = df_selected_newcases["date"].dt.date
y3 = df_selected_newcases["New_Cases"]

fig3 = plt.figure(figsize=(10, 9))
fig3.canvas.set_window_title('Newly Confirmed Cases Figure')
ax3 = fig3.add_subplot()

ax3.plot(x3, y3)
ax3.set_title("Number of Newly Confirmed COVID-19 Cases in " + provinces[selected_index])

ax3.set_xlabel("Date", labelpad=15)
ax3.set_ylabel("Number of Confirmed Cases", labelpad=15)

ax3.xaxis.set_major_locator(monthInterval)
plt.xticks(rotation = 45)

yticks3 = mticker.MaxNLocator(15)
ax3.yaxis.set_major_locator(yticks3)

cursor3 = widgets.Cursor(ax3, horizOn=True, vertOn=True,useblit=True, color='red', linewidth=0.5)
plt.show()


"""
Plot 4: Number of Currently Active Cases
"""
x4 = df_selected_active["date"].dt.date
y4 = df_selected_active["Active_Cases"]

fig4 = plt.figure(figsize=(10, 9))
fig4.canvas.set_window_title('Current Active Cases Figure')
ax4 = fig4.add_subplot()

ax4.plot(x4, y4)
ax4.set_title("Number of Currently Active COVID-19 Cases in " + provinces[selected_index])

ax4.set_xlabel("Date", labelpad=15)
ax4.set_ylabel("Number of Active Cases", labelpad=15)

ax4.xaxis.set_major_locator(monthInterval)
plt.xticks(rotation = 45)

yticks4 = mticker.MaxNLocator(15)
ax4.yaxis.set_major_locator(yticks4)

cursor4 = widgets.Cursor(ax4, horizOn=True, vertOn=True,useblit=True, color='red', linewidth=0.5)
plt.show()


"""
Plot 5: Number of Tested Individuals
"""
x5 = df_selected_tested["date"].dt.date
y5 = df_selected_tested["Tested"]

fig5 = plt.figure(figsize=(10, 9))
fig5.canvas.set_window_title('Tested Individuals Count Figure')
ax5 = fig5.add_subplot()

ax5.plot(x5, y5)
ax5.set_title("Number of Tested Individuals for COVID-19 in " + provinces[selected_index])

ax5.set_xlabel("Date", labelpad=15)
ax5.set_ylabel("Number of Tested Individuals", labelpad=15)

monthInterval5 = mdates.MonthLocator(interval=1)
ax5.xaxis.set_major_locator(monthInterval5)
plt.xticks(rotation = 45)

yticks5 = mticker.MaxNLocator(15)
ax5.yaxis.set_major_locator(yticks5)

cursor5 = widgets.Cursor(ax5, horizOn=True, vertOn=True,useblit=True, color='red', linewidth=0.5)
plt.show()


"""
Plot 6: Number of Recovered Cases
"""
x6 = df_selected_recovered["date"].dt.date
y6 = df_selected_recovered["Recovered_Cases"]

fig6 = plt.figure(figsize=(10, 9))
fig6.canvas.set_window_title('Recovered Cases Figure')
ax6 = fig6.add_subplot()

ax6.plot(x6, y6)
ax6.set_title("Number of Recovered COVID-19 Cases in " + provinces[selected_index])

ax6.set_xlabel("Date", labelpad=15)
ax6.set_ylabel("Number of Recovered Cases", labelpad=15)

ax6.xaxis.set_major_locator(monthInterval)
plt.xticks(rotation = 45)

yticks6 = mticker.MaxNLocator(15)
ax6.yaxis.set_major_locator(yticks6)

cursor6 = widgets.Cursor(ax6, horizOn=True, vertOn=True,useblit=True, color='red', linewidth=0.5)
plt.show()


"""
Plot 7: Number of Deaths
"""
x7 = df_selected_deaths["date"].dt.date
y7 = df_selected_deaths["Deaths"]

fig7 = plt.figure(figsize=(10, 9))
fig7.canvas.set_window_title('Deaths Figure')
ax7 = fig7.add_subplot()

ax7.plot(x7, y7)
ax7.set_title("Number of Deaths from COVID-19 in " + provinces[selected_index])

ax7.set_xlabel("Date", labelpad=15)
ax7.set_ylabel("Number of Deaths", labelpad=15)

ax7.xaxis.set_major_locator(monthInterval)
plt.xticks(rotation = 45)

yticks7 = mticker.MaxNLocator(15)
ax7.yaxis.set_major_locator(yticks7)

cursor7 = widgets.Cursor(ax7, horizOn=True, vertOn=True,useblit=True, color='red', linewidth=0.5)
plt.show()


timeOfProgram = time.time() - startTime #remove later
print("Time of Program: " + str(timeOfProgram) + "\n") #remove later
