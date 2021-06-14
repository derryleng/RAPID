from tkinter import filedialog

def load_file(filename):
    """
    Gets name of a file via dialog

    filename: Tkinter StringVar to set value for
    """
    x = filedialog.askopenfilename()
    print(x)
    filename.set(x)


def raise_frame(frame):
    frame.tkraise()

