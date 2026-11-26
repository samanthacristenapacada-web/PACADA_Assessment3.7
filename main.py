# Assessment 3.7: Sorting Algorithms
# Name: Samantha Cristena Calvo Pacada

full_name = "Samantha Cristena Calvo Pacada"

unsorted_array = []

for letter in full_name:
    if letter.isalpha():
        letter = letter.upper()

        if letter not in unsorted_array:
            unsorted_array.append(letter)

sorted_array = unsorted_array.copy()

n = len(sorted_array)

for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_array[j] > sorted_array[j + 1]:
            sorted_array[j], sorted_array[j + 1] = (
                sorted_array[j + 1],
                sorted_array[j]
            )

print("Full Name:", full_name)
print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)
