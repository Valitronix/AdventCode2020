# get rules
rules = {}
with open('data') as my_data:
    for rule in my_data.read().splitlines():    # for each rule
        words = rule.split(" bags contain ")
        # add the containing bag as dict key
        # add the inside bags list of strings as value
        rules[words[0]] = [inside.replace("s, ", "").replace(", ", "") for inside in words[1].split(" bag") if len(inside) > 2]
        
# empty list of possible outer bags
outer_bags = []
#empty list of checked outer bags
#checked = set()
# add desired bag to transport to list of inner bags
bag_count = 0
outer_bags.append('shiny gold')

# while there is a list of inner bags that is not empty
while len(outer_bags) > 0: 
    # remove (pop?) the inner bag off of the inner list
    lets_check = outer_bags.pop(0)
    print("Looking inside the ", lets_check)
    # If this section were necessary, we'd have infinite loops!
    # if lets_check in checked:
    #     continue 
    # checked.add(lets_check)

    # find the bags needed inside the current bag
    for inside_bag in rules[lets_check]:
        try:
            number = int(inside_bag[0])
            for i in range(number):
                outer_bags.append(inside_bag[2:])
            print("Found ", number, inside_bag[2:], "s inside this bag.")
        except:
            number = 0
        
        bag_count += number

print(bag_count)
