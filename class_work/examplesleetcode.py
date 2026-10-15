from collections import deque

def timeRequiredToBuy(tickets, k):
    q = deque(range(len(tickets)))
    time = 0

    while(True):
        person = q.popleft()
        tickets[person] -= 1
        time += 1

        if tickets[person] == 0 and person == k :
            return time
        if tickets[person] > 0:
            q.append(person)

tickets = [2,1,5,3,2]
k = 1

print(timeRequiredToBuy(tickets, k), "s")