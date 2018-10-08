#THIS SCRIPT WILL FIND THE BEST POSSIBLE COMBINATION IN PRODUCTION LINE
#DEPENDANT ON WINMARGIN AND YOUR FITTING ASSEMBLER TIMES

from list import *
""" LIST VARIABLES
time = The time each step takes to complete
step = The name of each step
amount = the amount of times the time has been to divided to comply with the winmargin
dict = a dictionary of time and step

A list of the steps as variables which equal the time they take """

smalltime = 60 #This is the step with the smallest time to complete
winmargin = 13 # how over or under the smallest time can be
smalltimeamount = 1 #assuming how many smalltime machines there are
amountlimit = 300 #how many is too many before giving up
for i in range(0,len(time)):#This finds the smallest time
  if time[i] < smalltime:
    smalltime = time[i]
print("Smallest time is " +str(smalltimeamount) + " of " + str(step[i]) + " with a time of: " + str(smalltime/smalltimeamount) )#printing the smallest time


for i in range(0, len(time)):
  while time[i]/amount[i] <= (smalltime/smalltimeamount)-winmargin or time[i]/amount[i] >= (smalltime/smalltimeamount)+winmargin:
  #Test every time in the list to see if it is close enough to the smalltime
    amount[i] += 1 #add one to amount to divide it more
  print(step[i] + " Divided by " + str(amount[i]) + " makes " + str(int(time[i]/amount[i])) + ", Bottleneck: " + "%.2f" % (time[i]/amount[i] - smalltime/smalltimeamount))
  if amount[i] >= amountlimit:
    print("AMOUNT LIMIT REACHED")
    break
