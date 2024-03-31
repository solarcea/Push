import time
from win10toast import ToastNotifier

x = time = 0
n = ToastNotifier()

amount = int(input("Type in how often you want notifications (minutes): "))
time = amount * 60         #making it into minutes
title = str(input("Type in your title: "))
msg = str(input("Type in your message: "))
dur = int(input("Type in how long you want to see it (seconds): "))
cycle = int(input("Type in how many times you want it to proc: "))

n.show_toast(title, msg, duration = dur)

while x < cycle:
    time.sleep(t)
    n.show_toast(title, msg, duration = dur)
    x += 1
time.sleep(t+1)
n.show_toast("Done", duration = 5)
