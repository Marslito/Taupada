
from Libraries_import import tk, plt

# Root definition-------------------------------------------------------------:
root   = tk.Tk()
width  = root.winfo_screenwidth()               
height = root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))


px = 1/plt.rcParams['figure.dpi']  # pixel in inches


