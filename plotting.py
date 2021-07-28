
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

returns: the function returns a list of the figures with plots 
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


    # Making all the relevant plots by passing the needed info into a function, and then adding into a list of figures

    totalCasesFigure = _createPlot(df_selected_total, "Total_Cases", "Number of Cases",
               "Total Number of COVID-19 Cases in " + provinces[selected_index] + " (Confirmed and Possible Cases)")
    listOfFigures.append(totalCasesFigure)

    confirmedCasesFigure = _createPlot(df_selected_confirmed, "Confirmed_Cases", "Number of Confirmed Cases",
                                  "Total Number of Confirmed COVID-19 Cases in " + provinces[selected_index])
    listOfFigures.append(confirmedCasesFigure)

    newCasesFigure = _createPlot(df_selected_newcases, "New_Cases", "Number of Newly Confirmed Cases",
                                  "Number of Newly Confirmed COVID-19 Cases in " + provinces[selected_index])
    listOfFigures.append(newCasesFigure)

    activeCasesFigure = _createPlot(df_selected_active, "Active_Cases", "Number of Active Cases",
                                  "Number of Currently Active COVID-19 Cases in " + provinces[selected_index])
    listOfFigures.append(activeCasesFigure)

    numTestedFigure = _createPlot(df_selected_tested, "Tested", "Number of Tested Individuals",
                                  "Number of Tested Individuals for COVID-19 in " + provinces[selected_index])
    listOfFigures.append(numTestedFigure)

    recoveredCasesFigure = _createPlot(df_selected_recovered, "Recovered_Cases", "Number of Recovered Cases",
                                  "Number of Recovered COVID-19 Cases in " + provinces[selected_index])
    listOfFigures.append(recoveredCasesFigure)

    numDeathsFigure = _createPlot(df_selected_deaths, "Deaths", "Number of Deaths",
                                  "Number of Deaths from COVID-19 in " + provinces[selected_index])
    listOfFigures.append(numDeathsFigure)

    return listOfFigures

"""
This function makes a figure with a plot as specified. 

df_selected: this is a dataframe that is used for the x and y coordinates, and is not null
dataSelectedColumn: this string is the column's name of the dataframe to be used for the y coordinates

yaxisLabel: this string is for the y-axis label of the plot
plotTitle: this string is the specified plot title

returns: this function returns the created figure with the plot
"""
def _createPlot(df_selected, dataSelectedColumn, yaxisLabel, plotTitle):
    x = df_selected["date"].dt.date
    y = df_selected[dataSelectedColumn]

    fig = Figure(figsize=(10, 9))
    ax = fig.add_subplot()
    fig.subplots_adjust(bottom=0.18, top=0.93)

    ax.plot(x, y)
    ax.set_title(plotTitle)

    ax.set_xlabel("Date", labelpad=15)
    ax.set_ylabel(yaxisLabel, labelpad=15)

    monthInterval = mdates.MonthLocator(interval=1)
    ax.xaxis.set_major_locator(monthInterval)
    ax.tick_params(axis="x", labelrotation=45)

    yticks = mticker.MaxNLocator(15)
    ax.yaxis.set_major_locator(yticks)

    return fig

