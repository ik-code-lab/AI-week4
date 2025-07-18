# Write a function to sort a list of dictionaries by a specific key

def sort_dicts_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

def manual_sort_dicts_by_key(data, key):
    # Create a copy to avoid modifying original list
    sorted_data = data[:]
    
    # Use bubble sort for learning (not efficient)
    for i in range(len(sorted_data)):
        for j in range(len(sorted_data) - i - 1):
            if sorted_data[j][key] > sorted_data[j + 1][key]:
                # Swap if the current item is greater than the next
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
    
    return sorted_data

data = [
    {'name': 'Ade', 'age': 50},
    {'name': 'Grace', 'age': 45},
    {'name': 'Chuks', 'age': 55}
]

print("AI Generated Sort:", sort_dicts_by_key(data, 'age'))
print("Manual Sort:", manual_sort_dicts_by_key(data, 'age'))

