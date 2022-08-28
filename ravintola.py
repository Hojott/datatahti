numberofcustomers = int(input())
customersinside = 0
customerenter = []
customerleave = []
customerids = []
customerstimetable = []

if numberofcustomers == 0:
    ans = 0
else: 
    for id in range (numberofcustomers):
        splitinput = input().split(' ')
        customerids.append(id)
        customerenter.append(int(splitinput[0]))
        customerleave.append(int(splitinput[1]))

    customerenter.sort()
    customerleave.sort()

    while len(customerenter) > 0:
        if customerenter[0] < customerleave[0]:
            customersinside = customersinside +1
            customerenter.pop(0)
        else:
            customersinside = customersinside -1
            customerleave.pop(0)
        customerstimetable.append(customersinside)  
#       <-- kestää liian kauan -->

    print(max(customerstimetable))