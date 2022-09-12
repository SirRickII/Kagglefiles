def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
        
    return "{:.2f}".format(num)

def round_to_two_places2(num):

    return round(num, 2)

print(round_to_two_places(3.14159))
print(round_to_two_places2(3.14159))