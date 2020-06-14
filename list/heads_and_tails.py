import random

def coin_flip(number_of_flips):
    """Simulates the flip of a coin. Heads - H or Tails - T"""
    heads = 'H'
    tails = 'T'
    num_heads = 0
    num_tails = 0
    outcome_list = []
    for flips in range(number_of_flips):
        outcome = random.randint(0, 1)
        if outcome == 0:
            num_heads += 1
            outcome_list.append(heads)
            return f"{heads}: {num_heads}"
        elif outcome == 1:
            num_tails += 1
            outcome_list.append(tails)
            return f"{tails}: {num_tails}"
        
        
    return(outcome_list)


print(coin_flip(100))