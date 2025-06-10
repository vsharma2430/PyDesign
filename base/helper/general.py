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
    """Group consecutive numbers into ranges or single numbers.
    
    Args:
        numbers: List of integers
    Returns:
        List containing single numbers or [start, end] ranges
    """
    if not numbers:
        return []
    
    numbers = sorted(numbers, key=int)  # Ensure proper sorting for non-integer inputs
    result = []
    start = prev = numbers[0]
    
    for num in numbers[1:]:
        if num == prev + 1:
            prev = num
        else:
            result.append(start if start == prev else [start, prev])
            start = prev = num
    
    result.append(start if start == prev else [start, prev])
    return result

def format_consecutive_numbers(grouped_list):
    """Format grouped numbers into a string representation.
    
    Args:
        grouped_list: List of single numbers or [start, end] ranges
    Returns:
        Formatted string of numbers and ranges
    """
    def format_item(item):
        return f"{item[0]} To {item[1]}" if isinstance(item, list) else str(item)
    
    return " ".join(format_item(item) for item in grouped_list)