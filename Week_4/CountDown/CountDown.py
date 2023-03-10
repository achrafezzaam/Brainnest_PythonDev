from tkinter import *
from tkinter import ttk
import time

class CountDown:
    def __init__(self,hours:int=0,minutes:int=0,seconds:int=0) -> None:
        self.timer = [seconds,minutes,hours]
        self.on_off = True

    def decrement_timer(self,index): # Decrement the timer parameter by one each time it's called
        if index <= (len(self.timer)-1):
            if self.timer[index] > 0:
                self.timer[index] -= 1
            elif self.timer[index+1] > 0:
                self.timer[index] = 59
                self.decrement_timer(index+1) # a recursion call when the value of seconds or minutes in the timer parameter equals to 0
            else:
                self.on_off = False # set the on_off parameter value to False when the timer parameter value is equal to [0,0,0]

    def countdown(self): # only executes when the timer parameter is not equal to [0,0,0]
        if self.on_off:
            self.decrement_timer(0)
            return self.on_off

class GUI:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Countdown App")
        self.frm1 = ttk.Frame(self.root)
        self.frm1.grid(padx=60,pady=30)
        self.frm2 = ttk.Frame(self.root)
        self.frm2.grid(padx=60,pady=30)
        self.countdown = None
        self.BuildGUI()

    def refresher(self, field): # refresh the timer display
        x = self.countdown.countdown()
        formated_count = "{} : {} : {}".format(self.countdown.timer[2],self.countdown.timer[1],self.countdown.timer[0])
        field.set(formated_count)
        if x:
            self.frm2.after(1000, self.refresher, field)
    
    def BuildGUI(self):
        def increment(field,max=60): # increment the labels value by one. It also loops back when the label's value gets to the maximum value
            value = int(field.get())
            if value < max:
                field.set(value+1)
            else:
                field.set(0)

        def decrement(field,max=60): # decrement the labels value by one. It also loops back when the label's value gets to the minimum value
            value = int(field.get())
            if value > 0:
                field.set(value-1)
            else:
                field.set(max)
        
        def start_countdown(): # starts the countdown when the start button is pressed 
            hours = hours_label.get()
            minutes = minutes_label.get()
            seconds = seconds_label.get()
            self.countdown = CountDown(hours,minutes,seconds)
            self.refresher(countdown)
        
        # Hours field and buttons
        hours_label = IntVar()
        ttk.Button(self.frm1, text="+", width=14, command=lambda:increment(hours_label,24)).grid(column=0, row=0)
        ttk.Label(self.frm1,anchor='center', width=14, textvariable=hours_label).grid(column=0, row=1)
        ttk.Button(self.frm1, text="-", width=14, command=lambda:decrement(hours_label,24)).grid(column=0, row=2)
        
        # Minutes field and buttons
        minutes_label = IntVar()
        ttk.Button(self.frm1, text="+", width=14, command=lambda:increment(minutes_label)).grid(column=1, row=0)
        ttk.Label(self.frm1,anchor='center', width=14, textvariable=minutes_label).grid(column=1, row=1)
        ttk.Button(self.frm1, text="-", width=14, command=lambda:decrement(minutes_label)).grid(column=1, row=2)
        
        # Seconds field and buttons
        seconds_label = IntVar()
        ttk.Button(self.frm1, text="+", width=14, command=lambda:increment(seconds_label)).grid(column=2, row=0)
        ttk.Label(self.frm1,anchor='center', width=14, textvariable=seconds_label).grid(column=2, row=1)
        ttk.Button(self.frm1, text="-", width=14, command=lambda:decrement(seconds_label)).grid(column=2, row=2)
        
        # Countdown display and start button
        countdown = StringVar()
        ttk.Button(self.frm2, text="Start", width=14, command=start_countdown).grid(column=1, row=0)
        ttk.Label(self.frm2,anchor='center', width=14, textvariable=countdown, font=('Times',20)).grid(column=1, row=1, pady=20)
        
        self.root.mainloop()

test = GUI()