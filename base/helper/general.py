avg = lambda items : sum(items)/len(items)
closest_to = lambda lst,x : min(lst, key=lambda n: abs(n - x))

def get_closest_lower_value_then_higher_value(arr, target):
    """
    Find the closest value in arr that is lower than target.
    
    Args:
        arr (list): List of numbers
        target (float/int): Target value to compare against
    
    Returns:
        The closest value less than target, or None if no such value exists
    """
    if not arr:  # Check if list is empty
        return None
        
    lower_values = [x for x in arr if x < target]
    higher_values = [x for x in arr if x > target]
    
    if not lower_values:  # If no values are less than target
        return None
        
    return max(lower_values) if max(lower_values) != target else min(higher_values)

def group_consecutive_numbers(numbers):
    if not numbers:
        return []
    
    # Sort the list to ensure numbers are in order
    numbers = sorted(numbers)
    result = []
    start = numbers[0]
    prev = numbers[0]
    
    for num in numbers[1:]:
        if num == prev + 1:
            # Consecutive number found, update previous
            prev = num
        else:
            # Break in sequence, add the range or single number
            if start == prev:
                result.append(start)
            else:
                result.append([start, prev])
            start = num
            prev = num
    
    # Handle the last group or number
    if start == prev:
        result.append(start)
    else:
        result.append([start, prev])
    
    return result

def format_consecutive_numbers(grouped_list):
    formatted = [f"{start} To {end}" if isinstance(item, list) else str(item) for item, start, end in 
                [(item, item[0], item[1]) if isinstance(item, list) else (item, None, None) for item in grouped_list]]
    return " ".join(formatted)