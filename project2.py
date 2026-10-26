# Elian Martinez
# COMP 250-002
# Project 1

from collections import deque

# step 1
alert_count = 1

def alert_function(source_ip, description, severity):
    global alert_count #this is telling python to use this variable instead of making it local.
    alert = { #this created a dictionary, and it is taking the values we giving it.
        "id": alert_count,
        "source_ip": source_ip,
        "description": description,
        "severity": severity,
    }
    alert_count += 1 #this is adds 1 every time the function run.
    return alert
    #this is returning the dictionary.

def alert_format(alert): #this is another function, but it is just the formatting of the alert.
    print(f"[ID {alert['id']}] Severity {alert['severity']} | {alert['source_ip']} | {alert['description']}")

#step 2
def adding_queue(queue, source_ip, description, severity):
    alert = alert_function(source_ip, description, severity)
    if severity == 5:
        queue.appendleft(alert) #here we will move the highest severity to the front.
    else:
        queue.append(alert) #and with the else, the rest will go to the back.

# step 3
def solve_alert(queue, history): #this function checks the history of alerts.
    if len(queue) == 0:
        print("No pending alerts.")
        return
    alert = queue.popleft()   #this will take the alert from the front of the queue.
    history.append(alert)     #and here we push it onto the top of the stack.
    print("Resolved: ")
    alert_format(alert) #we call back the main format of it

def undo_alert(queue, history):
    if len(history) == 0:
        print("Nothing to undo.")
        return
    alert = history.pop()  #this will take the most recent alert off the top of the stack.
    queue.appendleft(alert) #and here we put it back at the front of the queue.
    print("Undone:")
    alert_format(alert)

# step 4
def search_alert(alerts, target_id, index):
    if index == len(alerts):#we used a base case. If index is the same as the length, we return None.
        return None
    #if the id is the same as the one we are looking for, we return that alert.
    if alerts[index]["id"] == target_id:
        return alerts[index]
    #if it is not this one, the function calls itself again with the next index, which is a recursive function
    return search_alert(alerts, target_id, index + 1)

def total_severity(alerts, index):
    if index == len(alerts): #we used another base case in this function. If the index is the same as the length, we return 0.
        return 0
    #this gets the severity of the current alert and adds it to the total of the rest of the alerts.
    return alerts[index]["severity"] + total_severity(alerts, index + 1)

# step 5
# each menu option has its own function, like a little menu.
def add_alert(queue):
    source_ip = input("Enter source IP: ")
    description = input("Enter description: ")
    severity = int(input("Enter severity (1-5): "))
    adding_queue(queue, source_ip, description, severity) #uses the function from step 2.
    print("Alert added.")

def view_next(queue):
    if len(queue) == 0:
        print("No pending alerts.")
        return
    alert_format(queue[0]) #queue[0] is the front, it looks at it.

def view_all(queue):
    if len(queue) == 0:
        print("No pending alerts.")
        return
    for alert in queue: #loops from front to bac.
        alert_format(alert)
    alerts_list = list(queue) #this uses recursion, so we're using a normal list.
    print("Total severity:", total_severity(alerts_list, 0))

def view_history(history):
    if len(history) == 0:
        print("No resolution history.")
        return
    x = len(history) - 1 #this gives the last index, which is the top of the stack.
    while x >= 0: #here we go down to 0 so it prints the most recent to oldest.
        alert_format(history[x]) #this one is reading alerts.
        x -= 1

def search_id(queue): #we searching for the IDs in this function.
    if len(queue) == 0:
        print("No pending alerts.")
        return
    target_id = int(input("Enter alert ID: "))
    alerts_list = list(queue)
    found = search_alert(alerts_list, target_id, 0)
    if found is None:
        print("Alert not found.")
    else:
        alert_format(found)

def show_menu(): #this is the menu that we get when we run the code.
    print()
    print("===== SOC ALERT TRIAGE CONSOLE =====")
    print("1. Add new alert")
    print("2. View next alert")
    print("3. Resolve next alert")
    print("4. Undo last resolution")
    print("5. View all pending alerts")
    print("6. View resolution history")
    print("7. Search alert by ID")
    print("8. Exit")

def main():
    alert_queue = deque() #we make queue and stack here
    resolved_stack = []  

    adding_queue(alert_queue, "10.0.0.5", "Port scan detected", 2)
    adding_queue(alert_queue, "192.168.1.10", "Multiple failed login attempts", 4)
    adding_queue(alert_queue, "172.16.0.8", "Ransomware signature detected", 5)
    adding_queue(alert_queue, "10.0.0.22", "Unusual outbound traffic", 3)
    adding_queue(alert_queue, "192.168.1.45", "Expired SSL certificate", 1)

    while True: #the menu keeps showing until the user picks 8
        show_menu()
        choice = input("Choose an option: ") 
        if choice == "1":
            add_alert(alert_queue)
        elif choice == "2":
            view_next(alert_queue)
        elif choice == "3":
            solve_alert(alert_queue, resolved_stack)
        elif choice == "4":
            undo_alert(alert_queue, resolved_stack)
        elif choice == "5":
            view_all(alert_queue)
        elif choice == "6":
            view_history(resolved_stack)
        elif choice == "7":
            search_id(alert_queue)
        elif choice == "8":
            print("Goodbye!")
            break #this is the stop of the program to exit it.
        else:
            print("Invalid option.")

main()

'''
Steps 6 & 7: I wasn't sure how to continue for step 6, 
so I will try to write what I will have done for these steps.

First, I will write a function with def get_int, 
this function works as an error catcher, and it only gives a number if it falls between low and high.
I will have a while loop so the user needs to enter the IP and the description.

Step 7: Time Complexity Analysis
1. Add a regular alert (severity 1 to 4):
O(1); it is just adding to the back of the deque, so it is constant

2. Add a critical alert (severity 5):
O(1); this is also just adding to the deque, so it is constant

3. Resolve the next alert:
O(1); This is removing from the deque, so it is constant.

4. Undo the last resolution:
O(1); This pops from the histoy os the list, so it is constant.

5. Search for an alert by ID:
O(n); This function has a loop to check the IDs.

6. If the queue were a regular Python list and you resolved alerts by removing the item at
index 0, what would the Big-O of resolving become, and why?:
O(n) because if the regular list is used, Python forces every single item to shift left.

7. Your recursive functions could have been written with loops. Give one reason a loop
might be the better choice in a real SOC tool that handles thousands of alerts:
Loops use a constant amount of memory, and recursive functions create a new stack every call,
wasting a lot of memory, and it can crash the program with an overflow error if it's too big.
'''