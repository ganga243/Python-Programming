#1. map->The map() function applies a function to every item in a collection.
# map(function, iterable)
#2. filter()->The filter() function is used to filter items based on a condition.
# filter(function, iterable):(condition satify cheyithu varunnath filter object)
# condition satify cheyunna element matharame return cheyyathollu

# reduce()-->The reduce() function reduces all items in a collection to a single value.
# package ->nammaku venda code code ullath
# Reduce(function, iterable)

from functools import reduce

num = [45, 2, 4, 6, 5, 8, 44, 6, 55]

squared_numbers = map(lambda x: x * x, num)
even_numbers = filter(lambda x: x % 2 == 0, num)
number_sum = reduce(lambda x, y: x + y, num)

print(list(squared_numbers))
print(list(even_numbers))
print(number_sum)


# function file store cheyunnath->modulues