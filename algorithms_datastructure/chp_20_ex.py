import math

# exercise 1 
# run time should be O(n+m)

basketball_players = [{'first_name':'jill', 'last_name': 'huang', 'team': 'gators'},
                    {'first_name':'janko', 'last_name': 'barton', 'team': 'sharks'},
                    {'first_name':'wanda', 'last_name': 'vakulskas', 'team': 'sharks'},
                    {'first_name':'jill', 'last_name': 'moloney', 'team': 'gators'}, 
                    {'first_name':'luuk', 'last_name': 'watkins', 'team': 'gators'}, 
                    ]

football_players = [{'first_name':'hanzla', 'last_name': 'radosti', 'team': '32ers'},
                    {'first_name':'tina', 'last_name': 'watkins', 'team': 'barleycorns'}, 
                    {'first_name':'alex', 'last_name': 'patel', 'team': '32ers'}, 
                    {'first_name':'jill', 'last_name': 'huang', 'team': 'barleycorns'}, 
                    {'first_name':'wanda', 'last_name': 'vakulskas', 'team': 'barleycorns'}]

missing_integer_1 = [2,3,0,6,1,5]
missing_integer_2 = [8,2,3,9,4,7,5,0,6]

stock_predictions = [10,7,5,8,11,2,6]

greatest_number = [5, -10, -6, 9, 4]

temperature_readings = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]

longest_consecutive = [19,13,15,12,18,14,17,11]

def exercise_1(array_1, array_2)->list[str]:
    # create dict from first array
    dict_1 = {str(x.get('first_name') + " " + x.get('last_name')): True for x in array_1}

    # overlapped list
    overlapped = [str(x.get('first_name') + " " + x.get('last_name')) for x in array_2 if dict_1.get(str(x.get('first_name') + " " + x.get('last_name')))]
    
    return overlapped

def exercise_2(array)->int:
    # run time O(n)
    # array always counts from 0,1,2,...

    full_sum = sum(range(len(array) + 1))
    actual_sum = sum(array)

    return full_sum - actual_sum

def exercise_3(array)->int:
    # O(n)
    # greedy, if difference for next number is negative, current is next

    buy_price = array[0]
    max_profit = 0

    for price in array:
        if price - buy_price <= 0:
            buy_price = price    
        else:
            profit_current = price - buy_price 
            if profit_current > max_profit:
                max_profit = profit_current

    return max_profit

def exercise_4(array)->int:
    largest = [0,0]
    smallest = [0,0]
    
    for number in array:
        if number < 0:
            if number < smallest[0]:
                smallest[0] = number
            elif number < smallest[1]:
                smallest[1] = number
         
        if number > 0:
            if number > largest[0]:
                largest[0] = number
            elif number > largest[1]:
                largest[1] = number
    
    return max(math.prod(largest), math.prod(smallest))

def exercise_5(array:list[float])->list[float]:
    # O(n) for sort
    # temperature reading constrained between 97.0 to 99.0
    # decimal points never goes beyond the tenths place (0.9, 0.1) NOT (0.01 or 0.02)

    # use a hash/dict with all possible values from 97.0 to 99.0

    temp_range = {temp/10:0 for temp in range(970, 991, 1)}

    # loop through array to sort
    # count occurence
    for temperature in array:
        temp_range[temperature] += 1

    # create the sorted array from dict of counts
    sorted_temp = []
    for temperature in temp_range.keys():
        if temp_range.get(temperature) != 0:
            sorted_temp.append([temperature] * temp_range.get(temperature))

    # flatten
    sorted_temp = [x for sublist in sorted_temp for x in sublist]

    return sorted_temp

def exercise_6(array:list[int])->int:
    # O(n)
    # longest consecutive int
    # create dict for the numbers in array
    # for each number, if a smaller number (number-1) exists in the dict, skip
    # if no smaller, calculate longest increment

    longest_consecutive_ints = 0

    dict_lookup = {number: True for number in array}

    for num in array:
        # check if smaller doesn't exist
        if not dict_lookup.get(num - 1):
            # find longest consecutive
            current_longest_sequence = 0
            while dict_lookup.get(num + 1):
                current_longest_sequence += 1
                num += 1
                if current_longest_sequence > longest_consecutive_ints:
                    longest_consecutive_ints = current_longest_sequence

    return longest_consecutive_ints

if __name__== "__main__":
    response = exercise_1(basketball_players, football_players)
    
    missing = exercise_2(missing_integer_1)

    largest_profit = exercise_3(stock_predictions)

    largest_multiple = exercise_4(greatest_number)

    temp = exercise_5(temperature_readings)

    longest_consecutive_result = exercise_6(longest_consecutive)