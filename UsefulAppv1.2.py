#Imports

from tkinter import *
import os

#Objects and Variables
def networkscanner(): #Comment it if you do not need it and credit to geeksforgeeks.org
    import scapy.all as scapy 

    request = scapy.ARP() 

    request.pdst = 'x'
    broadcast = scapy.Ether() 

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'

    request_broadcast = broadcast / request 
    clients = scapy.srp(request_broadcast, timeout = 1)[0]
    for element in clients: 
        print(element[1].psrc + "    " + element[1].hwsrc)

x = os.getlogin()
#Window
window = Tk()
window.title("UsefulApp v1.2")
#Widgets

#Labels

Label(window,padx=10,pady=13).pack()
Label(window,text="Hello " + x + '!').pack()
Label(window,text="Network Scanner").pack()

#Buttons

Button(window,text = "Network Scanner",command = networkscanner).pack()

#Loop (Do Not Remove!)

window.mainloop()
