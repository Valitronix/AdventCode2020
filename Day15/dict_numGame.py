turns = 30000000
prev_idx = {} #[0] * turns # holds the index of the last time the number was said
prev_prev_idx = {} # [0] * turns # holds the index of the time before that
with open('data') as input_data:
    starting = input_data.read().split(',')
    for i, number in enumerate(starting):
        prev_idx[int(number)] = i + 1
        say = int(number)

for idx in range(i+2, turns+1):
    last = say # get the last number spoken
    try:
        say = prev_idx[last] - prev_prev_idx[last] #find the difference between the times it was said
    except: # if that was the first time it was said, prev_prev key would not exist
        say = 0 # so say 0
    try:
        prev_prev_idx[say] = prev_idx[say]
    except:
        pass
    prev_idx[say] = idx

print("The", turns, "th number in the game is", say)