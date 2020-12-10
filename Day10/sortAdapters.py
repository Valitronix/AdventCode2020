with open('data') as my_data:
    adapters = [int(x) for x in my_data.read().splitlines()]

adapters.sort()
adapters.insert(0,0)
count_3s = 1
 #the last jump is always +3
count_1s = 0
for index, adapter in enumerate(adapters[1:]):
    if adapter - adapters[index] == 3:
        count_3s += 1
    elif adapter - adapters[index] == 1:
        count_1s += 1
    else:
        print("Something funny here, one adapter is", adapters[index], "jolts and the next is", adapter, "jolts")

print("There were", count_1s, "gaps of 1 jolt and", count_3s, "gaps of 3 jolts, whose product is", count_3s*count_1s)