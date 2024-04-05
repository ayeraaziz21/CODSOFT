import tkinter as tk
import customtkinter as ctk
import math

class CalculatorApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Simple Calculator")
        self.geometry("400x485")
        self.resizable(False, False)
        self.configure(bg="black")  

        self.entry = ctk.CTkEntry(master=self, width=380, height=60, corner_radius=10,
                                  font=("Arial", 30, "bold"), fg_color="white", bg_color="#4A4A4A")
       
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        button_list = [
            "AC", "C", "%", "/", 
            "7", "8", "9", "*", 
            "4", "5", "6", "-", 
            "1", "2", "3", "+", 
            ".", "0", "√", "="
        ]

        row = 1
        column = 0
        for button in button_list:
            if button in ["/", "*", "-", "+"]:
                button_color = "#FF9500"  
            elif button == "=":
                button_color = "#FF9500"  
            elif button in ["C", "AC", "%"]:
                button_color = "#D4D4D2" 
            else:
                button_color = "#333333"  
            
            if button in ["C", "AC", "%"]:
                text_color = "black"
            else:
                text_color = "white"

            self.button = ctk.CTkButton(
                master=self,
                font=("Arial", 20, "bold"),
                text=button,
                corner_radius=80,
                width=80,
                height=70,
                fg_color=button_color,
                hover_color="#5C5C5C",  
                text_color=text_color,
                command=lambda x=button: self.on_click(x)
            )
            self.button.grid(row=row, column=column, padx=5, pady=5)
            column += 1
            if column > 3:
                column = 0
                row += 1

    def on_click(self, button_text):
        if button_text == "AC":
            self.entry.delete(0, tk.END) 
        elif button_text == "C":
            res = self.entry.get()
            res = res[:-1] 
            self.entry.delete(0, tk.END)
            self.entry.insert(0, res)
        elif button_text == "=":
            try:
                exp = self.entry.get()
                if "√" in exp:
                    exp = exp.replace("√", "math.sqrt(") + ")"
                else:
                    exp = exp.replace("%", "*(1 / 100)")
                result = eval(exp)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, button_text)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
