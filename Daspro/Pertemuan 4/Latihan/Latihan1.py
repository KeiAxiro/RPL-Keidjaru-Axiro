numbers = [10, 20, 20, 30, 40, 50, 50, 60]

# menghapus duplikasi dengan mengubah ke set
unique_numbers = set(numbers)

# sort
unique_numbers.sort(key=numbers.index)

print(unique_numbers)