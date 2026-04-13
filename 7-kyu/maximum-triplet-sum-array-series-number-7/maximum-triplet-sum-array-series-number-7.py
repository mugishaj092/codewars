def max_tri_sum(numbers):
    new_set = list(set(numbers))
    new_set.sort(key= lambda x: -x)
    return sum(new_set[:3])