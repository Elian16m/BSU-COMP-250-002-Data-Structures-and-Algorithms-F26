# Elian Martinez
# COMP 250-002
# Project 1

from collections import deque

'''
Step 1: Model the Data
Each alert is a dictionary with these keys:
• id (int)
• source_ip (str)
• description (str)
• severity (int from 1 to 5, where 5 is critical)
IDs are assigned automatically. Use a global counter that starts at 1 and increases by 1 every time
an alert is created. This counter is the only global variable you may use.
Whenever you display an alert anywhere in the program, use this format:
[ID 3] Severity 4 | 192.168.1.10 | Multiple failed login attempt
'''

alert_count = 1

def alert_function(source_ip, description, severity):
    global alert_count #this is telling python to use this variable instead of making it local.
    alert = { #this created a dictionary and it is taking the values we giving it.
        "id": alert_count,
        "source_ip": source_ip,
        "description": description,
        "severity": severity,
    }
    alert_count += 1 #this is adding 1 every time the function run
    return alert
    #this is returning the dictionary
def alert_format(alert):
    print(f"[ID {alert['id']}] Severity {alert['severity']} | {alert['source_ip']} | {alert['description']}")

def main_code(): #this is a function to call the main code that will show the result, i did it because it say we can only use one global variable which is alert count 
    a1 = alert_function("192.168.1.10", "Multiple failed login attempts", 4) #we adding this to the function and a1 will be a dictionary
    a2 = alert_function("554.332.2.8", "Multiple login attempts", 3)
    alert_format(a1) #we the function alert_format which give us the proper formatting for the alert
    alert_format(a2)

main_code()


'''
Step 2: Build the Queue (Pending Alerts)
Store pending alerts in a deque. Do not use a regular Python list for the queue.
• Alerts with severity 1 to 4 go to the back of the queue.
• Alerts with severity 5 go to the front of the queue.
• The analyst always works on the alert at the front of the queue.
A critical alert must be placed in the right spot at the moment it is added. Do not sort the queue
(no sort(), sorted(), or anything similar) and do not use a priority queue module.
Write a helper function that creates an alert, assigns its ID, and places it in the queue following
the rules above. Use this helper for option 1 of the menu, and also use it to load these 5 sample
alerts when the program starts:
("10.0.0.5", "Port scan detected", 2)
("192.168.1.10", "Multiple failed login attempts", 4)
("172.16.0.8", "Ransomware signature detected", 5)
("10.0.0.22", "Unusual outbound traffic", 3)
("192.168.1.45", "Expired SSL certificate", 1)
'''

