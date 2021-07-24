import tkinter as tk
from tkinter import ttk

"""
@purpose: Runs the GUI of the program, leading to the main page.
"""

"""
This class creates creates a GUI window and displays the home page.
"""
class mainPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = tk.Frame(self)
        self.geometry("800x600")
        self.title("Data Plot")
        self.home()

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
                print("Changed button to normal state\n")


        label_provTerr = tk.Label(self, text="Select the province/territory to view data from using the list below",
                                  font=("Calibri", 11, "bold"))
        label_provTerr.place(relx=0.5, rely=0.15, anchor="center")

        province_Territory = tk.StringVar()
        provTerrList = ["Alberta", "British Columbia", "Manitoba", "New Brunswick",
                        "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut",
                        "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon"]

        dropdown_provTerr = ttk.Combobox(self, textvariable=province_Territory, values=provTerrList, state="readonly", width=27)
        dropdown_provTerr.place(relx=0.5, rely=0.2, anchor="center")

        # need to find a good font
        generateBtn = tk.Button(self, text="Generate plots", height=1, bg="sky blue", padx=5, relief="flat",
                                state=tk.DISABLED, font="Calibri", command=lambda: self.makePlots())
        generateBtn.place(relx=0.5, rely=0.27, anchor="center")

        dropdown_provTerr.bind("<<ComboboxSelected>>", genBtnState)


    def makePlots(self):
        print("Clicked generate button!\n")
        self._frame.destroy()

        for i in self.winfo_children():
            i.destroy()

        self._frame = plotPage(self)
        print("Created plot page frame\n")


"""
This class creates the page of plots.
"""
class plotPage(tk.Frame):
    def __init__(self, parent):
        self._frame = tk.Frame.__init__(self, parent)

        backBtn = tk.Button(self._frame, text="Back", height=1, bg="sky blue", padx=5, relief="flat", font="Calibri",
                            command=lambda: self.back(parent=parent))
        backBtn.grid(row=1, column=2)

        self.plotButtons()

    """
    This method creates the layout of the buttons for the Plots Page
    """
    def plotButtons(self):

        totalCasesBtn = tk.Button(self._frame, text="Total Cases", height=1, bg="sky blue", padx=5, relief="flat",
                                  font="Calibri", command=self.getTotalCases)
        totalCasesBtn.grid(row=3, column=1)

        confirmedCasesBtn = tk.Button(self._frame, text="Confirmed Cases", height=1, bg="sky blue", padx=5, relief="flat",
                                      font="Calibri")
        confirmedCasesBtn.grid(row=3, column=2)

        newCasesBtn = tk.Button(self._frame, text="New Cases", height=1, bg="sky blue", padx=5, relief="flat",
                                font="Calibri")
        newCasesBtn.grid(row=3, column=3)

        ActiveCasesBtn = tk.Button(self._frame, text="Active Cases", height=1, bg="sky blue", padx=5, relief="flat",
                                   font="Calibri")
        ActiveCasesBtn.grid(row=3, column=4)

        testedBtn = tk.Button(self._frame, text="Tested People Count", height=1, bg="sky blue", padx=5, relief="flat",
                              font="Calibri")
        testedBtn.grid(row=3, column=5)

        recoveredCasesBtn = tk.Button(self._frame, text="Recovered Cases", height=1, bg="sky blue", padx=5, relief="flat",
                                      font="Calibri")
        recoveredCasesBtn.grid(row=3, column=6)

        deathsBtn = tk.Button(self._frame, text="Death Count", height=1, bg="sky blue", padx=5, relief="flat",
                              font="Calibri")
        deathsBtn.grid(row=3, column=7)


    def back(self, parent):
        print("Clicked the back button")

    def getTotalCases(self):
        print("Clicked for Total Cases Plot")


# # This is the start of creating the Tkinter GUI
#
# window = tk.Tk()
# window.geometry("800x600")
# window.title("Data Plot")
#
# # This section sets a dropdown list for user input and its relevant labels, buttons, etc
#
# label_provTerr = tk.Label(window, text="Select the province/territory to view data from using the list below", font=("Calibri", 11, "bold"))
# label_provTerr.place(relx=0.5, rely=0.15, anchor="center")
#
# province_Territory = tk.StringVar()
# provTerrList = ["Alberta", "British Columbia", "Manitoba", "New Brunswick",
#              "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut",
#              "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon"]
#
# dropdown_provTerr = ttk.Combobox(window, textvariable=province_Territory, values=provTerrList, state="readonly")
# dropdown_provTerr.place(relx=0.5, rely=0.2, anchor="center")
#
# # need to find a good font
# generateBtn = tk.Button(window, text="Generate plots", height=1, bg="sky blue", padx=5, relief="flat",
#                         state=tk.DISABLED, font="Calibri", command=makePlots)
# generateBtn.place(relx=0.5, rely=0.27, anchor="center")
#
# dropdown_provTerr.bind("<<ComboboxSelected>>", genBtnState)

if __name__ == "__main__":
    window = mainPage()
    window.mainloop()