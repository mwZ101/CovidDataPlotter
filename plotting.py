
"""
@purpose: Create plots of selected COVID-19 Data
"""

import numpy as np
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.figure import Figure
import pandas as pd


"""
This function runs the dataset using the inputted province/territory string and makes the necessary plots.

provTerrName: this argument is the string for the province/territory name, and is not null

return: the function returns a list of the figures with plots 
"""
def runPlots(provTerrName):
    provinces = np.array(["Alberta", "British Columbia", "Manitoba", "New Brunswick",
                 "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut",
                 "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon"])

    listOfFigures = []
    selected_index = 0

    for i in range(provinces.size):
        if (provinces[i] == provTerrName):
            selected_index = i
            print("Processing the province/territory COVID data...\n")
            break

    print("Reading dataset...\n")
    data = pd.read_excel("covid19-dataset-Excel.xlsx")


    # Getting all relevant info for the plots

    relevant_df = data[["prname", "date"]]
    pd.to_datetime(relevant_df["date"])
    relevant_df.rename(columns = {"date": "Date"})

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

    """
    Plot 1: Total number of cases
    """
    x1 = df_selected_total["date"].dt.date
    y1 = df_selected_total["Total_Cases"]

    fig1 = Figure(figsize=(10, 9))
    ax1 = fig1.add_subplot()
    fig1.subplots_adjust(bottom=0.18, top=0.93)

    ax1.plot(x1, y1)
    ax1.set_title("Total Number of COVID-19 Cases in " + provinces[selected_index] + " (Confirmed and Possible Cases)")

    ax1.set_xlabel("Date", labelpad=15)
    ax1.set_ylabel("Number of Cases", labelpad=15)

    monthInterval = mdates.MonthLocator(interval=1)
    ax1.xaxis.set_major_locator(monthInterval)
    ax1.tick_params(axis="x", labelrotation=45)

    yticks1 = mticker.MaxNLocator(15)
    ax1.yaxis.set_major_locator(yticks1)

    listOfFigures.append(fig1)


    """
    Plot 2: Number of Confirmed Cases per day
    """
    x2 = df_selected_confirmed["date"].dt.date
    y2 = df_selected_confirmed["Confirmed_Cases"]

    fig2 = Figure(figsize=(10, 9))
    ax2 = fig2.add_subplot()
    fig2.subplots_adjust(bottom=0.18, top=0.93)

    ax2.plot(x2, y2)
    ax2.set_title("Total Number of Confirmed COVID-19 Cases in " + provinces[selected_index])

    ax2.set_xlabel("Date", labelpad=15)
    ax2.set_ylabel("Number of Confirmed Cases", labelpad=15)

    ax2.xaxis.set_major_locator(monthInterval)
    ax2.tick_params(axis="x", labelrotation=45)

    yticks2 = mticker.MaxNLocator(15)
    ax2.yaxis.set_major_locator(yticks2)

    listOfFigures.append(fig2)


    """
    Plot 3: Number of Newly Confirmed Cases
    """
    x3 = df_selected_newcases["date"].dt.date
    y3 = df_selected_newcases["New_Cases"]

    fig3 = Figure(figsize=(10, 9))
    ax3 = fig3.add_subplot()
    fig3.subplots_adjust(bottom=0.18, top=0.93)

    ax3.plot(x3, y3)
    ax3.set_title("Number of Newly Confirmed COVID-19 Cases in " + provinces[selected_index])

    ax3.set_xlabel("Date", labelpad=15)
    ax3.set_ylabel("Number of Confirmed Cases", labelpad=15)

    ax3.xaxis.set_major_locator(monthInterval)
    ax3.tick_params(axis="x", labelrotation=45)

    yticks3 = mticker.MaxNLocator(15)
    ax3.yaxis.set_major_locator(yticks3)

    listOfFigures.append(fig3)


    """
    Plot 4: Number of Currently Active Cases
    """
    x4 = df_selected_active["date"].dt.date
    y4 = df_selected_active["Active_Cases"]

    fig4 = Figure(figsize=(10, 9))
    ax4 = fig4.add_subplot()
    fig4.subplots_adjust(bottom=0.18, top=0.93)

    ax4.plot(x4, y4)
    ax4.set_title("Number of Currently Active COVID-19 Cases in " + provinces[selected_index])

    ax4.set_xlabel("Date", labelpad=15)
    ax4.set_ylabel("Number of Active Cases", labelpad=15)

    ax4.xaxis.set_major_locator(monthInterval)
    ax4.tick_params(axis="x", labelrotation=45)

    yticks4 = mticker.MaxNLocator(15)
    ax4.yaxis.set_major_locator(yticks4)

    listOfFigures.append(fig4)


    """
    Plot 5: Number of Tested Individuals
    """
    x5 = df_selected_tested["date"].dt.date
    y5 = df_selected_tested["Tested"]

    fig5 = Figure(figsize=(10, 9))
    ax5 = fig5.add_subplot()
    fig5.subplots_adjust(bottom=0.18, top=0.93)

    ax5.plot(x5, y5)
    ax5.set_title("Number of Tested Individuals for COVID-19 in " + provinces[selected_index])

    ax5.set_xlabel("Date", labelpad=15)
    ax5.set_ylabel("Number of Tested Individuals", labelpad=15)

    monthInterval5 = mdates.MonthLocator(interval=1)
    ax5.xaxis.set_major_locator(monthInterval5)
    ax5.tick_params(axis="x", labelrotation=45)

    yticks5 = mticker.MaxNLocator(15)
    ax5.yaxis.set_major_locator(yticks5)

    listOfFigures.append(fig5)


    """
    Plot 6: Number of Recovered Cases
    """
    x6 = df_selected_recovered["date"].dt.date
    y6 = df_selected_recovered["Recovered_Cases"]

    fig6 = Figure(figsize=(10, 9))
    ax6 = fig6.add_subplot()
    fig6.subplots_adjust(bottom=0.18, top=0.93)

    ax6.plot(x6, y6)
    ax6.set_title("Number of Recovered COVID-19 Cases in " + provinces[selected_index])

    ax6.set_xlabel("Date", labelpad=15)
    ax6.set_ylabel("Number of Recovered Cases", labelpad=15)

    ax6.xaxis.set_major_locator(monthInterval)
    ax6.tick_params(axis="x", labelrotation=45)

    yticks6 = mticker.MaxNLocator(15)
    ax6.yaxis.set_major_locator(yticks6)

    listOfFigures.append(fig6)


    """
    Plot 7: Number of Deaths
    """
    x7 = df_selected_deaths["date"].dt.date
    y7 = df_selected_deaths["Deaths"]

    fig7 = Figure(figsize=(10, 9))
    ax7 = fig7.add_subplot()
    fig7.subplots_adjust(bottom=0.18, top=0.93)

    ax7.plot(x7, y7)
    ax7.set_title("Number of Deaths from COVID-19 in " + provinces[selected_index])

    ax7.set_xlabel("Date", labelpad=15)
    ax7.set_ylabel("Number of Deaths", labelpad=15)

    ax7.xaxis.set_major_locator(monthInterval)
    ax7.tick_params(axis="x", labelrotation=45)

    yticks7 = mticker.MaxNLocator(15)
    ax7.yaxis.set_major_locator(yticks7)

    listOfFigures.append(fig7)


    return listOfFigures
