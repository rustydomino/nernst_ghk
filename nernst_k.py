import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
from matplotlib.lines import Line2D
from matplotlib.widgets import Slider


class Scope:
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]  # initialize time data
        self.ydata = [0]  # initialize y data
        self.line = Line2D(self.tdata, self.ydata)  # create a line object
        self.ax.add_line(self.line)  # add the line to the axes
        self.ax.set_ylim(-200, 200)  # set the y-axis limits
        self.ax.set_xlim(0, self.maxt)  # set the x-axis limits
        self.text = self.ax.text(0.6, 0.9, '', transform=self.ax.transAxes) #creates a text object

    def update(self, y):
        lastt = self.tdata[-1]
        if lastt >= self.tdata[0] + self.maxt:  # reset the arrays if the time exceeds the limit
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)  # reset the x-axis limits
            self.ax.figure.canvas.draw()

        # This slightly more complex calculation avoids floating-point issues
        # from just repeatedly adding `self.dt` to the previous value.
        t = self.tdata[0] + len(self.tdata) * self.dt  # calculate the new time value

        self.tdata.append(t)  # append the new time value
        self.ydata.append(y)  # append the new y value
        self.line.set_data(self.tdata, self.ydata)  # set the line data
        update_text(y)
        return self.line,


def emitter():
    k_in = k_in_slider.val
    k_out = k_out_slider.val
    R = 8.314 # joule/K/mol
    T = 310 # in Kelvin
    F = 96485 # joule/volt/mol
    y = 1000*(R*T/F)*np.log(k_out/k_in)
    # y is just the dependent variable - put Nernst or GHK equation here eventually
    update_text(y)
    yield y

fig, ax = plt.subplots()
scope = Scope(ax)
# making some space for the slide at the bottom
plt.subplots_adjust(bottom=0.25)

#here is the slider code
#this line draws the slider in the figure
ax_k_in_slider = fig.add_axes([0.175, 0.15, 0.65, 0.03])
#the four parameters in fig.add_axes define the position and represent percentages of left, bottom width, height
k_in_slider = Slider(ax_k_in_slider, '[K]in (mM)', 1, 200, valinit= 100)

#attempting to add a second slider
ax_k_out_slider = fig.add_axes([0.175, 0.075, 0.65, 0.03])
k_out_slider = Slider(ax_k_out_slider, '[K]out (mM)', 1, 600, valinit=5)

# define a function that updates the text object with the slide value
def update_text(val):
    scope.text.set_text(f'E$_{{K}}$ = {val:.1f} mV') #some LaTeX fuckery here for subscript K, not sure how got italics?

# pass a generator in "emitter" to produce data for the update func
ani = animation.FuncAnimation(fig, scope.update, emitter, interval=50,
                              blit=True, save_count=100)



plt.show()

