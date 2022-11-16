import tkinter as tk

class Converter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("My Basic Converter")
        self.window.geometry("400x150")
        self.window.resizable(width=False, height=False)
        self.window.rowconfigure([0, 1, 2, 3], weight=1)
        self.window.columnconfigure([0, 1, 2], weight=1)
    
        self.create_entry()
        self.convert()

    def hp_to_kw(self):
        self.horsepower = self.ent_hp.get()
        self.kilowatt = (float(self.horsepower)) * 0.746
        self.kw_result["text"] = f"{self.kilowatt} kW"

    def kw_to_hp(self):
        self.kilowatt = self.ent_kw.get()
        self.horsepower = (float(self.kilowatt)) / 0.746
        self.horsepower_result["text"] = f"{self.horsepower} hp"

    def create_entry(self):  
        self.hp_entry = tk.Frame(self.window)
        self.ent_hp = tk.Entry(self.hp_entry, width = 10)
        self.lbl_hp = tk.Label(self.hp_entry, text = "hp")
        self.hp_title = tk.Label(self.hp_entry, text = "Horsepower to Kilowatt:")  

        self.kw_entry = tk.Frame(self.window)
        self.ent_kw = tk.Entry(self.kw_entry, width = 10)
        self.lbl_kw = tk.Label(self.kw_entry, text = "kW")
        self.kw_title = tk.Label(self.kw_entry, text = "Kilowatt to Horsepower:")

        self.hp_entry.grid(row=1, column = 0)
        self.ent_hp.grid(row = 1, column = 0)
        self.lbl_hp.grid(row = 1, column = 1)
        self.hp_title.grid(row = 0, column = 0)

        self.kw_entry.grid(row = 3, column =0)
        self.ent_kw.grid(row = 3, column = 0)
        self.lbl_kw.grid(row = 3, column = 1)
        self.kw_title.grid(row = 2, column = 0)

    def convert(self):
        self.horsepower_convert = tk.Button(
            self.window,
            text = "=",
            command = self.hp_to_kw
            )
        self.kw_result = tk.Label(self.window, text="kW")

        self.horsepower_convert.grid(row=1, column=1)
        self.kw_result.grid(row=1, column=2)


        self.kilowatt_convert = tk.Button(
            self.window,
            text = "=",
            command = self.kw_to_hp
            )
        self.horsepower_result = tk.Label(self.window, text="hp")

        self.kilowatt_convert.grid(row=3, column=1)
        self.horsepower_result.grid(row=3, column=2)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    conv = Converter()
    conv.run()



     