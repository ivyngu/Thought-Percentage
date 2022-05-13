import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button

x = []
labels = []
expression = ""
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(x, labels=labels)
ax.set_title('My Thoughts')
plt.tight_layout()

def update_text(expression):
    expression=expression
    ax.relim()
    ax.autoscale_view()
    plt.draw()

axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Add Thought", textalignment="center")
text_box.on_text_change(update_text)

class Index:
    ind = 0

    def next(self, event):
        self.ind += 1
        x.append(self.ind)
        labels.append(expression)
        ax.pie(x, labels=labels)
        plt.draw()

nextThought = Index()
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Add')
bnext.on_clicked(nextThought.next)
plt.show()
