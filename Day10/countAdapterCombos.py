
def count_downline(list_of_remaining_adapters, already_done, current_adapter):
    if not list_of_remaining_adapters:
        return 1
    elif already_done[current_adapter] >= 0:
        return already_done[current_adapter]
    else:
        this_count = 0
        potential_connecting = [x for x in list_of_remaining_adapters[:3] if (x - current_adapter) <= 3]
        lets_try_these = list_of_remaining_adapters.copy()
        for adapter_to_follow in potential_connecting:
            try:
                lets_try_these.remove(adapter_to_follow)
                this_count += count_downline(lets_try_these, already_done, adapter_to_follow)
            except:
                print("Tried to remove", adapter_to_follow, "from list:", lets_try_these)
        already_done[current_adapter] = this_count
        return this_count

with open('data') as my_data:
    adapters = [int(x) for x in my_data.read().splitlines()]

adapters.sort()
memoize = [-1]*adapters[-1]
print(count_downline(adapters, memoize, 0))
# print("There were", count_1s, "gaps of 1 jolt and", count_3s, "gaps of 3 jolts, whose product is", count_3s*count_1s)