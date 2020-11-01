# -*- coding: utf-8 -*-

# Given a set of 𝑚 flights that the airline company must realize, determine the
# minimum number of planes that the company needs to purchase
#
# The airline may add unscheduled flights to move the airplanes around if
# that would reduce the total number of planes needed.

airtportNumber = 2
flightNumber = 2
inspectionTime = [1,1]

#On the 𝑖th line, The 𝑗th integer indicates the amount of time it takes to fly
#from airport 𝑖 to airport 𝑗. It takes no time to fly from an airport to itself.
#Note that the flight time from airport 𝑖 to 𝑗 is not necessarily the same as
#the flight time from airport 𝑗 to 𝑖.
flightMatrix = [[0,1],[1,0]]

#The next 𝑚 lines contain three space-separated integers, 𝑠, 𝑓, and 𝑡,
# indicating that a flight must start at airport 𝑠, end at airport 𝑓,
#and fly out from airport 𝑠 at exactly time 𝑡 heading directly to airport 𝑓.
flightPaths = [[1,2,1],[2,1,1]]
#Output a single positive integer indicating the minimum number of planes the
#airline company must purchase in order to realize the 𝑚 requested flights.

#planes having conditions
class Airplane:
    """docstring for airplane."""

    def __init__(self,airport, available, timetaken):
        self.airport = airport
        self.available = available
        self.timetaken = timetaken

def myFunc(e):
    return e[2]

def availablePlanes(planelist,airport):
    output = 0
    for i in range(0 , len(planelist) - 1):
        if planelist[i].available == True and (planelist[i].airport == -1 or planelist[i].airport == airport):
            planelist[i].airport = airport
            output = i
    return output

def planesFlyTicker(planelist):
    for i in range(0 , len(planelist)-1):
        if planelist[i].available == False:
            planelist[i].timetaken = planelist[i].timetaken -1
            if planelist[i].timetaken <= 0:
                planelist[i].timetaken = 0
                planelist[i].available = True
    pass

def flightsPending(flightlist,t):
    out = False
    for flight in flightlist:
        if flight[2] > t:
            out = True
    return out

def flightOptimizer(planelist,flightlist,t):
    for plane in planelist:
        if plane.available == True:
            

    pass

flightPaths.sort(key = myFunc)
p=Airplane(-1 , True , 0)
continuebool = True
planes = [Airplane(-1 , True , 0)]


t=0
while continuebool:
    planesFlyTicker(planes)
    t=t+1
    for path in flightPaths:
        #if there needs to be a flight
        if path[2] == t:
            #check if there are available flights
            currentPlane = availablePlanes(planes,path[0])

            # if a plane is found to be available already in the airport - Set in flight.
            if planes[currentPlane].airport == path[0] and planes[currentPlane].available == True:
                planes[currentPlane].airport =  path[1]
                planes[currentPlane].available = False
                planes[currentPlane].timetaken = flightMatrix[path[0]-1][path[1]-1]
            # if a plane is not found - Create a new plane
            else:
                planes.append(Airplane(path[1],False,flightMatrix[path[0]-1][path[1]-1]))
    pass
    continuebool = flightsPending(flightPaths,t)
pass

print(len(planes))






# for i in range(0,flightNumber-1):
#     if flightPaths[i][2] > max_time:
#         if flightPaths[i][2] = max_time:
#         max_time = flightPaths[i][2]
#         last_flight = i
#     pass
#
# last_flights = []
#
# for i in range(0,flightNumber-1):
#     if flightPaths[i][2] = max_time:
#         last_flights.append(i)
#
# for i in range(0,len(last_flights)-1)
#     flightMatrix[flightPaths[]]
