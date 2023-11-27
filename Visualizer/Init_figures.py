from Libraries_import import plt
from Init_root import px,width,height

# Options to not show figures:
plt.ioff()

# Figure 1 -------------------------------------------------------------------:
f1           = plt.figure(figsize=(width*0.4*px,height*0.2*px))
f1_ax00      = f1.add_subplot(1,1,1)

f1_ax00.set_xlabel('Distance (samples)')
f1_ax00.set_ylabel('Time (samples)')

plt.tight_layout()

# Figure 2 -------------------------------------------------------------------:

f2       = plt.figure(figsize=(width*0.4*px,height*0.2*px))
f2_ax00  = f2.add_subplot(2,1,1)
f2_ax00.set_xticks([])
f2_ax00.set_xticklabels([])
f2_ax00.set_ylabel('Phase (rad)')

f2_ax10 = f2.add_subplot(2,1,2, sharex = f2_ax00)
f2_ax10.set_xlabel('Time (samples)')
f2_ax10.set_ylabel('Frequency (Hz)')

plt.tight_layout()