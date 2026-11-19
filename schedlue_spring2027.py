import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
C = {
 "P181E":"#4F7CAC","P181EL":"#2E5E8C","P181T":"#7FA7D1",
 "M360":"#7B5EA7","M200":"#D98A3D","E299":"#4E9F7D","CS340":"#C8566B"}

# (name, code, room, days, start, end, colour, instructor)
# days: 0=Mon ... 4=Fri; times are decimal hours (12.5 = 12:30 PM)
cl = [
 ("Elements of Physics I (Enhanced)","PHYS 181E","DMF280",[1,3],12.5,13.75,"P181E","D. Barros"),
 ("Elements of Physics I (ELAB)","PHYS 181EL","DMF280",[3],14+25/60,16.25,"P181EL","D. Barros"),
 ("Problem Solving in Physics","PHYS 181T","DMF280",[1],14+35/60,16.25,"P181T","D. Barros"),
 ("Foundations of Modern AI","MATH 360","DMF124",[0,2],13+50/60,15+5/60,"M360","S. Flood"),
 ("Statistical Methods I","MATH 200","DMF459",[1,3],11,12.25,"M200","K. Rion"),
 ("HON: 2YSem: Public & its Problems","ENGL 299","RSU114",[0,2,4],10+10/60,11,"E299","M. Hegbloom"),
 ("Organization of Program Lang","CS 340","DMF230",[0,2,4],11.25,12+5/60,"CS340","P. Kim"),
]

def fmt(h):  # 13.75 -> "1:45 PM"
    H=int(h); M=round((h-H)*60); ap="AM" if H<12 else "PM"; H12=H if H<=12 else H-12
    return f"{H12}:{M:02d} {ap}"

T0,T1=9,17   # grid runs 9 AM to 5 PM
fig,ax=plt.subplots(figsize=(16.5,10.5))
ax.set_xlim(-0.12,5); ax.set_ylim(T1,T0)   # reversed y so morning is at the top

# hour lines, half-hour lines, and time labels
for h in range(T0,T1+1):
    ax.axhline(h,color="#d8d8d8",lw=1,zorder=0)
    if h<T1: ax.axhline(h+.5,color="#efefef",lw=.7,zorder=0)
    ax.text(-0.02,h,fmt(h),ha="right",va="center",fontsize=10,color="#555")

# day columns and headers
for i in range(6):
    ax.axvline(i,color="#d8d8d8",lw=1,zorder=0)
for i,d in enumerate(days):
    ax.text(i+.5,T0-.12,d,ha="center",va="bottom",fontsize=14,fontweight="bold",color="#222")

# the class blocks: one rounded rectangle per class per day
for name,code,room,ds,s,e,c,ins in cl:
    for d in ds:
        pad=.03
        ax.add_patch(FancyBboxPatch((d+pad,s+.02),1-2*pad,e-s-.04,
            boxstyle="round,pad=0,rounding_size=0.04",fc=C[c],ec="white",lw=1.5,zorder=2))
        dur=e-s
        txt=f"{code}\n{name}\n{fmt(s)} – {fmt(e)}\n{room}"
        if dur>=1.4: txt+=f"\n{ins}"   # only longer blocks have room for the instructor
        ax.text(d+.5,s+dur/2,txt,ha="center",va="center",fontsize=9 if dur>1 else 8.5,
                color="white",zorder=3,linespacing=1.35,wrap=True)

ax.set_xticks([]); ax.set_yticks([])
for sp in ax.spines.values(): sp.set_visible(False)

fig.suptitle("Spring 2027 Weekly Schedule",fontsize=20,fontweight="bold",y=.985)
fig.text(.5,.928,"Bridgewater State · Classes run Jan 20 – May 11, 2027 · Rooms in Dana Mohler Faria SciMath Ctr (DMF) and Rondileau Student Union (RSU)",
         ha="center",va="center",fontsize=10.5,color="#555")
fig.subplots_adjust(left=.07,right=.985,top=.875,bottom=.03)

fig.savefig("schedule.png",dpi=150)
fig.savefig("schedule.pdf")