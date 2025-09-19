from tkinter import *
from tkinter import ttk

# Constants
HFILL_STICKY = (W, E)
VFILL_STICKY = (N, S)
FILL_STICKY  = (N, S, W, E)

# Custom classes
class StringVarEntry():
    """Custom class for ttk.Entry with ttk.StringVar"""

    def __init__(self, master=None, widget=None, **kw):
        self.textvariable = StringVar()
        self.entry = ttk.Entry(master=master, widget=widget, textvariable=self.textvariable, **kw)

    def set(self, value):
        self.textvariable.set(value)

# Add root
root = Tk()

# Menu Frame
menuframe = ttk.Frame(root)
ttk.Label(menuframe, text="EVERY"  ).grid(row=0, column=0, sticky=E)
ttk.Label(menuframe, text="MINUTES").grid(row=0, column=2, sticky=W)
ttk.Label(menuframe, text="AND"    ).grid(row=1, column=0, sticky=E)
ttk.Label(menuframe, text="SECONDS").grid(row=1, column=2, sticky=W)
ttk.Label(menuframe, text="FOR"    ).grid(row=2, column=0, sticky=E)
ttk.Label(menuframe, text="ROUNDS" ).grid(row=2, column=2, sticky=W)
ttk.Label(menuframe, text="REST"   ).grid(row=3, column=0, sticky=E)
ttk.Label(menuframe, text="SECONDS").grid(row=3, column=2, sticky=W)
mins   = StringVarEntry(master=menuframe)
secs   = StringVarEntry(master=menuframe)
rounds = StringVarEntry(master=menuframe)
rest   = StringVarEntry(master=menuframe)
mins.entry.grid  (row=0, column=1, sticky=HFILL_STICKY)
secs.entry.grid  (row=1, column=1, sticky=HFILL_STICKY)
rounds.entry.grid(row=2, column=1, sticky=HFILL_STICKY)
rest.entry.grid  (row=3, column=1, sticky=HFILL_STICKY)
mins.set  ( 1)
secs.set  ( 0)
rounds.set(10)
rest.set  ( 0)

# Add execution of root main loop
root.mainloop()
