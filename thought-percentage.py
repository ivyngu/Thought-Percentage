import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button

def draw_pie():
    pie_ax.clear()

    patches, texts, pcts = pie_ax.pie(
        thoughts.values(), labels=thoughts.keys(), autopct='%.1f%%',
        wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
        textprops={'size': 'x-large'})

    plt.setp(pcts, color='white', fontweight='bold')
    pie_ax.set_title('My Thoughts', fontsize=18)

    fig.canvas.draw_idle()

def on_textbox_update(inp):
    global text_input
    text_input = inp
    fig.canvas.draw_idle()

def next_thought(_):
    if text_input not in thoughts:
        thoughts[text_input] = 0
    thoughts[text_input] += 1
    draw_pie()

def clear_chart(_):
    global thoughts
    pie_ax.clear()
    thoughts = {}
    draw_pie()

# Initial set up of pie chart
thoughts = {}
fig, pie_ax = plt.subplots(figsize=(7, 7))
draw_pie()

# Textbox
axbox = fig.add_axes([0.1, 0.005, 0.4, 0.075])
text_box = TextBox(axbox, "", textalignment="center")
text_box.on_text_change(on_textbox_update)

# Button for adding thought
axnext = fig.add_axes([0.5, 0.005, 0.2, 0.075])
bnnext = Button(axnext, 'Add Thought')
bnnext.on_clicked(next_thought)

# Button for clearing grid
axclear = fig.add_axes([0.7, 0.005, 0.2, 0.075])
bnclear = Button(axclear, 'Clear Chart')
bnclear.on_clicked(clear_chart)

plt.show()
