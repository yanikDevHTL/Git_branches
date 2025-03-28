import tkinter as tk
from tkinter import ttk  # Combobox

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Währungsrechner")
        self.root.geometry("400x400")
    
        # Label:
        self.label = tk.Label(self.root, text="Wähle Währung:")  
        self.label.pack(pady=10)

        # Dropdown 1
        self.auswahl = ttk.Combobox(self.root, values=["Euro"])  
        self.auswahl.pack(pady=5)

        # Währung
        self.label_3 = tk.Label(self.root, text="Betrag:")  
        self.label_3.pack(pady=10)
        #entry
        self.entry =tk.Entry(root)
        self.entry.pack(pady=5)
        
        # Währung
        self.label_2 = tk.Label(self.root, text="Wähle in umzurechnete Währung:")  
        self.label_2.pack(pady=10)

        # Dropdown 2
        self.auswahl_2 = ttk.Combobox(self.root, values=["Euro", "US_Dollar", "Pound", "Yen"])  # Korrekt geschlossene Anführungszeichen
        self.auswahl_2.pack(pady=5)

        # Button
        self.button = tk.Button(self.root, text="Umrechnen", command=self.umrechnen)
        self.button.pack(pady=10)

        #Output Label
        self.output_label= tk.Label(self.root, text="")
        self.output_label.pack(pady=10)

    def umrechnen(self):
        #selected_currency = self.auswahl.get()  # Holt erste Währung
        selected_currency_2 = self.auswahl_2.get()  # Holt zweite Währung
        #print(f"Selected currency: {selected_currency}")
        print(f"Converted to: {selected_currency_2}")

        betrag = float(self.entry())
        
        if selected_currency_2 =="Euro":
            ergebnis = betrag
        elif selected_currency_2 =="US_Dollar":
            ergebnis = betrag * 1.1
        elif selected_currency_2 =="Pound":
            ergebnis = betrag * 0.83
        elif selected_currency_2 =="Yen":
            ergebnis = betrag * 162.32
        else:
            self.output_label.config(text="Error")
            return
        self.output_lable.config(text=f"{betrag}Euro = {ergebnis}{selected_currency_2}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Currency(root)
    root.mainloop()