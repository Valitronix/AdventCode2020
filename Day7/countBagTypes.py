# get rules
rules = {}
with open('data') as my_data:
    for rule in my_data.read().splitlines():    # for each rule
        words = rule.split(" bags contain ")
        # add the containing bag as dict key
        # add the inside bags list of strings as value
        rules[words[0]] = [inside.replace("s, ", "").replace(", ", "") for inside in words[1].split(" bag") if len(inside) > 2]
        
# empty list of possible outer bags
outer_bags = set()
#empty list of checked outer bags
checked = set()
# add desired bag to transport to list of inner bags
inner_bags = set()
inner_bags.add('shiny gold')

# while there is a list of inner bags that is not empty
while len(inner_bags) > 0: 
    # remove (pop?) the inner bag off of the inner list
    lets_check = inner_bags.pop()
    if lets_check in checked:
        continue 
    checked.add(lets_check)
    # find the keys for which the inner bag is one of the values in the list
    for outside_bag in rules.keys():
        for inside_bag in rules[outside_bag]:
            if lets_check in inside_bag:
                # add those keys to inner bags AND outer bags
                outer_bags.add(outside_bag)
                inner_bags.add(outside_bag)

print(len(outer_bags))
