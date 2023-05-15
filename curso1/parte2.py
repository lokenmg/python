#-----------------------------------------------    1     -----------------------------------------------
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
          
    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num, 2)
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    pass
round_to_two_places(3.14159)

#-----------------------------------------------    2     -----------------------------------------------
print (round(3.141522229, -2))

#-----------------------------------------------    3     -----------------------------------------------
def to_smash(total_candies, friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between n friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % friends

to_smash(91)

# Check your answer
q3.check()