# Elian Martinez
# COMP 250-002
# Project 1

from collections import deque

# step 1
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

#step 2
def adding_queue(queue, source_ip, description, severity):
    alert = alert_function(source_ip, description, severity)
    if severity == 5:
        queue.appendleft(alert) #this one will move the highest severity to the front
    else:
        queue.append(alert)

def main_code(): #this is a function to call the main code that will show the result, i did it because it say we can only use one global variable which is alert count 
    all_alerts = deque()#this create the deque which is empty

    # this are the 5 sample alerts, loaded with the helper
    adding_queue(all_alerts, "10.0.0.5", "Port scan detected", 2)
    adding_queue(all_alerts, "192.168.1.10", "Multiple failed login attempts", 4)
    adding_queue(all_alerts, "172.16.0.8", "Ransomware signature detected", 5)
    adding_queue(all_alerts, "10.0.0.22", "Unusual outbound traffic", 3)
    adding_queue(all_alerts, "192.168.1.45", "Expired SSL certificate", 1)

    for alert in all_alerts:
        alert_format(alert)
        
main_code()

