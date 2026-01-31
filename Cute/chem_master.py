import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
from math import log10, sqrt

# Main Window
root = tk.Tk()
root.title("🌸 Cute IB Chemistry Master 🌸")
root.geometry("1250x900")
root.configure(bg="#fce4ec")

style = ttk.Style()
style.theme_use("clam")

style.configure("TNotebook", background="#fce4ec")
style.configure("TFrame", background="#ffffff")
style.configure("TButton",
                background="#bbdefb",
                font=("Comic Sans MS", 10, "bold"))
style.configure("TLabel",
                background="#ffffff",
                font=("Comic Sans MS", 11))

tk.Label(root,
    text="🧪 CUTE IB CHEMISTRY MASTER 🧪",
    font=("Comic Sans MS", 26, "bold"),
    bg="#fce4ec",
    fg="#42a5f5").pack(pady=10)

tk.Label(root,
    text="Your pretty chemistry helper 💖",
    font=("Comic Sans MS", 12),
    bg="#fce4ec").pack()

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=20, pady=10)

tabs = {}

tab_names = [
"Moles 🌷",
"Stoichiometry ⚖️",
"Empirical 🔬",
"Gas Laws 💨",
"pH & Acids 🍋",
"Titration 💧",
"Periodic 🌎",
"Graphing 📈",
"Unit Converter 🔁",
"Uncertainty 📏"
]

for name in tab_names:
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=name)
    tabs[name] = frame
tab = tabs["Moles 🌷"]

tk.Label(tab, text="Mole Calculator",
         font=("Comic Sans MS", 16)).pack()

note = """📝 HOW TO USE:
moles = mass ÷ molar mass
Used in nearly ALL IB calculations!
"""
tk.Label(tab, text=note).pack()

mass = tk.Entry(tab)
mm = tk.Entry(tab)

tk.Label(tab,text="Mass (g)").pack(); mass.pack()
tk.Label(tab,text="Molar Mass (g/mol)").pack(); mm.pack()

def calc_moles():
    try:
        n = float(mass.get()) / float(mm.get())
        messagebox.showinfo("Result",
        f"Moles = {round(n,4)} mol\n\nThis can now be used for stoichiometry!")
    except:
        messagebox.showerror("Error","Invalid input")

tk.Button(tab,text="Calculate Moles 💖",
          command=calc_moles).pack(pady=10)
tab = tabs["Stoichiometry ⚖️"]

tk.Label(tab,text="Stoichiometry Solver",
         font=("Comic Sans MS",16)).pack()

note = """📝 HOW TO USE:
Find moles of product from reactant using ratios.
"""
tk.Label(tab,text=note).pack()

n=tk.Entry(tab)
r1=tk.Entry(tab)
r2=tk.Entry(tab)

tk.Label(tab,text="Known moles").pack(); n.pack()
tk.Label(tab,text="Coefficient known").pack(); r1.pack()
tk.Label(tab,text="Coefficient wanted").pack(); r2.pack()

def stoich():
    try:
        res=float(n.get()) * float(r2.get())/float(r1.get())
        messagebox.showinfo("Result",
        f"Required moles = {round(res,4)}")
    except:
        messagebox.showerror("Error","Invalid")

tk.Button(tab,text="Solve ⚖️",command=stoich).pack()
tab = tabs["Empirical 🔬"]

tk.Label(tab,text="Empirical Formula Helper",
         font=("Comic Sans MS",16)).pack()

note="""📝 Divide masses by molar masses,
then find simplest ratio"""
tk.Label(tab,text=note).pack()

a=tk.Entry(tab)
b=tk.Entry(tab)

tk.Label(tab,text="Moles of element 1").pack(); a.pack()
tk.Label(tab,text="Moles of element 2").pack(); b.pack()

def emp():
    try:
        r=float(a.get())/float(b.get())
        messagebox.showinfo("Ratio",
        f"Ratio ≈ {round(r,2)} : 1")
    except:
        messagebox.showerror("Error","Invalid")

tk.Button(tab,text="Find Ratio 🔬",command=emp).pack()
tab = tabs["Gas Laws 💨"]

tk.Label(tab,text="Ideal Gas Law PV = nRT",
         font=("Comic Sans MS",16)).pack()

note="📝 Find pressure from n, V, T"
tk.Label(tab,text=note).pack()

n=tk.Entry(tab)
v=tk.Entry(tab)
t=tk.Entry(tab)

for text,e in [("n (mol)",n),("V (L)",v),("T (K)",t)]:
    tk.Label(tab,text=text).pack(); e.pack()

R=0.0821

def gas():
    try:
        p=float(n.get())*R*float(t.get())/float(v.get())
        messagebox.showinfo("Pressure",
        f"P = {round(p,3)} atm")
    except:
        messagebox.showerror("Error","Invalid")

tk.Button(tab,text="Calculate 💨",command=gas).pack()
tab = tabs["pH & Acids 🍋"]

tk.Label(tab,text="pH Calculator",
         font=("Comic Sans MS",16)).pack()

note="📝 pH = -log[H+]"
tk.Label(tab,text=note).pack()

h=tk.Entry(tab); h.pack()

def ph():
    try:
        val=-log10(float(h.get()))
        messagebox.showinfo("pH",
        f"pH = {round(val,3)}")
    except:
        messagebox.showerror("Error","Invalid")

tk.Button(tab,text="Find pH 🍋",command=ph).pack()
tab = tabs["Titration 💧"]

tk.Label(tab,text="Titration Helper",
         font=("Comic Sans MS",16)).pack()

note="📝 C1V1 = C2V2"
tk.Label(tab,text=note).pack()

c1=tk.Entry(tab)
v1=tk.Entry(tab)
v2=tk.Entry(tab)

tk.Label(tab,text="C1").pack(); c1.pack()
tk.Label(tab,text="V1").pack(); v1.pack()
tk.Label(tab,text="V2").pack(); v2.pack()

def tit():
    try:
        c2=float(c1.get())*float(v1.get())/float(v2.get())
        messagebox.showinfo("Result",
        f"Unknown concentration = {round(c2,4)} M")
    except:
        messagebox.showerror("Error","Invalid")

tk.Button(tab,text="Solve 💧",command=tit).pack()
tab = tabs["Periodic 🌎"]

tk.Label(tab,text="Periodic Table Lookup",
         font=("Comic Sans MS",16)).pack()

note="📝 Find molar masses!"
tk.Label(tab,text=note).pack()

data={
"H":1.01,"He":4.00,"Li":6.94,"C":12.01,
"N":14.01,"O":16.00,"Na":22.99,
"Cl":35.45,"K":39.10,"Ca":40.08
}

e=tk.Entry(tab); e.pack()

def find():
    res=data.get(e.get(),"Not in mini database")
    messagebox.showinfo("Info",res)

tk.Button(tab,text="Search 🌎",command=find).pack()
tab = tabs["Graphing 📈"]

tk.Label(tab,text="Simple Data Plotter",
         font=("Comic Sans MS",16)).pack()

note="📝 Visualise experimental data!"
tk.Label(tab,text=note).pack()

def plot():
    x=np.linspace(0,10,20)
    y=x**2
    plt.figure()
    plt.plot(x,y)
    plt.title("Cute Graph 📈")
    plt.show()

tk.Button(tab,text="Show Example Graph 📈",
          command=plot).pack()
tab = tabs["Unit Converter 🔁"]

tk.Label(tab,text="mL to L Converter",
         font=("Comic Sans MS",16)).pack()

note="📝 Basic but SUPER important in IB!"
tk.Label(tab,text=note).pack()

ml=tk.Entry(tab); ml.pack()

def convert():
    try:
        L=float(ml.get())/1000
        messagebox.showinfo("Result",f"{L} L")
    except:
        messagebox.showerror("Error","Invalid")

tk.Button(tab,text="Convert 🔁",command=convert).pack()
tab = tabs["Uncertainty 📏"]

tk.Label(tab,text="Combine Uncertainties",
         font=("Comic Sans MS",16)).pack()

a=tk.Entry(tab); b=tk.Entry(tab)
a.pack(); b.pack()

def unc():
    try:
        r=sqrt(float(a.get())**2+float(b.get())**2)
        messagebox.showinfo("Result",f"Combined = {round(r,4)}")
    except:
        messagebox.showerror("Error","Invalid")

tk.Button(tab,text="Calculate 📏",command=unc).pack()
root.mainloop()
