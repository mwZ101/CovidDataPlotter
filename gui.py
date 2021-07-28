import tkinter as tk
from tkinter import ttk
import plotting

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from matplotlib.widgets import Cursor

"""
@purpose: Runs the GUI of the program, which contains the main home page and a page of plots.
"""

"""
This class creates creates a GUI window and displays the home page.
"""
class mainPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.__frame = tk.Frame(self)

        self.geometry("1050x750")
        self.title("Data Plot")

        self.home()
        self.tk.call("source", "azure-dark.tcl")

        self.__style = ttk.Style()
        self.__style.theme_use("azure-dark")
        self.__userInput = ""

    """
    This method creates the layout for the home page, which includes the dropdown list
    for user input and plot generation button.
    """
    def home(self):

        """
        This function is for changing the state of the generate button from disabled to normal,
        after the user selects an option from the dropdown list.
        """
        def genBtnState(event):
            if (dropdown_provTerr.get() != ""):
                generateBtn["state"] = tk.NORMAL
                generateBtn["background"] = "#007fff" #change to the theme's blue


        label_provTerr = tk.Label(self, text="Select the province/territory to view data from using the list below",
                                  font=("Calibri", 12, "bold"))
        label_provTerr.place(relx=0.5, rely=0.13, anchor="center")

        province_Territory = tk.StringVar()
        provTerrList = ["Alberta", "British Columbia", "Manitoba", "New Brunswick",
                        "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut",
                        "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon"]

        dropdown_provTerr = ttk.Combobox(self, textvariable=province_Territory, values=provTerrList, state="readonly", width=27,
                                         font=("Calibri", 12))
        dropdown_provTerr.place(relx=0.5, rely=0.2, anchor="center")

        # #737373 represents the theme's grey
        generateBtn = tk.Button(self, text="Generate plots", background="#737373", activebackground="#737373", disabledforeground="black",
                                height=1, padx=5, relief="flat", state=tk.DISABLED, font=("Calibri", 14), borderwidth=0,
                                command=lambda: self.makePlots())
        generateBtn.place(relx=0.5, rely=0.27, anchor="center")

        dropdown_provTerr.bind("<<ComboboxSelected>>", genBtnState)
        self.__userInput = province_Territory.get()

    """
    This method turns the current home page frame into a page of plots
    """
    def makePlots(self):
        self.__frame.destroy()

        for i in self.winfo_children():
            i.destroy()

        self.__frame = plotPage(self, rootWindow=self, style=self.__style, provTerrString=self.__userInput)


"""
This class creates the page of plots.
"""
class plotPage(tk.Frame):

    """
    parent: this represents the parent window, and is not null
    style: this is the themed style object that was initialized for the parent window, and is not null
    provTerrString: this is the string version of the user selected province/territory
    """
    def __init__(self, parent, rootWindow, style, provTerrString):
        self.__window = rootWindow
        self.__parentFrame = tk.Frame.__init__(self, parent)
        self.__mainFrame = tk.Frame(self.__parentFrame)
        self.__mainFrame.pack(side="top", fill="both", expand=True)

        self.__row1 = tk.Frame(self.__mainFrame)
        self.__row1.pack(side="top", fill="x", expand=False)

        self.__row2 = tk.Frame(self.__mainFrame)
        self.__row2.pack(fill="both", expand=True, pady=3)

        self.__parentStyle = style
        self.__parent = parent

        self.__provTerrName = provTerrString
        self.plotNotebook()

    """
    This method creates the layout for the page, including the back button and a notebook of plots
    """
    def plotNotebook(self):
        backBtn = ttk.Button(self.__row1, text="Back", style="TButton", command=lambda: self.back(parent=self.__parent))
        backBtn.pack(side="left", padx=50, pady=10)

        self.__parentStyle.configure("TButton", font=("Calibri", 11))
        self.__parentStyle.configure("TNotebook.Tab", font=("Calibri", 11))

        self.__book = ttk.Notebook(self.__row2)
        self.__book.pack(padx= 50, pady=5, fill="both", expand=True)
        listOfTabs = []

        totalCasesTab = tk.Frame(self.__book, bg="black")
        totalCasesTab.pack(fill="both", expand=True)
        listOfTabs.append(totalCasesTab)

        confirmedCasesTab = tk.Frame(self.__book, bg="black")
        confirmedCasesTab.pack(fill="both", expand=True)
        listOfTabs.append(confirmedCasesTab)

        newCasesTab = tk.Frame(self.__book, bg="black")
        newCasesTab.pack(fill="both", expand=True)
        listOfTabs.append(newCasesTab)

        activeCasesTab = tk.Frame(self.__book, bg="black")
        activeCasesTab.pack(fill="both", expand=True)
        listOfTabs.append(activeCasesTab)

        numTestedTab = tk.Frame(self.__book, bg="black")
        numTestedTab.pack(fill="both", expand=True)
        listOfTabs.append(numTestedTab)

        recoveredCasesTab = tk.Frame(self.__book, bg="black")
        recoveredCasesTab.pack(fill="both", expand=True)
        listOfTabs.append(recoveredCasesTab)

        numDeathsTab = tk.Frame(self.__book, bg="black")
        numDeathsTab.pack(fill="both", expand=True)
        listOfTabs.append(numDeathsTab)

        self.__book.add(totalCasesTab, text="Total Cases")
        self.__book.add(confirmedCasesTab, text="Confirmed Cases")

        self.__book.add(newCasesTab, text="New Cases")
        self.__book.add(activeCasesTab, text="Active Cases")

        self.__book.add(numTestedTab, text="Tested People Count")
        self.__book.add(recoveredCasesTab, text="Recovered Cases")
        self.__book.add(numDeathsTab, text="Death Count")

        for i in listOfTabs:
            tk.Label(i, bg="black", fg="white", text="Loading Plot...", font=("Calibri, 14")).place(relx=0.5, rely=0.5, anchor="center")

        self.__window.protocol("WM_DELETE_WINDOW", self.closeProtocol)
        self.addPlots(listOfTabs)

    """
    This method allows the user to go back to the home page by destroying all the relevant frames and then
    initiating the home page. 
    
    parent: this argument represents the parent window, and is not null
    """
    def back(self, parent):
        self.__mainFrame.pack_forget()
        self.__mainFrame.destroy()
        parent.home()

    """
    This method handles the protocol when the user clicks the X button to close the window. The relevant frames 
    and the window get destroyed in a 'smoother' manner.
    """
    def closeProtocol(self):
        self.__book.pack_forget()
        self.__window.destroy()

    """
    This method run the plots from the module plotting.py by taking in the user selected province/territory
    name, and then adding those plots into the respective frames in the notebook tabs.
    
    listOfFrames: this argument is a list of all the children tabs/frames in the notebook, and is not null
    """
    def addPlots(self, listOfFrames):
        __listOfFigures = plotting.runPlots(self.__provTerrName)

        for i in range(0, len(listOfFrames)):
            figCanvas = FigureCanvasTkAgg(__listOfFigures[i], listOfFrames[i])
            figCanvas.draw()

            canvasToolbar = NavigationToolbar2Tk(figCanvas, listOfFrames[i])
            canvasToolbar.update()

            figCanvas.get_tk_widget().pack(side="top")

if __name__ == "__main__":
    window = mainPage()
    window.mainloop()