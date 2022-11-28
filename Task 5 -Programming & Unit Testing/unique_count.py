# your code goes here
numbers = [4,5,6,8,5,3,1,5,3]


def get_unique_numbers(numbers):

    list_of_unique_numbers = []

    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return len(list_of_unique_numbers) 


print('unique_count', numbers , "-> ", get_unique_numbers(numbers))
