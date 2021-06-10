from tkinter import filedialog

def load_file(tk_var):
    """
    Gets name of a file via dialog

    tk_var (string): name of the Tkinter StringVar to set value for
    """
    x = filedialog.askopenfilename()
    print(x)
    eval(tk_var + ".set(x)")


def raise_frame(frame):
    frame.tkraise()

