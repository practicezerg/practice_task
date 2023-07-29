"""You are given a positive integer arrivalTime denoting the arrival time of a train in hours, and another positive
integer delayedTime denoting the amount of delay in hours.
Return the time when the train will arrive at the station.
Note that the time in this problem is in 24-hours format."""
def findDelayedArrivalTime(arrivalTime,delayedTime):
    finish = arrivalTime + delayedTime
    if finish > 24:
        return finish - 24
    elif finish == 24:
        return 0
    else:
        return finish


arrivalTime,delayedTime = 15, 5
res = findDelayedArrivalTime(arrivalTime,delayedTime)
print(res)