import tkinter as tk
from tkinter import *
from tkinter.font import *

import select_map
import skill.endurance
import skill.covert
import heal.noheal
import heal.nohpheal
import heal.fullheal

# Main Window
m = tk.Tk()
m.title("Tarkov Botting Script")

m.geometry("300x200")
m.configure(bg="black")

# Map Selection
map_title = Label(m, text='Choose a map to run:', bg="black", fg="#f07a3c", font=Font(size=12))
map_title.pack(pady=1)
maps = ["Shoreline", "Woods", "Customs", "Factory", "Interchange", "Lighthouse", "Reserve", "Streets Of Tarkov"]
map_name = StringVar()
map_name.set("Shoreline")
w = tk.OptionMenu(m, map_name, *maps)
w.config(bg='#f07a3c', highlightthickness=0, highlightcolor="#f07a3c", highlightbackground="#f07a3c")
w.pack()

# Healing Options
heal_title = Label(m, text='Choose a healing option:', bg="black", fg="#f07a3c", font=Font(size=12))
heal_title.pack(pady=1)
Healing = ["Full Heal", "Only Heal breaks and bleeds", "Don't Heal"]
healing_op = StringVar()
healing_op.set("Full Heal")
h = tk.OptionMenu(m, healing_op, *Healing)
h.config(bg='#f07a3c', highlightthickness=0, highlightcolor="#f07a3c", highlightbackground="#f07a3c")
h.pack()


# Skill Options
skill_title = Label(m, text='Choose a skill to level:', bg="black", fg="#f07a3c", font=Font(size=12))
skill_title.pack(pady=1)
Skills = ["Endurance/Strength", "Covert"]
skill_op = StringVar()
skill_op.set("Endurance/Strength")
s = tk.OptionMenu(m, skill_op, *Skills)
s.config(bg='#f07a3c', highlightthickness=0, highlightcolor="#f07a3c", highlightbackground="#f07a3c")
s.pack()


# Helper Functions
def run_skill(skill_sel):
    if skill_sel == "Endurance/Strength":
        skill.endurance.run()
    elif skill_sel == "Covert":
        skill.covert.run()
    else:
        print("Unknown skill selection, please enter a valid skill option number")


def run_healing(heal_sel):
    if heal_sel == "Full Heal":
        heal.fullheal.run()
    elif heal_sel == "Only Heal breaks and bleeds":
        heal.nohpheal.run()
    elif heal_sel == "Don't Heal":
        heal.noheal.run()
    else:
        print("Unknown healing selection, please enter a valid healing option number")


def run_map(map_sel):
    maps_dict = {
        "Shoreline": lambda: select_map.run("shoreline"),
        "Woods": lambda: select_map.run("woods"),
        "Customs": lambda: select_map.run("customs"),
        "Factory": lambda: select_map.run("factory"),
        "Interchange": lambda: select_map.run("interchange"),
        "Lighthouse": lambda: select_map.run("lighthouse"),
        "Reserve": lambda: select_map.run("reserve"),
        "Streets Of Tarkov": lambda: select_map.run("streets"),
    }
    selected_map = maps_dict.get(map_sel)
    if selected_map:
        selected_map()
    else:
        print("Unknown map selection, please enter a valid map selection number")


def start_bot():
    map_sel = map_name.get()
    heal_sel = healing_op.get()
    skill_sel = skill_op.get()

    run_map(map_sel)
    run_healing(heal_sel)
    run_skill(skill_sel)


def stop_bot():
    print('Stopping the bot!')
    return


# Add a start and stop button
start_button = Button(m, text="Start Bot", command=start_bot, bg="#f07a3c", fg="black")
start_button.pack(pady=10)

stop_button = Button(m, text="Stop Bot", command=stop_bot, bg="#f07a3c", fg="black")
stop_button.pack(pady=5)

m.mainloop()
