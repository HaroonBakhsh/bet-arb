def calculate_arbitrage(odd_list):
    # Calculate the inverse of each odd
    inv_list = [1 / odd for odd in odd_list]

    # Calculate the sum of inverse odds
    inv_sum = sum(inv_list)

    # Calculate the implied probability for each odd
    imp_prob_list = [inv / inv_sum for inv in inv_list]

    # Calculate the total implied probability
    total_imp_prob = sum(imp_prob_list)

    # Check if there is an arbitrage opportunity
    if total_imp_prob < 1:
        arb_margin = 1 - total_imp_prob
        arb_stake = 1 / arb_margin
        return (True, arb_margin, arb_stake)
    else:
        return (False, None, None)

# Example usage
while True:
    num_list_1 = input("Enter list 1 of numbers separated by commas: ")
    num_list_2 = input("Enter list 2 of numbers separated by commas: ")

    # Convert each input string to a list of floats
    list_1 = [float(num) for num in num_list_1.split(',')]
    list_2 = [float(num) for num in num_list_2.split(',')]

    # Find the highest value in each list
    max_value_1 = max(list_1)
    max_value_2 = max(list_2)

    # Input the highest values into the odd list
    odd_list = [max_value_1, max_value_2]

    # Check for arbitrage opportunities
    result = calculate_arbitrage(odd_list)
    if result[0]:
        print("Arbitrage opportunity found! Margin: {:.2%}, Stake: ${:.2f}".format(result[1], result[2]))
    else:
        print("No arbitrage opportunity found.")

    # Prompt user to run the program again
    run_again = input("Do you want to run the program again? (y/n): ")
    if run_again.lower() != 'y':
        break