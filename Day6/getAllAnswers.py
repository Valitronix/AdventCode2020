import string 
alphabet = list(string.ascii_lowercase)

with open('data') as my_data:
    count = 0
    for group in my_data.read().split('\n\n'):
        questions = [0] * 26
        responses = group.split('\n') # each person's answers are a response
        for response in responses:
            for yes in response:
                questions[alphabet.index(yes)] += 1 
        group_yes = [1 for x in questions if x == len(responses)]
        # print(questions)
        # print(responses)
        # print(sum(group_yes))
        count += sum(group_yes)

    print(count)