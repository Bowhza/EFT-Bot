import tkinter as tk
from tkinter import *
from tkinter.font import *
import skill.endurance
import skill.covert
import skill.death
import heal.noheal
import heal.nohpheal
import heal.fullheal
import map.shoreline
import map.customs
import map.factory
import map.interchange
import map.lighthouse
import map.reserve
import map.streets
import map.woods

import base64, PIL, requests
from PIL import ImageTk

# Main Window
m = tk.Tk()
m.title("Tarkov Botting Script")

m.geometry("300x200")
m.configure(bg="black")

# Map Selection
maptitle = Label(m, text='Choose a map to run:', bg="black", fg="#f07a3c", font=Font(size=12))
maptitle.pack(pady=1)
maps = ["Shoreline", "Woods", "Customs", "Factory", "Interchange", "Lighthouse", "Reserve", "Streets Of Tarkov"]
mapname = StringVar()
mapname.set("Shoreline")
w = tk.OptionMenu(m, mapname, *maps)
w.config(bg='#f07a3c', highlightthickness=0, highlightcolor="#f07a3c", highlightbackground="#f07a3c")
w.pack()

# Healing Options
Healtitle = Label(m, text='Choose a healing option:', bg="black", fg="#f07a3c", font=Font(size=12))
Healtitle.pack(pady=1)
Healing = ["Full Heal", "Only Heal breaks and bleeds", "Don't Heal"]
healingop = StringVar()
healingop.set("Full Heal")
h = tk.OptionMenu(m, healingop, *Healing)
h.config(bg='#f07a3c', highlightthickness=0, highlightcolor="#f07a3c", highlightbackground="#f07a3c")
h.pack()

# Skill Options
skilltitle = Label(m, text='Choose a skill to level:', bg="black", fg="#f07a3c", font=Font(size=12))
skilltitle.pack(pady=1)
Skills = ["Endurance/Strength", "Covert", "Death, heavy bleeds required"]
skillop = StringVar()
skillop.set("Endurance/Strength")
s = tk.OptionMenu(m, skillop, *Skills)
s.config(bg='#f07a3c', highlightthickness=0, highlightcolor="#f07a3c", highlightbackground="#f07a3c")
s.pack()

# Helper Functions
def run_skill(skill_sel):
    if skill_sel == "Endurance/Strength":
        skill.endurance.run()
    elif skill_sel == "Covert":
        skill.covert.run()
    elif skill_sel == "Death, heavy bleeds required":
        skill.death.run()
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
        "Shoreline": map.shoreline,
        "Woods": map.woods,
        "Customs": map.customs,
        "Factory": map.factory,
        "Interchange": map.interchange,
        "Lighthouse": map.lighthouse,
        "Reserve": map.reserve,
        "Streets Of Tarkov": map.streets
    }
    selected_map = maps_dict.get(map_sel)
    if selected_map:
        selected_map.run()
    else:
        print("Unknown map selection, please enter a valid map selection number")

# Commands
def startBot():
    map_sel = mapname.get()
    heal_sel = healingop.get()
    skill_sel = skillop.get()

    run_map(map_sel)
    run_healing(heal_sel)
    run_skill(skill_sel)

def stopBot():
    print('Stopping the bot!')
    return

# Add a start and stop button
start_button = Button(m, text="Start Bot", command=startBot, bg="#f07a3c", fg="black")
start_button.pack(pady=10)

stop_button = Button(m, text="Stop Bot", command=stopBot, bg="#f07a3c", fg="black")
stop_button.pack(pady=5)


m.mainloop()
