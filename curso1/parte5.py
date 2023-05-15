#-----------------------------------------------    1     -----------------------------------------------
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    n=0
    for num in nums:
        if ((num % 7) == 0):
            n=n+1
    if n>=1:
        return True
    else:
        return False
#-----------------------------------------------    2     -----------------------------------------------
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    nl=[]
    for li in L:
        if li>thresh:
            nl.append(True)
        else:
            nl.append(False)
        
    return nl
    pass

#-----------------------------------------------    3     -----------------------------------------------
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
    pass
#-----------------------------------------------    4     -----------------------------------------------
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    payouts = [play_slot_machine()-1 for i in range(n_runs)] 
    avg_payout = sum(payouts) / n_runs
    return avg_payout
    pass
print(estimate_average_slot_payout(100000000))