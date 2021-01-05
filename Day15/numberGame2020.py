turns = 30000000
prev_idx = [0] * turns # holds the index of the last time the number was said
prev_prev_idx = [0] * turns # holds the index of the time before that
with open('testData1') as input_data:
    starting = input_data.read().split(',')
    for idx, number in enumerate(starting):
        prev_idx[int(number)] = idx + 1
        say = int(number)
idx += 1

while idx <= turns-1:
    last = say # get the last number spoken
    if prev_prev_idx[last] == 0: # if that was the first time it was said, prev_prev would still be 0
        say = 0 # so say 0
    else: # otherwise the number was said before
        say = prev_idx[last] - prev_prev_idx[last] #find the difference between the times it was said
    prev_prev_idx[say] = prev_idx[say]
    prev_idx[say] = idx + 1
    idx += 1

print("The 2020th number in the game is", say)