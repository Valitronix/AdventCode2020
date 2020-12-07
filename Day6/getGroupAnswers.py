import string 

with open('data') as my_data:
    groups = my_data.read().split('\n\n')
count = 0
alphabet = list(string.ascii_lowercase)
for group in groups:
    questions = [0] * 26
    responses = group.replace('\n', '')
    for response in responses:
        questions[alphabet.index(response)] = 1

    count += sum(questions)

print(count)