# 1. Find the median value of a given list of numbers using a Python function.

def find_median(input_list):
    sorted_list = sorted(input_list)
    mid = len(sorted_list) // 2
    return (sorted_list[mid] + sorted_list[-mid-1]) / 2 if len(sorted_list) % 2 == 0 else sorted_list[mid]
my_list = [23, 12, 43, 14, 22, 54]
median_value = find_median(my_list)
print(median_value)



# 2. Get a list of all the keys in a given dictionary using a Python function.

def get_dictionary(input_dict):
    keys_list = list(input_dict.keys())

    return keys_list
my_dict = {"name": "Clarah", "age": 327, "city": "New York"}
dict_keys = get_dictionary(my_dict)
print(dict_keys) 



# 3. Filter a given list of numbers to return only the ones that are greater 
#than or equal to 10 using a Python function.
 
def filter(number_list):
    filtered_list = []
    
    for number in number_list:
        if number >= 10:
            filtered_list.append(number)
    return filtered_list

my_numbers = [5, 10, 9, 4, 16, 20, 25]
filtered_numbers = filter(my_numbers)
print(filtered_numbers)



# 4. Create a new list containing only the strings that start with the letter 
#"a" from a given list of strings using a Python function.

def filter(string):
    filtered = []
    for string in string:
        if string.startswith("a"):
            filtered.append(string)
    
    return filtered
strings = ["apple", "banana", "orange", "apricot", "pear"]
strng = filter(strings)
print(strng) 



# 5. Find the product of all the numbers in a given list of numbers using a Python function.
#multiply all numbers in list

def num_list(list) :
    prd = 1
    for x in list:
         prd = prd * x
    return prd
     

list1 = [11, 12, 4, 3]
print(list1)
print(num_list(list1))


                    #    SOME OF THE TAKEAWAY KEYS INCLUDES
# 1. Default Parameters: Default parameters can be used to provide a default value 
# for a parameter if the function is called without providing a value for that parameter.

# 2. Variable Arguments: The *args and **kwargs syntax can be used to specify variable-
# length argument lists. *args is used for non-keyword arguments, while **kwargs is used 
# for keyword arguments.

# 3. Recursion: Python functions can be recursive, meaning they can call themselves. 
# Recursion is often used to solve problems that can be broken down into smaller sub-problems.

