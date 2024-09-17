def remove_even_numbers(input_list):
    result_list = [num for num in input_list if num % 2 != 0]
    return result_list

def remove_short_strings(input_list, min_length=5):
    result_list = [string for string in input_list if len(str(string)) >= min_length]
    return result_list


numbers = [int(x) for x in input("Enter a list of numbers (space-separated): ").split()]


words = input("Enter a list of strings (comma-separated): ").split(',')


result_even = remove_even_numbers(numbers)
print("List after removing even numbers:", result_even)

result_short = remove_short_strings(words)
print("List after removing short strings:", result_short)


