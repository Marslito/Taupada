from Libraries_import import tk,np,pywt,FigureCanvasTkAgg,NavigationToolbar2Tk,plt

from Init_widgets import (load_data_btn,slider_x,slider_1_start,slider_1_end,
                          canvas1,canvas2,stations_combobox, update_y_lim_btn,
                          update_scales_btn, save_waveform_btn,DWT_btn,
                          quit_btn,y_lim_entry,scales_start,scales_end,
                          scales_step)

from Init_figures import (f1_ax00,f2_ax00,f2_ax10,f1)
from Init_root import root, width,height

initial_directory = r'C:\Users\Felipe_PC\Desktop\New_folder'
initial_directory = r'/mnt/Data/Preprocessed_phase/Test/2022/12/11'
first_file_flag   = True

dt = 0.002
# Update figure functions ----------------------------------------------------:

from scipy import signal   
    
def high_pass_filter(s,dt,fc):
    
    #--------------------------------------------------------------------------
    # Description: Code to apply a zero-phase high-pass filtering to signal.  
    # Note:        Each signal is assumed to be in a column of the matrix s. 
    # Inputs: 
    #     s  : Signal matrix.
    #     dt : Sampling period of signals. 
    #     fc : Filter cutoff frequency. 
    # Outputs: 
    #     filtered: Filtered signal matrix.  
    #--------------------------------------------------------------------------
    
    fs       = 1/dt
    b,a      = signal.butter(4,fc,'hp', fs = fs)

    filtered = signal.filtfilt(b,a,s,axis = 0)
    filtered = filtered - np.mean(filtered,axis = 0)
    
    return filtered
    
def set_figure_limits():
    
    global temporal_samples,spatial_samples,t_aux,d_aux,D,T
    global x_lim_min,x_lim_max,y_lim_min,y_lim_max
    global wavelet_name,scales
    
    temporal_samples = data.shape[0]
    spatial_samples  = data.shape[1]
    t_aux            = np.arange(0,temporal_samples)
    d_aux            = np.arange(0,spatial_samples)
    D,T              = np.meshgrid(d_aux,t_aux)
    
    x_lim_min        = 0
    x_lim_max        = spatial_samples-1

    y_lim_min        = 0
    y_lim_max        = temporal_samples-1 

    wavelet_name     = 'cmor1.5-1.0'
    scales           = np.arange(5,200,2)
    
    #freq = pywt.scale2frequency(wavelet_name,scales)/dt
    
def set_slider_limits(): 
    
    global x 
    
    x = slider_x.get()
    
    slider_x.configure(from_= x_lim_min, to = x_lim_max)
    slider_1_start.configure(from_= y_lim_min, to = y_lim_max)
    slider_1_end.configure(from_= y_lim_min, to = y_lim_max)

    slider_1_start.set(y_lim_min)
    slider_1_end.set(y_lim_max)

    
def get_CWT():
    
    global CWT_data,T_CWT,F
    
    CWT_data,freqs = pywt.cwt(data[::10,x],scales,
                              wavelet_name,sampling_period = dt)

    T_CWT,F = np.meshgrid(t_aux[::10],freqs)   
  

def create_quad_and_lines(): 
    
    global f1_ax00_quad,f1_ax00_l0,f1_ax00_l1,f1_ax00_l2,f2_ax00_l0,f2_ax10_quad
    global bg
    

    f1_ax00_quad = f1_ax00.pcolormesh(D[::100,::10],T[::100,::10],
                                      data[::100,::10])

    f1_ax00_quad.set_clim([-3,3])
    
    
    f1_ax00_l0   = f1_ax00.axvline(10)
    f1_ax00_l0.set_color("r")

    f1_ax00_l1, = f1_ax00.plot(x,slider_1_start.get(),'k*')
    f1_ax00_l2, = f1_ax00.plot(x,slider_1_end.get(),'k*')
    
    f1_ax00.set_ylim([y_lim_min,y_lim_max])

    f2_ax00_l0, = f2_ax00.plot(data[:,x])

    f2_ax10_quad = f2_ax10.pcolormesh(T_CWT,F,np.abs(CWT_data))
    f2_ax10_quad.set_clim([0,0.5])
        
    canvas1.draw()
    
    canvas2.draw()

    
def update_figures(): 
    
    global x 
    
    x = slider_x.get()

    aux_index_1 = np.arange(slider_1_start.get(),slider_1_end.get())

    # Update vertical line and vertical dots:
    f1_ax00_l0.set_xdata(x)
    f1_ax00_l1.set_data(x,slider_1_start.get())
    f1_ax00_l2.set_data(x,slider_1_end.get())
    
    # Update temporal phase:
    f2_ax00.set_xlim([aux_index_1[0],aux_index_1[-1]])
    f2_ax00_l0.set_data(aux_index_1,data[aux_index_1,x])
    
    # Update CWT:
    get_CWT()
    f2_ax10_quad.set_array(np.abs(CWT_data))
    
    # Update canvas:
    canvas1.draw()
    canvas2.draw()

# Read data functions --------------------------------------------------------:
def open_file_dialog():
    
    global filename, data, first_file_flag
    
    filename = tk.filedialog.askopenfilename(initialdir = initial_directory, 
                                             title = 'Select file')   
    data     = np.float16(np.load(filename))
    
    data     = high_pass_filter(data.T,dt,0.8)
    
    if first_file_flag == True: 
        set_figure_limits()
        set_slider_limits()
        get_CWT()
        create_quad_and_lines()
        first_file_flag = False
    else:     
        update_figures()


# Slider functions------------------------------------------------------------:
def update_slider_x(value):
    
    update_figures()

def update_slider_1_start(value):

    if slider_1_start.get() >=  slider_1_end.get()-100:
        slider_1_start.set(slider_1_end.get()-100)
        
    update_figures()
        
def update_slider_1_end(value):

    if slider_1_end.get() <=  slider_1_start.get() + 100:
        slider_1_end.set(slider_1_start.get()+100)
        
    update_figures()
    
def select_stations(value):
    
    global f1_ax00_quad, f1_ax00_l0, f1_ax00_l1,f1_ax00_l2
    
    selected_station = stations_combobox.get()
    
    if selected_station == 'Full':
        x_range = np.arange(0,spatial_samples*10)
    elif selected_station == "SS-AT":
        x_range = np.arange(170,1950)
    elif selected_station == "AT-LL":
        x_range = np.arange(1950,3450)
    elif selected_station == "LL-ID":
        x_range = np.arange(3450,4800)
    elif selected_station == "ID-H" : 
        x_range = np.arange(4800,6500)        
    elif selected_station == "H-PA" :
        x_range = np.arange(6500,8420)                
    elif selected_station == "PA-RG":
        x_range = np.arange(8420,9650)                
    elif selected_station == "RG-RT":
        x_range = np.arange(9650,10450)                
    elif selected_station == "RT-RF":
        x_range = np.arange(10450,11920)                
    elif selected_station == "RF-OY":
        x_range = np.arange(11920,12800)              
    elif selected_station == "OY-G" :
        x_range = np.arange(12800,16000)                 
    elif selected_station == "G-end":
        x_range = np.arange(16000,18500)                
    else:
        x_range = np.arange(0,spatial_samples*10)

    
    x_range = np.arange(int(x_range[0]/10), int(x_range[-1]/10))
    
    slider_x.configure(from_ = x_range[0], to = x_range[-1])
    slider_x.set(x_range[0])
    
    # Update fig 1: 
    
    f1_ax00.cla()
    f1_ax00_quad = f1_ax00.pcolormesh(D[::100,x_range[0]:x_range[-1]],T[::100,x_range[0]:x_range[-1]],
                                      data[::100,x_range[0]:x_range[-1]])
    
    f1_ax00_quad.set_clim([-3,3])
    
    f1_ax00_l0   = f1_ax00.axvline(x_range[0])
    f1_ax00_l0.set_color("r")

    f1_ax00_l1, = f1_ax00.plot(x_range[0],slider_1_start.get(),'k*')
    f1_ax00_l2, = f1_ax00.plot(x_range[0],slider_1_end.get(),'k*')
    
    canvas1.draw()
    canvas1.get_tk_widget().pack()

def save_waveform():
    
    save_directory = r'D:\OneDrive - UPTECH SENSING S.L\UTS_AS1000 (Shared)\Development\06_EHW\Medidas ETS\Train_Dataset\Particular_Trains\Train930\930_Positive(SS-H)'
    
    time_stamp_aux = filename.split("/")[-1].split(".npy")[0]
    
    aux_start = int(slider_1_start.get())
    aux_end   = int(slider_1_end.get())
    aux_data  = data[aux_start:aux_end,x]
    
    # np.save(save_directory + "/" + time_stamp_aux + "_" + str(x), aux_data)
    np.save(save_directory + "/" + "930-" + time_stamp_aux + "_" + str(x), aux_data)

def open_DWT_analysis():

    aux_start = int(slider_1_start.get())
    aux_end   = int(slider_1_end.get())
    aux_data = data[aux_start:aux_end,x]


    top = tk.Toplevel()
    top.geometry("%dx%d" % (width, height))
    wavelet_name = 'db1'
    wavelet      = pywt.Wavelet(wavelet_name)
    
    frame_DWT = tk.Frame(top)
    frame_DWT.pack(expand = True, fill = tk.BOTH)

    
    f_DWT, axarr = plt.subplots(nrows = 5, ncols = 2)
    axarr[0, 0].set_title("Approximation coefficients", fontsize = 14)
    axarr[0, 1].set_title("Detail coefficients", fontsize = 14)
    
    for ii in range(5):
        
        print('pseudo freq: %.2f [Hz]'  %pywt.scale2frequency(wavelet_name,ii+1))
        print('central freq: %.2f [Hz]' %(pywt.scale2frequency(wavelet_name,ii+1)/dt))
    
        (aux_data, coeff_d) = pywt.dwt(aux_data, wavelet_name)
                
        axarr[ii, 0].plot(aux_data, 'r')
        axarr[ii, 1].plot(coeff_d, 'g')
        axarr[ii, 0].set_ylabel("Level {}".format(ii + 1), fontsize=14, rotation=90)

    
    canvas_DWT = FigureCanvasTkAgg(f_DWT,master = frame_DWT)
    canvas_DWT.draw()
    canvas_DWT.get_tk_widget().pack(expand = True, fill = tk.BOTH)

    
    DWT_tlb = NavigationToolbar2Tk(canvas_DWT,frame_DWT)
    DWT_tlb.pack()
    f_DWT.tight_layout()

    
    def fxd_():
        f_DWT.tight_layout()
        canvas_DWT.draw()

    adjust_layout = tk.Button(top,text='Adjust layout',command = fxd_)
    adjust_layout.pack()
    
    close_DWT_analysis_btn = tk.Button(top, text = 'Close DWT analysis' ,
                                       command = top.destroy)
    
    close_DWT_analysis_btn.pack(side = tk.BOTTOM)

def quit_app():
    
    plt.close('all')
    root.quit()
    root.destroy()
    
def update_y_lims():
    
    aux_y = float(y_lim_entry.get())

    f2_ax00.set_ylim([-aux_y,aux_y])
    canvas2.draw()

def update_CWT_scales():
    
    global scales
    
    aux_start = float(scales_start.get())
    aux_end   = float(scales_end.get())
    aux_step  = float(scales_step.get())

    scales = np.arange(aux_start,aux_end,aux_step)
    
    # Update CWT:
    get_CWT()
    f2_ax10_quad.set_array(np.abs(CWT_data))
    
    canvas2.draw()
# =============================================================================
#  Assign functions to widgets
# =============================================================================

# Master frame commands-------------------------------------------------------:
quit_btn.configure(command = quit_app)
    
# Subframe 0 commands --------------------------------------------------------:

# Sub sub frame 00 
stations_combobox.bind("<<ComboboxSelected>>", select_stations )

## Sub sub frame 01
update_y_lim_btn.configure(command = update_y_lims)
#
## Sub sub frame 02
update_scales_btn.configure(command = update_CWT_scales)
   
## Sub sub frame 03
save_waveform_btn.configure(command = save_waveform)

# Sub sub frame 04: 
DWT_btn.configure(command = open_DWT_analysis)
    
# Sub frame 1 commands -------------------------------------------------------:
load_data_btn.configure(command = open_file_dialog)

slider_x.bind("<ButtonRelease-1>", update_slider_x)
slider_1_start.bind("<ButtonRelease-1>", update_slider_1_start)
slider_1_end.bind("<ButtonRelease-1>", update_slider_1_end)
