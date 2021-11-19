"""
S.Y.S.M.S. powered by Python

################################### CONTENT ####################################
S.No.   Topic                              Line
================================================================================
1.      Modules                            5 - 29
2.      SPEECH RECOGNITION & VOICE        32 - 67
3.      QUERY AND RESPONSE                69 - 154
4.      WISH ME AND STARTING PHRASE      156 - 176
5.      GUI                              179 - 1749
5.1.    Gui setting                      182 - 187
5.2.    Message-box                      189 - 220
5.3.    Info-box                         222 - 396
5.4.    Clock-box                        398 - 642
5.5.    Weather-box                      644 - 716
5.6.    News categories-box              718 - 941
5.7.    Quick Icon                       943 - 1219
5.8.    Quick Access-box                1222 - 1425
5.9.    SYSMS logo & ester egg           1427 - 1642
5.10.   About SYSMS                      1644 - 1670
5.11.   Key binding                     1672 - 1677
5.12.   Threading for Progressbar       1679 - 1742
==================================================================================
Moudule to be install:
pip install tkcalendar
pip install pillow
pip install pyttsx3
pip install speechRecognition
pip install psutil
pip install GPUtil
pip install requests
pip install wikipedia
pip install newsapi-python

"""
##################################### MODULE #####################################

from datetime import datetime
import datetime as dt
import random
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkcalendar import *            # pip install tkcalendar
from PIL import ImageTk, Image      # pip install pillow
import pyttsx3                      # pip install pyttsx3
import speech_recognition as sr     # pip install speechRecognition
import subprocess
import os
import psutil                       # pip install psutil
import platform
import GPUtil                       # pip install GPUtil
import turtle
import time
import threading                       
import requests                     # pip install requests
import webbrowser
import wikipedia                    # pip install wikipedia
from newsapi import NewsApiClient   # pip install newsapi-python

######################## SPEECH RECOGNITION & VOICE ################################

# Setting up pyttsx3 as speak function
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Setting up Speech recognition as takeCommand funtion

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        textF.delete(0, END)
        textF.insert(0, query.lower())
        ask_from_bot()
    except Exception as e:
        print(e)
        # print("Say that again please...")
        return "None"

################################### QUERY AND RESPONSE  ##########################################

def ask_from_bot():
    query = textF.get()
    msgs.insert(END, " you : " + query)
    
    # Questions
    blank=''
    greetingQ=["hello","hi","hey","hii","hiii","hiii","Namaste","Hola"]
    How_are_uQ=["how are you","whats up","what's up","how you doing"]
    music=["play music", "open music",]
    whoRuQ=["Who are you","tell me about yourself","who r u", "who are you"]
    tttgameP=["do u want to play tic tac toe","do u wanna play tic tac toe","play tic tac toe","let's play tic tac toe","lets play tic tac toe","let play tic tac toe", "tic tac toe","do u want to play tic tac toe game","do u wanna play tic tac toe game","play tic tac toe game","let's play tic tac toe game","lets play tic tac toe game","let play tic tac toe game", "tic tac toe game", "open tic tac","play tic tac","open tic tac to","play tic tac to"]
    newQ=["tell me some news","today news","today's news","todays news","news","tell news","tell me news"]
    search=["search","wikipedia","google it","google",'meaning']
    ums=["open u m s lpu","open  u m s","open university management system","ums","u m s","lpu"]
    lpu_live=("open l p u live","open lpulive","lpu live")
    video=("open youtube")
    stop=["take rest","bye","good night","see u","see you","okay then bye","ok bye"]
    myclass=["myclass","my class","open my class","open myclass","Open Myclass","Open My class"]
    camera=["camera","take a photo"]
    per=[ "who made you","who discovered you"]
    ability=["what can you do","tell me your abilites","who are you"]
    # Answers
    if query == blank:
        ans='Are you kidding me with a blank message'        
        msgs.insert(END, " SYSMS : "+ans)
        speak(ans)
    elif query in greetingQ:
        lst = ['hello','hi', 'oh hello','Hello How are you', 'Hola', 'Namaste','Sat Sri Akaal Ji']
        choice = random.choice(lst)
        msgs.insert(END, " SYSMS : "+choice)
        speak(choice)        
    elif query in How_are_uQ:
        lst = ['fine sir','fantastic sir', 'wonderful sir','great sir']
        choice = random.choice(lst)
        msgs.insert(END, " SYSMS : "+choice)
        speak(choice)
    elif query in whoRuQ:
        msgs.insert(END, " SYSMS : I'm SYSMS, S Y S M S System Multitasking Servant, I'm mark 7, before me 5 version are tested, right now I'm the best of myself")        
        speak("I'm SYSMS, S Y S M S System Multitasking Servant, I'm mark 7, before me 5 version are tested, right now I'm the best of myself")
    elif query in tttgameP:        
        msgs.insert(END, " SYSMS : Why not!!!")        
        speak("Why not!")
        tttgame()
    elif "news on topic" in query: # news on topic india = ['news', 'on', 'topic', 'india']
        y = query.split(' ')
        MNews(y[-1])
    elif query in newQ:
        News()
    elif query in search:           #For searching
        speak('Searching web')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to web")
        msgs.insert(END, " SYSMS : "+results)
        speak(results)
    elif query in video:            #for youtube
        speak('opening youtube...')
        msgs.insert(END, " SYSMS : Opening Youtube...")
        webbrowser.open("youtube.com")
    elif query in ums:              #for ums opening tab
        speak('opening UMS LPU')
        msgs.insert(END, " SYSMS : opening UMS LPU")
        webbrowser.open("ums.lpu.in")
    elif query in myclass:              #for myclass opening tab
        speak('opening MyClass')
        msgs.insert(END, " SYSMS : opening MyClass")
        webbrowser.open("https://myclass.lpu.in/")
    elif query in lpu_live:         #for lpu live opening tab
        speak('Opening LPU live')
        msgs.insert(END, " SYSMS : Opening LPU live")
        webbrowser.open("lpulive.lpu.in")
    elif query in stop:             #for stopping SYSMS
        lst = ['Have a Good Day!','Good Bye!','Thank you for choosing me.']
        choice = random.choice(lst)
        msgs.insert(END, " SYSMS : "+choice)
        speak(choice)
        root.destroy()
    elif query in ability:          #questions
        speak("I am SYSMS i can perform certain functions like searching,opening different tabs and many more")
        msgs.insert(END, " SYSMS : I am SYSMS i can perform certain functions like searching,opening different tabs and many more")
    elif query in per:              #about creators(add)
        speak("My Creaters name is Sachin Kumar and Akshay Anand")
        msgs.insert(END, " SYSMS : My Creaters name is Sachin Kumar and Akshay Anand")
    else:
        speak("Pardon, I didn't understand")
        msgs.insert(END, " SYSMS : Pardon, I didn't understand")
    textF.delete(0, END)
    # msgs.yview(END)

################################## WEATHER FUNCTION ######################################

# location using ipinfo
res = requests.get('https://ipinfo.io')
data = res.json()
city = data['city']

# weather - using open weather api
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
api_key = 'bcf589bf3a118b08bb2e67c66a87ccd7'
# funtion for check weather
def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
         
        json = result.json()

        country = json['sys']['country']

        # temperature conversion
        temp_kelvin = json['main']['temp']
        temp_celcius = temp_kelvin - 273.15 
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32


        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        weatherdescs = json['weather'][0]['description']

        # making tuple
        final =  (city, country, temp_celcius, temp_fahrenheit, icon, weather,weatherdescs)

        # returning tuple 
        return final
        
    else:
        return None

weatherS = get_weather(city)
line = f'{weatherS[6]}, In {city}, Right Now Temperature is {int(weatherS[2])} Degree Celcius'
print(line)

################################## WISH ME AND STARTING PHRASE ######################################
def wishMe():
    # current time
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

# Starting Phrase 
wishMe()
speak("Setting Things Up, checking componet")
speak("Uploading files... ")
speak("Loading...")
speak("Hello Sir, Now I'm Online")
speak(line)


############################################# GUI ###################################################

# Setting up gui
root = Tk()
root.geometry("510x485")
root.title("SYSMS Mark 7.0")
root.minsize(510,485)
root.iconbitmap('icon/sysms.ico')

# Creating Message-Box
wrapper0 = LabelFrame(root,text="Message-Box Powered by S.Y.S.M.S.")
wrapper0.place(x=6,y=5,height=475,width=500)

# For chat history
wrapper1 = LabelFrame(wrapper0)
wrapper1.pack(fill="both",expand="yes",padx=5,pady=5)

# Message and scroll Function
msgs = Listbox(wrapper1, font=('Arial'),width=80,relief=GROOVE)
sc = Scrollbar(wrapper1,command=msgs.yview)
sc.pack(side=RIGHT, fill=Y)
scy = Scrollbar(wrapper1,orient=HORIZONTAL,command=msgs.xview)
scy.pack(side=BOTTOM, fill=X)
msgs.configure(yscrollcommand=sc.set,xscrollcommand=scy.set)
msgs.pack(side=LEFT, fill=BOTH, pady=5,padx=5)

# For Entry-Box
wrapper2 = LabelFrame(wrapper0)
wrapper2.pack(fill="both",expand="yes",padx=5,pady=5)

# creating text field
textF = Entry(wrapper2,font=("Verdana"),relief=GROOVE)
textF.place(x=5,y=3,height=70,width=365)

# Send button for text field
btn = Button(wrapper2, text="SEND",bg='light blue',activebackground='light green',relief=GROOVE,command=ask_from_bot)
btn.place(x=378,y=40,height=35,width=100)

# Voice button for voice command
VoiceButton=Button(wrapper2,text='VOICE',bg='light blue',activebackground='light green',relief=GROOVE, command=takeCommand)
VoiceButton.place(x=378,y=3,height=35,width=100)

# Creating Info-Box
wrapper4 = LabelFrame(root,text="Info Powered by S.Y.S.M.S. ")
wrapper4.place(x=6,y=500,height=285,width=500)

# Creating progressbar
var_cpu = IntVar()
pgbar_cpu = Progressbar(wrapper4,orient=VERTICAL,mode='determinate',maximum=100,length=260,variable=var_cpu)
pgbar_cpu.place(x=120, y=2)

var_ram = IntVar()
pgbar_ram = Progressbar(wrapper4,orient=HORIZONTAL,mode='determinate',maximum=100,length=200,variable=var_ram)
pgbar_ram.place(x=150, y=22)

var_store = IntVar()
pgbar_store = Progressbar(wrapper4,orient=HORIZONTAL,mode='determinate',maximum=100,length=200,variable=var_store)
pgbar_store.place(x=150, y=90)

var_bat = IntVar()
pgbar_bat = Progressbar(wrapper4,orient=HORIZONTAL,mode='determinate',maximum=100,length=100,variable=var_bat)
pgbar_bat.place(x=150, y=138)

# Create box for CPU info
wrapper4_1 = LabelFrame(wrapper4,text="CPU INFO Powered by S.Y.S.M.S. ")
wrapper4_1.place(x=150,y=165,height=95,width=200)

# CPU info - PSUTIL
cpufreq = psutil.cpu_freq()
Label(wrapper4_1,text="CPU Physical Core: "+str(psutil.cpu_count(logical=False))).place(x=5,y=3)
Label(wrapper4_1,text="CPU Logical Core: "+str(psutil.cpu_count())).place(x=5,y=23)
Label(wrapper4_1,text=f"Max Frequency: {cpufreq.max:.2f}Mhz").place(x=5,y=45)

# Create box for system info
wrapper4_2 = LabelFrame(wrapper4,text="System Info")
wrapper4_2.place(x=360,height=260,width=130)

#Fairly portable uname interface. Returns a tuple of strings (system, node, release, version, machine, processor) identifying the underlying platform.
uname = platform.uname()

# system info
Label(wrapper4_2,text=f"System OS: {uname.system}").place(x=5,y=3)
Label(wrapper4_2,text=f"Name: {uname.node}").place(x=5,y=23)
Label(wrapper4_2,text=f"Version: {uname.version}").place(x=5,y=45)
Label(wrapper4_2,text=f"Release: {uname.release}").place(x=5,y=65)

# More System info button
# function for that buttons

# Cpu Info - PSUTIL
def cpuinfo():
    # print("Button clicked!")
    messagebox.showinfo("CPU INFO Powered by SYSMS",f"Machine: {uname.machine}\nProcessor: {uname.processor}")

# for getting size in max unit
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# changing list to sting
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 = str1 + "\n" + ele   
    
    # return string   
    return str1 

# storage info - PSUTIL
def diskinfo():
    # print("Button clicked!")
    disk = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        h = f"=== Device: {partition.device} ===\n"
        h += f"  Mountpoint: {partition.mountpoint}\n"
        h += f"  File system type: {partition.fstype}\n"
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        h += f"  Total Size: {get_size(partition_usage.total)}\n"
        h += f"  Used: {get_size(partition_usage.used)}\n"
        h += f"  Free: {get_size(partition_usage.free)}\n"
        h += f"  Percentage: {partition_usage.percent}%\n"
        disk.append(h)
    msg = listToString(disk)
    # messagebox.showinfo("CPU INFO Powered by SYSMS",disk[0]+"\n"+disk[1])
    messagebox.showinfo("Disk INFO Powered by SYSMS","Disk Partiton and Info...\n"+msg)

# boot time - PSUTIL
def bootTime():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    messagebox.showinfo("Boot Time Powered by SYSMS",f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

# Graphics info - GPUTIL
def GPUinfo():
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        # name of GPU
        h = "GPU Name: "+gpu.name+"\n"
        # get % percentage of GPU usage of that GPU
        h += f"GPU Load: {gpu.load*100}%\n"
        # get free memory in MB format
        h += f"GPU Memory Free: {gpu.memoryFree} MB\n"
        # get used memory
        h += f"GPU Memory Used: {gpu.memoryUsed} MB\n"
        # get total memory
        h += f"GPU Total Memory: {gpu.memoryTotal} MB\n"
        # get GPU temperature in Celsius
        h += f"GPU Temperature: {gpu.temperature} °C\n"
        h = h +"GPU UID: "+str(gpu.uuid)+"\n"
        list_gpus.append(h)
    msg = listToString(list_gpus)
    messagebox.showinfo("GPU INFO Powered by SYSMS","GPU Info...\n"+msg)

# changing list to sting without creating new line
def listToStringWOnewline(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 = str1 + ele   
    
    # return string   
    return str1 

# newtowk info - PSUTIL
def networkInfo():
    if_addrs = psutil.net_if_addrs()
    msgbx = []
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            h = f"=== Interface: {interface_name} ===\n"
            if str(address.family) == 'AddressFamily.AF_INET':
                h += f"  IP Address: {address.address}\n"
                h += f"  Netmask: {address.netmask}\n"
                h += f"  Broadcast IP: {address.broadcast}\n"
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                h += f"  MAC Address: {address.address}\n"
                h += f"  Netmask: {address.netmask}\n"
                h += f"  Broadcast MAC: {address.broadcast}\n"
            msgbx.append(h)    

    msg = listToStringWOnewline(msgbx)
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    msg += f"Total Bytes Sent: {get_size(net_io.bytes_sent)}\n"
    msg += f"Total Bytes Received: {get_size(net_io.bytes_recv)}\n"
    # print(msg)
    messagebox.showinfo("Network INFO Powered by SYSMS",msg)

# Buttons for more System info 
btn_cpu=Button(wrapper4_2,text='CPU MORE INFO...',relief=GROOVE, command=cpuinfo).place(x=5,y=90,width=115)
btn_disk=Button(wrapper4_2,text='DISK MORE INFO...',relief=GROOVE, command=diskinfo).place(x=5,y=120,width=115)
btn_boot=Button(wrapper4_2,text='BOOT TIME...',relief=GROOVE, command=bootTime).place(x=5,y=150,width=115)
btn_gpu=Button(wrapper4_2,text='GPU INFO...',relief=GROOVE, command=GPUinfo).place(x=5,y=180,width=115)
btn_network=Button(wrapper4_2,text='NETWORK INFO...',relief=GROOVE, command=networkInfo).place(x=5,y=210,width=115)

# Creating Clock-Box
# Clock Section
def clock():
    t2=time.strftime("%H:%M:%S %p")
    t3=Label(frame5_2,text=t2,font=('ds digital',40,'bold'),fg='#06b025',bg="#e6e6e6")
    t3.after(1000,clock)
    t3.place(x=5,y=5)
    t4=dt.date.today()
    t5=Label(frame5_1,text=t4.year,font=('ds digital',40,'bold'),fg='#06b025',bg="#e6e6e6").place(x=10,y=5)
    t6=Label(frame5_1,text=t4.month,font=('ds digital',40,'bold'),fg='#06b025',bg="#e6e6e6").place(x=150,y=5)
    t7=Label(frame5_1,text=t4.day,font=('ds digital',40,'bold'),fg='#06b025',bg="#e6e6e6").place(x=235,y=5)
    t8=Label(frame5_1,text='YEAR',font=('ds digital',15),fg='#06b025',bg="#e6e6e6").place(x=20,y=65)
    t9=Label(frame5_1,text='MONTH',font=('ds digital',15),fg='#06b025',bg="#e6e6e6").place(x=140,y=65)
    t10=Label(frame5_1,text='DATE',font=('ds digital',15),fg='#06b025',bg="#e6e6e6").place(x=235,y=65)
    t11=Label(frame5_2,text='HOUR',font=('ds digital',15),fg='#06b025',bg="#e6e6e6").place(x=5,y=65)
    t12=Label(frame5_2,text='MIN',font=('ds digital',15),fg='#06b025',bg="#e6e6e6").place(x=90,y=65)
    t13=Label(frame5_2,text='SEC',font=('ds digital',15),fg='#06b025',bg="#e6e6e6").place(x=160,y=65)
# Used so much frame for designing...
wrapper5 = LabelFrame(root, text="Clock Powered by S.Y.S.M.S.")
wrapper5.place(x=520,y=5,height=320,width=440)
frame5 = Frame(wrapper5)
frame5.place(x=0,y=0,height=300,width=350)
wrapper5_1 = LabelFrame(frame5,text="Date")
wrapper5_1.pack(fill="both",expand="yes",padx=5,pady=5)
frame5_1 = Frame(wrapper5_1,highlightbackground="#bfbfbf", highlightcolor="#bfbfbf", highlightthickness=1,bg="#e6e6e6")
frame5_1.pack(fill="both",expand="yes",padx=5,pady=5)
wrapper5_2 = LabelFrame(frame5,text="Time")
wrapper5_2.pack(fill="both",expand="yes",padx=5,pady=5)
frame5_2 = Frame(wrapper5_2,highlightbackground="#bfbfbf", highlightcolor="#bfbfbf", highlightthickness=1,bg="#e6e6e6")
frame5_2.pack(fill="both",expand="yes",padx=5,pady=5)
clock()
wrapper5_3 = LabelFrame(wrapper5)
wrapper5_3.place(x=350,y=12,height=283,width=80)

# Creating Clock funtion button like alarm,  timer...
# fuction for that buttons 
def alarm():
    file_name = "border.py"
    command = 'explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App'
    subprocess.run(command, shell=True)


def timer():
    class Countdown(Frame):
        '''A Frame with label to show the time left, an entry
        to input the seconds to count down from, and a
        start button to start counting down.'''
        def __init__(self, master):
            super().__init__(master)
            self.create_widgets()
            self.show_widgets()
            self.seconds_left = 0
            self._timer_on = False

        def show_widgets(self):

            self.label.pack()
            self.entry.pack()
            self.start.pack()

        def create_widgets(self):

            self.label = Label(self, text="00:00:00",font="Verdana 30 bold")
            self.entry = Entry(self, justify='center')
            self.entry.focus_set()
            self.start = Button(self, text="Start",command=self.start_button)

        def countdown(self):
            '''Update label based on the time left.'''
            self.label['text'] = self.convert_seconds_left_to_time()

            if self.seconds_left:
                self.seconds_left -= 1
                self._timer_on = self.after(1000, self.countdown)
            else:
                self._timer_on = False
                speak("Time Up")
                messagebox.showinfo("Timer","Time Up")
                

        def start_button(self):
            '''Start counting down.'''
            # 1. to fetch the seconds
            self.seconds_left = int(self.entry.get())
            # 2. to prevent having multiple
            self.stop_timer()
            #    timers at once
            self.countdown()                            

        def stop_timer(self):
            '''Stops after schedule from executing.'''
            if self._timer_on:
                self.after_cancel(self._timer_on)
                self._timer_on = False
                

        def convert_seconds_left_to_time(self):
            return dt.timedelta(seconds=self.seconds_left)


    root = Tk()
    # root.resizable(False, False)
    root.title("Timer Powered by S.Y.S.M.S.")
    root.geometry("330x150")
    root.resizable(False,False)
    root.iconbitmap('icon/timer.ico')
    countdown = Countdown(root)
    countdown.pack(pady=20)
    root.mainloop()


def cal():
    CALroot = Tk()
    CALroot.title("Calender Powered by S.Y.S.M.S.")
    CALroot.geometry("350x300")
    CALroot.resizable(False,False)
    CALroot.iconbitmap('icon/Cal.ico')

    cal = Calendar(CALroot, selectmode="day",year=2020, month=11,day=3)
    cal.pack(padx=20,pady=20,fill="both",expand=True)
    CALroot.mainloop()


counter = 66600
running = False
def sWatch():    
    def counter_label(label): 
        def count(): 
            if running: 
                global counter 
        
                # To manage the intial delay. 
                if counter==66600:			 
                    display="Starting..."
                else: 
                    tt = datetime.fromtimestamp(counter) 
                    string = tt.strftime("%H:%M:%S") 
                    display=string 
        
                label['text']=display # Or label.config(text=display) 
        
                # label.after(arg1, arg2) delays by 
                # first argument given in milliseconds 
                # and then calls the function given as second argument. 
                # Generally like here we need to call the 
                # function in which it is present repeatedly. 
                # Delays by 1000ms=1 seconds and call count again. 
                label.after(1000, count) 
                counter += 1
        
        # Triggering the start of the counter. 
        count()	 
        
    # start function of the stopwatch 
    def Start(label): 
        global running 
        running=True
        counter_label(label) 
        start['state']='disabled'
        stop['state']='normal'
        reset['state']='normal'
        
    # Stop function of the stopwatch 
    def Stop(): 
        global running 
        start['state']='normal'
        stop['state']='disabled'
        reset['state']='normal'
        running = False
        
    # Reset function of the stopwatch 
    def Reset(label): 
        global counter 
        counter=66600
        
        # If rest is pressed after pressing stop. 
        if running==False:	 
            reset['state']='disabled'
            label['text']='STOP-WATCH'
        
        # If reset is pressed while the stopwatch is running. 
        else:				 
            label['text']='Starting...'
        
    root = Tk() 
    root.title("Stopwatch Powered by S.Y.S.M.S.") 
    root.geometry('350x150')
    root.iconbitmap('icon/sWatch.ico')	
    # Fixing the window size.
    root.resizable(False,False) 
    label = Label(root, text="STOP-WATCH", fg="black", font="Verdana 30 bold") 
    label.pack(pady=20) 
    f = Frame(root) 
    start = Button(f, text='Start', width=6, command=lambda:Start(label)) 
    stop = Button(f, text='Stop',width=6,state='disabled', command=Stop) 
    reset = Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label)) 
    f.pack(anchor = 'center',pady=5) 
    start.pack(side="left") 
    stop.pack(side ="left") 
    reset.pack(side="left") 
    root.mainloop() 


# Clock option Button using image - PILLOW(for resize)
cal_pic = Image.open('img/cal.png')
resized = cal_pic.resize((45,45), Image.ANTIALIAS)
cal_NewPic = ImageTk.PhotoImage(resized)
cal_label = Label(root, image=cal_NewPic)
btn_cal=Button(wrapper5_3,image=cal_NewPic,relief=GROOVE, command=cal).place(x=2.5,y=2,height=70,width=70)

timer_pic = Image.open('img/timer.png')
resized = timer_pic.resize((40,40), Image.ANTIALIAS)
timer_NewPic = ImageTk.PhotoImage(resized)
timer_label = Label(root, image=timer_NewPic)
btn_timer=Button(wrapper5_3,image=timer_NewPic,relief=GROOVE, command=timer).place(x=2.5,y=70,height=70,width=70)

sWatch_pic = Image.open('img/sWatch.png')
resized = sWatch_pic.resize((40,40), Image.ANTIALIAS)
sWatch_NewPic = ImageTk.PhotoImage(resized)
sWatch_label = Label(root, image=sWatch_NewPic)
btn_sWatch=Button(wrapper5_3,image=sWatch_NewPic,relief=GROOVE, command=sWatch).place(x=2.5,y=138,height=70,width=70)

alarm_pic = Image.open('img/alarm.png')
resized = alarm_pic.resize((40,40), Image.ANTIALIAS)
alarm_NewPic = ImageTk.PhotoImage(resized)
alarm_label = Label(root, image=alarm_NewPic)
btn_alarm=Button(wrapper5_3,image=alarm_NewPic,relief=GROOVE, command=alarm).place(x=2.5,y=206,height=70,width=70)

# clock showing date and time
clock()

# Creating Weather-Box
wrapper6 = LabelFrame(root, text="Weather Powered by S.Y.S.M.S.")
wrapper6.place(x=520,y=330,height=175,width=440)
frame6 = Frame(wrapper6, bg='white',highlightbackground="#bfbfbf", highlightcolor="#bfbfbf", highlightthickness=1)
frame6.place(x=5,y=2,height=145,width=335)





# checking city location
city = data['city']
# get weather called
weather = get_weather(city)

# if got weather then creating gui 
if weather:
    location_lbl = Label(frame6, text= f'{weather[0]}, {weather[1]}' , font=('bold',20),bg='white')
    location_lbl.pack(pady=20)

    img_weather = PhotoImage(file=f'weatherIcon/{weather[4]}.png')
    image = Label(frame6, image=img_weather,bg='white')
    image.place(x=5,y=5)

    temp_lblC = Label(frame6, text=f'{int(weather[2])}',font=('ds digital',40,'bold'),bg='white')
    temp_lblC.place(x=130, y=60)
    temp_lblF = Label(frame6, text=f'°C / {int(weather[3])}°F',font=('ds digital',20,'bold'),bg='white')
    temp_lblF.place(x=190, y=65)

    weather_lbl = Label(frame6, text=weather[5],font=('bold',18),bg='white')
    weather_lbl.place(x=25,y=110)

     

# call for search weather for different cities  
def weatherSearch():
    subprocess.call(["python", "Files/weather.py"])

# creating image button for search weather
weather_pic = Image.open('img/weather.png')
resized = weather_pic.resize((85,152), Image.ANTIALIAS)
weather_NewPic = ImageTk.PhotoImage(resized)
weather_label = Label(root, image=weather_NewPic)
btn_weather=Button(wrapper6,image=weather_NewPic,relief=GROOVE, command=weatherSearch).place(x=347,y=1,height=152,width=85)

# News categoies box
wrapper7 = LabelFrame(root, text="NEWS Powered by S.Y.S.M.S.")
wrapper7.place(x=520,y=510,height=185,width=250)

newsapi = NewsApiClient(api_key='f8d16e69437940019a0bf2cb08e961f8')

# for counting 
num = ['first','second','third','fourth','fifth','sixth','seventh','eight','ninth','tenth']

# Button for News categories
# Button function

def News():
    # getting head lines
    top_headlines = newsapi.get_top_headlines(category='general',country='in')
    
    # creating list
    articles = top_headlines['articles']
    if len(articles) < 10 and len(articles) > 0:
        speak("Not much news today") 
    elif len(articles) == 0:
        speak("No news today related to ")
    else:
        pass
    # speaking and show headline in chat
    msgs.insert(END, " SYSMS : Today's news are like this :-")
    speak("Today's news are like this:")    
    for x,y in enumerate(articles):
        news_title = f'{x+1}.  {y["title"]}'        
        msgs.insert(END, "         "+news_title)
        if x+1 <= 5:        
            speak(str(num[x])+', '+y["title"])
    

def ENews():
    # getting head lines
    top_headlines = newsapi.get_top_headlines(category='entertainment',country='in')
    
    # creating list
    articles = top_headlines['articles']
    if len(articles) < 10 and len(articles) > 0:
        speak("Not much news today") 
    elif len(articles) == 0:
        speak("No news today related to ")
    else:
        pass
    # speaking and show headline in chat
    msgs.insert(END, " SYSMS : Today's entertainment news are like this :-")
    speak("Today's entertainment news are like this:")    
    for x,y in enumerate(articles):
        news_title = f'{x+1}.  {y["title"]}'        
        msgs.insert(END, "         "+news_title)
        if x+1 <= 5:        
            speak(str(num[x])+', '+y["title"])

def Hnews():
    # getting head lines
    top_headlines = newsapi.get_top_headlines(category='health',country='in')
    
    # creating list
    articles = top_headlines['articles']
    if len(articles) < 10 and len(articles) > 0:
        speak("Not much news today") 
    elif len(articles) == 0:
        speak("No news today related to ")
    else:
        pass
    # speaking and show headline in chat
    msgs.insert(END, " SYSMS : Today's health news are like this :-")
    speak("Today's health news are like this:")    
    for x,y in enumerate(articles):
        news_title = f'{x+1}.  {y["title"]}'        
        msgs.insert(END, "         "+news_title)
        if x+1 <= 5:        
            speak(str(num[x])+', '+y["title"])

def SNews():
    # getting head lines
    top_headlines = newsapi.get_top_headlines(category='science',country='in')
    
    # creating list
    articles = top_headlines['articles']
    if len(articles) < 10 and len(articles) > 0:
        speak("Not much news today") 
    elif len(articles) == 0:
        speak("No news today related to ")
    else:
        pass
    # speaking and show headline in chat
    msgs.insert(END, " SYSMS : Today's science news are like this :-")
    speak("Today's science news are like this:")    
    for x,y in enumerate(articles):
        news_title = f'{x+1}.  {y["title"]}'        
        msgs.insert(END, "         "+news_title)
        if x+1 <= 5:        
            speak(str(num[x])+', '+y["title"])

def SpNews():
    # getting head lines
    top_headlines = newsapi.get_top_headlines(category='sports',country='in')
    
    # creating list
    articles = top_headlines['articles']
    if len(articles) < 10 and len(articles) > 0:
        speak("Not much news today") 
    elif len(articles) == 0:
        speak("No news today related to ")
    else:
        pass
    # speaking and show headline in chat
    msgs.insert(END, " SYSMS : Today's sports news are like this :-")
    speak("Today's sports news are like this:")    
    for x,y in enumerate(articles):
        news_title = f'{x+1}.  {y["title"]}'        
        msgs.insert(END, "         "+news_title)
        if x+1 <= 5:        
            speak(str(num[x])+', '+y["title"])

def BNews():
    # getting head lines
    top_headlines = newsapi.get_top_headlines(category='business',country='in')
    
    # creating list
    articles = top_headlines['articles']
    if len(articles) < 10 and len(articles) > 0:
        speak("Not much news today") 
    elif len(articles) == 0:
        speak("No news today related to ")
    else:
        pass
    # speaking and show headline in chat
    msgs.insert(END, " SYSMS : Today's business news are like this :-")
    speak("Today's business news are like this:")    
    for x,y in enumerate(articles):
        news_title = f'{x+1}.  {y["title"]}'        
        msgs.insert(END, "         "+news_title)
        if x+1 <= 5:        
            speak(str(num[x])+', '+y["title"])

def Tnews():
    # getting head lines
    top_headlines = newsapi.get_top_headlines(category='technology',country='in')
    
    # creating list
    articles = top_headlines['articles']
    if len(articles) < 10 and len(articles) > 0:
        speak("Not much news today") 
    elif len(articles) == 0:
        speak("No news today related to ")
    else:
        pass
    # speaking and show headline in chat
    msgs.insert(END, " SYSMS : Today's technology news are like this :-")
    speak("Today's technology news are like this:")    
    for x,y in enumerate(articles):
        news_title = f'{x+1}.  {y["title"]}'        
        msgs.insert(END, "         "+news_title)
        if x+1 <= 5:        
            speak(str(num[x])+', '+y["title"])

def MNews(topic):
    # getting head lines
    top_headlines = newsapi.get_top_headlines(q=topic)
    
    # creating list
    articles = top_headlines['articles']
    if len(articles) < 10 and len(articles) > 0:
        speak("Not much news today") 
    elif len(articles) == 0:
        speak("No news today related to ")
    else:
        pass
    # speaking and show headline in chat
    msgs.insert(END, " SYSMS : Today's news on" + topic +" are like this :-")
    speak(f"Today's news on {topic} are like this:")    
    for x,y in enumerate(articles):
        news_title = f'{x+1}.  {y["title"]}'        
        msgs.insert(END, "         "+news_title)
        if x+1 <= 5:        
            speak(str(num[x])+', '+y["title"])

# News Button

# Entertainment News
ENews_pic = Image.open('img/ENews.png')
resized = ENews_pic.resize((60,60), Image.ANTIALIAS)
ENews_NewPic = ImageTk.PhotoImage(resized)
ENews_label = Label(root, image=ENews_NewPic)
btn_ENews=Button(wrapper7,image=ENews_NewPic,relief=GROOVE, command=ENews).place(x=2.5,y=2,height=80,width=80)

# Health News
Hnews_pic = Image.open('img/Hnews.png')
resized = Hnews_pic.resize((60,60), Image.ANTIALIAS)
Hnews_NewPic = ImageTk.PhotoImage(resized)
Hnews_label = Label(root, image=Hnews_NewPic)
btn_Hnews=Button(wrapper7,image=Hnews_NewPic,relief=GROOVE, command=Hnews).place(x=82.5,y=2,height=80,width=80)

# Science News
SNews_pic = Image.open('img/SNews.png')
resized = SNews_pic.resize((60,60), Image.ANTIALIAS)
SNews_NewPic = ImageTk.PhotoImage(resized)
SNews_label = Label(root, image=SNews_NewPic)
btn_SNews=Button(wrapper7,image=SNews_NewPic,relief=GROOVE, command=SNews).place(x=162.5,y=2,height=80,width=80)

# Sports News
SpNews_pic = Image.open('img/SpNews.png')
resized = SpNews_pic.resize((60,60), Image.ANTIALIAS)
SpNews_NewPic = ImageTk.PhotoImage(resized)
SpNews_label = Label(root, image=SpNews_NewPic)
btn_SpNews=Button(wrapper7,image=SpNews_NewPic,relief=GROOVE, command=SpNews).place(x=2.5,y=82,height=80,width=80)

# Business News
BNews_pic = Image.open('img/BNews.png')
resized = BNews_pic.resize((60,60), Image.ANTIALIAS)
BNews_NewPic = ImageTk.PhotoImage(resized)
BNews_label = Label(root, image=BNews_NewPic)
btn_BNews=Button(wrapper7,image=BNews_NewPic,relief=GROOVE, command=BNews).place(x=82.5,y=82,height=80,width=80)

# Tech News
Tnews_pic = Image.open('img/Tnews.png')
resized = Tnews_pic.resize((60,60), Image.ANTIALIAS)
Tnews_NewPic = ImageTk.PhotoImage(resized)
Tnews_label = Label(root, image=Tnews_NewPic)
btn_Tnews=Button(wrapper7,image=Tnews_NewPic,relief=GROOVE, command=Tnews).place(x=162.5,y=82,height=80,width=80)

# tic tac toe game
statement = "O Match Draw"
winner = False
count = 0
def tttgame():
    msgs.insert(END, " SYSMS : Playing Tic Tac Toe...")        
    speak("Initializing, Opening Tic Tac Toe, Let's play")
    win = Tk()
    win.title('Tic-Tac-Toe Powered by S.Y.S.M.S.')

    # check if someone won
    def checkifwon():
        global winner, statement, count
        winner = False

        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            b1.config(bg="light green")
            b2.config(bg="light green")
            b3.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS!\nYou WIN!!!")
            statement = "Congrats You win"
            count = 0
            disable_all_buttons()        
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1.config(bg="light green")
            b5.config(bg="light green")
            b9.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS!\nYou WIN!!!")
            statement = "Congrats You win"
            count = 0
            disable_all_buttons()        
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3.config(bg="light green")
            b5.config(bg="light green")
            b7.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS!\nYou WIN!!!")
            statement = "Congrats You win"
            count = 0
            disable_all_buttons()        
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4.config(bg="light green")
            b5.config(bg="light green")
            b6.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS!\nYou WIN!!!")
            statement = "Congrats You win"
            count = 0
            disable_all_buttons()        
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7.config(bg="light green")
            b8.config(bg="light green")
            b9.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS!\nYou WIN!!!")
            statement = "Congrats You win"
            count = 0
            disable_all_buttons()        
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b1.config(bg="light green")
            b4.config(bg="light green")
            b7.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS!\nYou WIN!!!")
            statement = "Congrats You win"
            count = 0
            disable_all_buttons()        
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2.config(bg="light green")
            b5.config(bg="light green")
            b8.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS!\nYou WIN!!!")
            statement = "Congrats You win"
            count = 0
            disable_all_buttons()        
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b6.config(bg="light green")
            b3.config(bg="light green")
            b9.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS!\nYou WIN!!!")
            statement = "Congrats You win"
            count = 0
            disable_all_buttons()        
    # Cheak for O
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            b1.config(bg="light green")
            b2.config(bg="light green")
            b3.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","OOPs!\nSYSMS WIN!!!")
            statement = "Woohoo! I Won"
            count = 0
            disable_all_buttons()
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.config(bg="light green")
            b5.config(bg="light green")
            b9.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","OOPs!\nSYSMS WIN!!!")
            statement = "Woohoo! I Won"
            count = 0
            disable_all_buttons()
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3.config(bg="light green")
            b5.config(bg="light green")
            b7.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","OOPs!\nSYSMS WIN!!!")
            statement = "Woohoo! I Won"
            count = 0
            disable_all_buttons()
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.config(bg="light green")
            b5.config(bg="light green")
            b6.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","OOPs!\nSYSMS WIN!!!")
            statement = "Woohoo! I Won"
            count = 0
            disable_all_buttons()
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.config(bg="light green")
            b8.config(bg="light green")
            b9.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","OOPs!\nSYSMS WIN!!!")
            statement = "Woohoo! I Won"
            count = 0
            disable_all_buttons()
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1.config(bg="light green")
            b4.config(bg="light green")
            b7.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","OOPs!\nSYSMS WIN!!!")
            statement = "Woohoo! I Won"
            count = 0
            disable_all_buttons()
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.config(bg="light green")
            b5.config(bg="light green")
            b8.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","OOPs!\nSYSMS WIN!!!")
            statement = "Woohoo! I Won"
            count = 0
            disable_all_buttons()
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b6.config(bg="light green")
            b3.config(bg="light green")
            b9.config(bg="light green")
            winner = True
            messagebox.showinfo("Tic Tac Toe","OOPs!\nSYSMS WIN!!!")
            statement = "Woohoo! I Won"
            count = 0
            disable_all_buttons()
        # tie condition
        if count == 9 and winner == False:
            messagebox.showinfo("Tic Tac Toe","It's A Tie!")
            statement = "OH! Match Draw"
            count = 0
            disable_all_buttons()  


    def disable_all_buttons():
        global statement
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        msgs.insert(END, " SYSMS : "+statement)        
        speak(statement)
        # print(statement)

    # Button Clicked Function

    def b_click(b_1,b_2,b_3,b_4,b_5,b_6,b_7,b_8,b_9):
        global count, winner
        if b_1["text"] == " ":
            b_1["text"] = "X"
            # print(b_1["text"])
            count += 1
            checkifwon()
            if winner == False and count<9:
                b_list = [b_2,b_3,b_4,b_5,b_6,b_7,b_8,b_9]
                while(True):            
                    choice = random.choice(b_list)
                    if choice["text"] == " ":
                        choice["text"] = "O"
                        # print(choice["text"])
                        count += 1
                        checkifwon()
                        break
                    else:
                        continue
        else:
            messagebox.showerror("Tic Tac Toe","Hey! That place has already been filled\nPick another place...")

    b1 = Button(win,text=" ",font=("Helvetica", 20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b1,b2,b3,b4,b5,b6,b7,b8,b9))
    b2 = Button(win,text=" ",font=("Helvetica", 20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b2,b1,b3,b4,b5,b6,b7,b8,b9))
    b3 = Button(win,text=" ",font=("Helvetica", 20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b3,b1,b2,b4,b5,b6,b7,b8,b9))

    b4 = Button(win,text=" ",font=("Helvetica", 20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b4,b1,b2,b3,b5,b6,b7,b8,b9))
    b5 = Button(win,text=" ",font=("Helvetica", 20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b5,b1,b2,b3,b4,b6,b7,b8,b9))
    b6 = Button(win,text=" ",font=("Helvetica", 20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b6,b1,b2,b3,b4,b5,b7,b8,b9))

    b7 = Button(win,text=" ",font=("Helvetica", 20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b7,b1,b2,b3,b4,b5,b6,b8,b9))
    b8 = Button(win,text=" ",font=("Helvetica", 20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b8,b1,b2,b3,b4,b5,b6,b7,b9))
    b9 = Button(win,text=" ",font=("Helvetica", 20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b9,b1,b2,b3,b4,b5,b6,b7,b8))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    win.mainloop()


# quick icon access
wrapper9 = Frame(root)
wrapper9.place(x=785,y=525,height=185,width =250)


# funtion for buttons
def mail():
    subprocess.run("start outlookmail:", shell=True)

def vs():
    subprocess.run("code", shell=True)

def ttt():
    tttgame()

def lpu():
    webbrowser.open("https://ums.lpu.in/lpuums/")

# quick buttons
lpu_pic = Image.open('img/lpu.png')
resized = lpu_pic.resize((60,60), Image.ANTIALIAS)
lpu_NewPic = ImageTk.PhotoImage(resized)
lpu_label = Label(root, image=lpu_NewPic)
btn_lpu=Button(wrapper9,image=lpu_NewPic,relief=GROOVE, command=lpu).place(x=1,y=1,height=80,width=80)

vs_pic = Image.open('img/vs.png')
resized = vs_pic.resize((60,60), Image.ANTIALIAS)
vs_NewPic = ImageTk.PhotoImage(resized)
vs_label = Label(root, image=vs_NewPic)
btn_vs=Button(wrapper9,image=vs_NewPic,relief=GROOVE, command=vs).place(x=81,y=1,height=80,width=80)

ttt_pic = Image.open('img/tttgame.png')
resized = ttt_pic.resize((60,60), Image.ANTIALIAS)
ttt_NewPic = ImageTk.PhotoImage(resized)
ttt_label = Label(root, image=ttt_NewPic)
btn_ttt=Button(wrapper9,image=ttt_NewPic,relief=GROOVE, command=ttt).place(x=81,y=81,height=80,width=80)

mail_pic = Image.open('img/mail.png')
resized = mail_pic.resize((60,60), Image.ANTIALIAS)
mail_NewPic = ImageTk.PhotoImage(resized)
mail_label = Label(root, image=mail_NewPic)
btn_mail=Button(wrapper9,image=mail_NewPic,relief=GROOVE, command=mail).place(x=1,y=81,height=80,width=80)


# Quick Acess box
wrapper8 = LabelFrame(root, text ="Quick Acess Powered by S.Y.S.M.S.")
wrapper8.place(x=520,y=695,height=100,width=448)

# icon function
def snote():
    subprocess.run("explorer.exe shell:appsFolder\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App", shell=True)

def calc():
    subprocess.run("calc", shell=True)

def cpanel():
    subprocess.run("control", shell=True)

def exp():
    subprocess.run("explorer", shell=True)

def npad():
    subprocess.run("notepad", shell=True)

def seti():
    subprocess.run("start ms-settings:", shell=True)

def go():
    webbrowser.open("https://www.google.com/")

def ins():
    webbrowser.open("https://www.instagram.com/")

def fa():
    webbrowser.open("https://www.facebook.com/")

def li():
    webbrowser.open("https://www.linkedin.com/feed/")

def tw():
    webbrowser.open("https://twitter.com/home")

def yt():
    webbrowser.open("https://www.youtube.com/")


def dx():
    subprocess.run("dxdiag", shell=True)

def mus():
    subprocess.run("start mswindowsmusic:", shell=True)

def cam():
    subprocess.run("start microsoft.windows.camera:", shell=True)

def gal():
    subprocess.run("start ms-photos:", shell=True)

def map_():
    subprocess.run("start ms-drive-to:", shell=True)

def wiki():
    webbrowser.open("https://www.wikipedia.org/")

def irctc():
    webbrowser.open("https://www.irctc.co.in/")

def dom():
    webbrowser.open("https://www.dominos.co.in/")

def fli():
    webbrowser.open("https://www.flipkart.com/")

def zom():
    webbrowser.open("https://www.zomato.com/")

# icons
snote_pic = Image.open('img/snote.png')
resized = snote_pic.resize((30,30), Image.ANTIALIAS)
snote_NewPic = ImageTk.PhotoImage(resized)
snote_label = Label(root, image=snote_NewPic)
btn_snote=Button(wrapper8,image=snote_NewPic,borderwidth=0, command=snote).place(x=2.5,y=0.5,height=40,width=40)

calc_pic = Image.open('img/calc.png')
resized = calc_pic.resize((30,30), Image.ANTIALIAS)
calc_NewPic = ImageTk.PhotoImage(resized)
calc_label = Label(root, image=calc_NewPic)
btn_calc=Button(wrapper8,image=calc_NewPic,borderwidth=0, command=calc).place(x=82.5,y=0.5,height=40,width=40)

cpanel_pic = Image.open('img/cpanel.png')
resized = cpanel_pic.resize((30,30), Image.ANTIALIAS)
cpanel_NewPic = ImageTk.PhotoImage(resized)
cpanel_label = Label(root, image=cpanel_NewPic)
btn_cpanel=Button(wrapper8,image=cpanel_NewPic,borderwidth=0, command=cpanel).place(x=162.5,y=0.5,height=40,width=40)

exp_pic = Image.open('img/exp.png')
resized = exp_pic.resize((30,30), Image.ANTIALIAS)
exp_NewPic = ImageTk.PhotoImage(resized)
exp_label = Label(root, image=exp_NewPic)
btn_exp=Button(wrapper8,image=exp_NewPic,borderwidth=0, command=exp).place(x=42.5,y=0.5,height=40,width=40)

npad_pic = Image.open('img/npad.png')
resized = npad_pic.resize((30,30), Image.ANTIALIAS)
npad_NewPic = ImageTk.PhotoImage(resized)
npad_label = Label(root, image=npad_NewPic)
btn_npad=Button(wrapper8,image=npad_NewPic,borderwidth=0, command=npad).place(x=122.5,y=0.5,height=40,width=40)

seti_pic = Image.open('img/seti.png')
resized = seti_pic.resize((30,30), Image.ANTIALIAS)
seti_NewPic = ImageTk.PhotoImage(resized)
seti_label = Label(root, image=seti_NewPic)
btn_seti=Button(wrapper8,image=seti_NewPic,borderwidth=0, command=seti).place(x=202.5,y=0.5,height=40,width=40)

dx_pic = Image.open('img/dx.png')
resized = dx_pic.resize((30,30), Image.ANTIALIAS)
dx_NewPic = ImageTk.PhotoImage(resized)
dx_label = Label(root, image=dx_NewPic)
btn_dx=Button(wrapper8,image=dx_NewPic,borderwidth=0, command=dx).place(x=242.5,y=0.5,height=40,width=40)

mus_pic = Image.open('img/mus.png')
resized = mus_pic.resize((30,30), Image.ANTIALIAS)
mus_NewPic = ImageTk.PhotoImage(resized)
mus_label = Label(root, image=mus_NewPic)
btn_mus=Button(wrapper8,image=mus_NewPic,borderwidth=0, command=mus).place(x=282.5,y=0.5,height=40,width=40)

cam_pic = Image.open('img/cam.png')
resized = cam_pic.resize((30,30), Image.ANTIALIAS)
cam_NewPic = ImageTk.PhotoImage(resized)
cam_label = Label(root, image=cam_NewPic)
btn_cam=Button(wrapper8,image=cam_NewPic,borderwidth=0, command=cam).place(x=322.5,y=0.5,height=40,width=40)

gal_pic = Image.open('img/gal.png')
resized = gal_pic.resize((30,30), Image.ANTIALIAS)
gal_NewPic = ImageTk.PhotoImage(resized)
gal_label = Label(root, image=gal_NewPic)
btn_gal=Button(wrapper8,image=gal_NewPic,borderwidth=0, command=gal).place(x=362.5,y=0.5,height=40,width=40)

map_pic = Image.open('img/map.png')
resized = map_pic.resize((30,30), Image.ANTIALIAS)
map_NewPic = ImageTk.PhotoImage(resized)
map_label = Label(root, image=map_NewPic)
btn_map=Button(wrapper8,image=map_NewPic,borderwidth=0, command=map_).place(x=402.5,y=0.5,height=40,width=40)

go_pic = Image.open('img/go.png')
resized = go_pic.resize((30,30), Image.ANTIALIAS)
go_NewPic = ImageTk.PhotoImage(resized)
go_label = Label(root, image=go_NewPic)
btn_go=Button(wrapper8,image=go_NewPic,borderwidth=0, command=go).place(x=2.5,y=40.5,height=40,width=40)

ins_pic = Image.open('img/ins.png')
resized = ins_pic.resize((30,30), Image.ANTIALIAS)
ins_NewPic = ImageTk.PhotoImage(resized)
ins_label = Label(root, image=ins_NewPic)
btn_ins=Button(wrapper8,image=ins_NewPic,borderwidth=0, command=ins).place(x=82.5,y=40.5,height=40,width=40)

fa_pic = Image.open('img/fa.png')
resized = fa_pic.resize((30,30), Image.ANTIALIAS)
fa_NewPic = ImageTk.PhotoImage(resized)
fa_label = Label(root, image=fa_NewPic)
btn_fa=Button(wrapper8,image=fa_NewPic,borderwidth=0, command=fa).place(x=162.5,y=40.5,height=40,width=40)

li_pic = Image.open('img/li.png')
resized = li_pic.resize((30,30), Image.ANTIALIAS)
li_NewPic = ImageTk.PhotoImage(resized)
li_label = Label(root, image=li_NewPic)
btn_li=Button(wrapper8,image=li_NewPic,borderwidth=0, command=li).place(x=42.5,y=40.5,height=40,width=40)

tw_pic = Image.open('img/tw.png')
resized = tw_pic.resize((30,30), Image.ANTIALIAS)
tw_NewPic = ImageTk.PhotoImage(resized)
tw_label = Label(root, image=tw_NewPic)
btn_tw=Button(wrapper8,image=tw_NewPic,borderwidth=0, command=tw).place(x=122.5,y=40.5,height=40,width=40)

yt_pic = Image.open('img/yt.png')
resized = yt_pic.resize((30,30), Image.ANTIALIAS)
yt_NewPic = ImageTk.PhotoImage(resized)
yt_label = Label(root, image=yt_NewPic)
btn_yt=Button(wrapper8,image=yt_NewPic,borderwidth=0, command=yt).place(x=202.5,y=40.5,height=40,width=40)

wiki_pic = Image.open('img/wiki.png')
resized = wiki_pic.resize((30,30), Image.ANTIALIAS)
wiki_NewPic = ImageTk.PhotoImage(resized)
wiki_label = Label(root, image=wiki_NewPic)
btn_wiki=Button(wrapper8,image=wiki_NewPic,borderwidth=0, command=wiki).place(x=242.5,y=40.5,height=40,width=40)

irctc_pic = Image.open('img/irctc.png')
resized = irctc_pic.resize((30,30), Image.ANTIALIAS)
irctc_NewPic = ImageTk.PhotoImage(resized)
irctc_label = Label(root, image=irctc_NewPic)
btn_irctc=Button(wrapper8,image=irctc_NewPic,borderwidth=0, command=irctc).place(x=282.5,y=40.5,height=40,width=40)

dom_pic = Image.open('img/dom.png')
resized = dom_pic.resize((30,30), Image.ANTIALIAS)
dom_NewPic = ImageTk.PhotoImage(resized)
dom_label = Label(root, image=dom_NewPic)
btn_dom=Button(wrapper8,image=dom_NewPic,borderwidth=0, command=dom).place(x=322.5,y=40.5,height=40,width=40)

fli_pic = Image.open('img/fli.png')
resized = fli_pic.resize((30,30), Image.ANTIALIAS)
fli_NewPic = ImageTk.PhotoImage(resized)
fli_label = Label(root, image=fli_NewPic)
btn_fli=Button(wrapper8,image=fli_NewPic,borderwidth=0, command=fli).place(x=362.5,y=40.5,height=40,width=40)

zom_pic = Image.open('img/zom.png')
resized = zom_pic.resize((30,30), Image.ANTIALIAS)
zom_NewPic = ImageTk.PhotoImage(resized)
zom_label = Label(root, image=zom_NewPic)
btn_zom=Button(wrapper8,image=zom_NewPic,borderwidth=0, command=zom).place(x=402.5,y=40.5,height=40,width=40)

# snake game

def snakegame():
    delay = 0.1

    # Score
    score = 0
    high_score = 0

    # Set up the screen
    wn = turtle.Screen()
    wn.title("Snake Game Powered by SYSMS")
    wn.bgcolor("#FFFF99")
    wn.setup(width=600, height=600)
    wn.tracer(0) # Turns off the screen updates

    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("circle")
    head.color("black")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"

    # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    colour_list=["red","blue","green","cyan","magenta"]
    colour = random.choice(colour_list)
    food.color(colour)
    food.penup()
    food.goto(0,100)

    segments = []

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Verdana", 24, "normal"))

    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

    # Main game loop
    while True:
        wn.update()

        # Check for a collision with the border
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Verdana", 24, "normal")) 


        # Check for a collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 10

            if score > high_score:
                high_score = score
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Verdana", 24, "normal")) 

        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()    

        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
            
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)
            
                # Clear the segments list
                segments.clear()

                # Reset the score
                score = 0

                # Reset the delay
                delay = 0.1
            
                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        time.sleep(delay)

    wn.mainloop()

# easter egg
tap = 0
def tap_SYSMS():
    global tap
    tap = tap + 1
    if tap < 5:
        temp = 5 - tap
        str_temp = str(temp)+' !'
        logoNo_label.config(text=str_temp)
    else:
        logoNo_label.config(text="0!!! Let's go...")
        tap = 0
        snakegame()    

def logo_reset():
    global tap
    tap = 0
    logoNo_label.config(text="")



# SYSMS LOGO
logo_pic = Image.open('img/logo.png')
resized = logo_pic.resize((575,575), Image.ANTIALIAS)
rotate = resized.rotate(0)
logo_NewPic = ImageTk.PhotoImage(rotate)
logo_label = Label(root, image=logo_NewPic)
btn_logo=Button(root,image=logo_NewPic,borderwidth=0, command=tap_SYSMS)
btn_logo.place(x=960,y=10,height=575,width=575)
logoNo_label = Button(root,text=' ',borderwidth=0,command=logo_reset)
logoNo_label.place(x=975, y=10)

# About SYSMS
about_f = Frame(root)
about_f.place(x=980,y=580,height=210,width=550)

# heading
about_lbl = Label(about_f,text="     S.Y.S.M.S.",font="Times 40 bold",wraplength=540)
about_lbl.pack()

# text matter
about_text = "SYSMS based fully on python. This is the project made by the students Sachin Kumar, Akshay Anand for K20GR whose faculty Dr. Dhanpratap Singh in Lovely Professional University. SYSMS - System Multitasking Servant. Let's Talk about Python - Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.  Python's generators are a great way to interleave running many processing loops in this approach.is great for writing asynchronous code, which rather than threading uses a single event loop to do work in small units. Because it is an interpreted language, it is often many times slower than compiled languages" 

# label
about_lbl = Label(about_f,text=about_text,wraplength=540)
about_lbl.pack()

# speak about SYSMS
def info_speak():
    speak(about_text)

# info button
info_pic = Image.open('img/info.png')
resized = info_pic.resize((60,60), Image.ANTIALIAS)
rotate = resized.rotate(0)
info_NewPic = ImageTk.PhotoImage(rotate)
info_label = Label(about_f, image=info_NewPic)
btn_info=Button(about_f,image=info_NewPic,borderwidth=0, command=info_speak)
btn_info.place(x=50 , y=0)

# creating a function
def enter_function(event):
    btn.invoke()

# going to bind root window with enter key...
root.bind('<Return>', enter_function)

# threding for refreshing progressbar
# udate for progressbar
val_cpu=0
val_ram=0
val_store=0
val_bat=0
def update():
    #cpu
    global val_cpu
    val_cpu = psutil.cpu_percent(interval=1)
    var_cpu.set(val_cpu)
    # print(val_cpu)
    # ram
    global val_ram
    val_ram = psutil.virtual_memory()[2]
    var_ram.set(val_ram)
    # print(val_ram)
    # storage
    global val_store
    val_store = psutil.disk_usage('/')[3]
    var_store.set(val_store)
    # print(val_store)
    # battery
    global val_bat
    battery = psutil.sensors_battery()
    val_bat = battery.percent
    var_bat.set(val_bat)
    # print(val_bat)

# second to hour conversion function
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

def repeatL():
    while True:                
        update()
        # for cpu
        Label(wrapper4,text="CPU Usages: "+str(val_cpu)).place(x=5)
        cpu_l = psutil.cpu_percent(interval=1,percpu=True)
        j = 0
        v=18
        h=5
        row=0
        for item in cpu_l:
            j = j + 1                        
            Label(wrapper4,text="CPU "+str(j)+" Usages: "+str(item)).place(x=h,y=v)
            v += 20
        # for ram
        Label(wrapper4,text="Ram Usages: "+str(val_ram)+" %").place(x=150)
        # for storage
        Label(wrapper4,text="Storage Usages: "+str(val_store)+" % | Total: "+str(psutil.disk_usage('/')[0]//1024//1024//1024)+" GB").place(x=150,y=46)
        Label(wrapper4,text="Used: "+str(psutil.disk_usage('/')[1]//1024//1024//1024)+" GB"+"Free: "+str(psutil.disk_usage('/')[2]//1024//1024//1024)+" GB").place(x=150,y=65)
        # for battery
        Label(wrapper4,text="Battery: "+str(val_bat)+" %").place(x=150,y=115)
        battery = psutil.sensors_battery()
        Label(wrapper4,text="time left").place(x=280,y=115)
        Label(wrapper4,text=str(secs2hours(battery.secsleft))).place(x=265,y=135)
        time.sleep(2)        

# threding for running parallely
t = threading.Thread(target=repeatL)
t.start()

root.mainloop()