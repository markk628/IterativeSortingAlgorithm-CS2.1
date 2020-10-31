import time

def is_sorted(items):
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            return False
    return True

def insertion_sort(items):
    # for i in range(len(items) - 1):
    #     for j in range(i + 1, len(items)):
    #         if items[i] > items[j]:
    #             items[i], items[j] = items[j], items[i]
    # return items
    while is_sorted(items) == False:
        first_index = 0
        second_index = 1
        if items[first_index] > items[second_index]:
            items[first_index], items[second_index] = items[second_index], items[first_index]
        if second_index < len(items) - 1:
            first_index += 1   
            second_index += 1
    return items   

start_time = time.time()
print(insertion_sort([9,4,17,2]))
print("%.10f seconds" % (time.time() - start_time))