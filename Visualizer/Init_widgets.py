from Libraries_import import (tk, ttk,NavigationToolbar2Tk, FigureCanvasTkAgg)
from Init_root import root, width,height
from Init_figures import (f1,f2)

# =============================================================================
# Frames
# =============================================================================

# Master frame:
master_frame = tk.Frame(root)
master_frame.pack(expand = True, fill = tk.BOTH)

quit_btn = tk.Button(master_frame, text = 'Quit')
quit_btn.pack(side = tk.BOTTOM)

# Sub frame 0-----------------------------------------------------------------:
    
frame_0 = tk.LabelFrame(master_frame)
frame_0.pack(fill = tk.Y, side = tk.LEFT)



# Sub sub frame 00: 
frame_0_0 = tk.LabelFrame(frame_0)
frame_0_0.pack(expand = True, fill = tk.BOTH)

load_data_btn = tk.Button(frame_0_0, text = 'Load data')
load_data_btn.pack()

stations_label = tk.Label(frame_0_0,text = 'Select station')
stations_label.pack()

stations_combobox = ttk.Combobox(frame_0_0,state = "readonly",
                                 values = ["Full","SS-AT", "AT-LL", "LL-ID", 
                                           "ID-H","H-PA","PA-RG", "RG-RT",
                                           "RT-RF","RF-OY","OY-G","G-end"])
stations_combobox.pack()

# Sub sub frame 01: 
frame_0_1 = tk.LabelFrame(frame_0)
frame_0_1.pack(expand = True, fill = tk.BOTH)

y_lim_entry = tk.Entry(frame_0_1, width = 4)
y_lim_entry.pack()

update_y_lim_btn = tk.Button(frame_0_1, text = "Update Y-limits")
update_y_lim_btn.pack()

# Sub sub frame 02: 
frame_0_2 = tk.LabelFrame(frame_0, text = 'CWT scales')
frame_0_2.pack(expand = True, fill = tk.BOTH)

CWT_entry_frame = tk.Frame(frame_0_2)
CWT_entry_frame.pack()

scales_start = tk.Entry(CWT_entry_frame,width = 4)
scales_start.pack(side = tk.LEFT)

scales_end = tk.Entry(CWT_entry_frame,width = 4)
scales_end.pack(side = tk.LEFT)

scales_step = tk.Entry(CWT_entry_frame,width = 4)
scales_step.pack(side = tk.LEFT)

update_scales_btn = tk.Button(frame_0_2, text = "Update CWT scales")
update_scales_btn.pack(fill = tk.X)

# Sub sub frame 03: 
frame_0_3 = tk.LabelFrame(frame_0, text = 'Save waveform')
frame_0_3.pack(expand = True, fill = tk.BOTH)
save_waveform_btn = tk.Button(frame_0_3,text = 'Save waveform')
save_waveform_btn.pack()
comment_entry     = ttk.Entry(frame_0_3)
comment_entry.insert(0, "Comentario")
comment_entry.pack()

# Sub sub frame 04: 
frame_0_4 = tk.LabelFrame(frame_0)
frame_0_4.pack(expand = True, fill = tk.BOTH)

DWT_btn = tk.Button(frame_0_4,text = "DWT")
DWT_btn.pack()

# Sub frame 1-----------------------------------------------------------------: 
frame_1 = tk.Frame(master_frame)
frame_1.pack(fill = tk.BOTH)

control_1_frame = tk.LabelFrame(frame_1)
control_1_frame.pack(fill = tk.Y, side = tk.LEFT)

plot_frame_1 = tk.LabelFrame(frame_1,text = 'Plot frame')
plot_frame_1.pack(expand = True, fill = tk.BOTH)

canvas1 = FigureCanvasTkAgg(f1,master = plot_frame_1)
canvas1.draw()
canvas1.get_tk_widget().pack(expand = True, fill = tk.BOTH)

# Sub frame 2-----------------------------------------------------------------: 
frame_2 = tk.Frame(master_frame)
frame_2.pack( expand = True, fill = tk.BOTH)

plot_frame_2 = tk.LabelFrame(frame_2, text='Plot 2 frame')
plot_frame_2.pack(expand = True, fill = tk.BOTH)

canvas2 = FigureCanvasTkAgg(f2,master = plot_frame_2)
canvas2.draw()
canvas2.get_tk_widget().pack(expand = True, fill = tk.BOTH)

tlb = NavigationToolbar2Tk(canvas2,plot_frame_2)
tlb.pack()
# =============================================================================
# Sliders
# =============================================================================

    
# Horizontal slider ----------------------------------------------------------:
slider_x = tk.Scale(plot_frame_1,
                 orient = tk.HORIZONTAL,length = width*0.3,
                 width = 10)

slider_x.pack()

# Control_1_frame sliders ----------------------------------------------------:

slider_1_start = tk.Scale(control_1_frame,
                       orient=tk.VERTICAL,length = height/4,width = 10)
slider_1_start.grid(row = 0,column = 0)

slider_1_end = tk.Scale(control_1_frame,
                     orient=tk.VERTICAL,length = height/4,width = 10)
slider_1_end.grid(row = 0,column = 1)




