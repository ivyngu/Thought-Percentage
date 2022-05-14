import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button

x = []
labels = []
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(x, labels=labels, autopct='%.1f%%')

def create_pie():
    ax.clear()
    patches, texts, pcts = ax.pie(
    x, labels=labels, autopct='%.1f%%',
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'})
    plt.setp(pcts, color='white', fontweight='bold')
    ax.set_title('My Thoughts', fontsize=18)
    plt.tight_layout()
def update_text(expression):
    global ex
    ex = expression
    ax.relim()
    ax.autoscale_view()
    plt.draw()
class Index:
    def next(self, event):
        if ex not in labels:
            labels.append(ex)
            x.append(1)
        else:
            index = labels.index(ex)
            x[index] = x[index] + 1
        create_pie()
        plt.draw()

axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Add Thought", textalignment="center")
text_box.on_text_change(update_text)

nextThought = Index()
axnext = plt.axes([0.8, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Add')
bnext.on_clicked(nextThought.next)
plt.show()
