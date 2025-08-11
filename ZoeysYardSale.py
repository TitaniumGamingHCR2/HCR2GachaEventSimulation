def ZoeysYardSale() -> int:
    """
    Simulates a gacha event for Hill Climb Racing 2 where the player has a chance to roll for 12 random rewards.
    """
    import random

    # Initialize the turn counter
    turn = 0
    # Initialize the list to keep track of collected rewards
    collected_rewards = []

    # Main loop to collect rewards until all 12 are collected
    # The loop continues until the collected_rewards list contains all integers from 1 to 12
    while not verify(collected_rewards):

        n = random.randint(1, 1000)
        turn += 1

        # Determine the reward based on the random number
        if n <= 25:
            # 2.5% chance to get reward 1
            collected_rewards.append(1)
        elif n <= 125:
            # 10 % chance to get reward 2
            collected_rewards.append(2)
        elif n <= 200:
            # 7.5% chance to get reward 3
            collected_rewards.append(3)
        elif n <= 225:
            # 2.5% chance to get reward 4
            collected_rewards.append(4)
        elif n <= 275:
            # 5% chance to get reward 5
            collected_rewards.append(5)
        elif n <= 425:
            # 15 % chance to get reward 6
            collected_rewards.append(6)
        elif n <= 450:
            # 2.5% chance to get reward 7
            collected_rewards.append(7)
        elif n <= 650:
            # 20 % chance to get reward 8
            collected_rewards.append(8)
        elif n <= 750:
            # 10 % chance to get reward 9
            collected_rewards.append(9)
        elif n <= 775:
            # 2.5% chance to get reward 10
            collected_rewards.append(10)
        elif n <= 925:
            # 15 % chance to get reward 11
            collected_rewards.append(11)
        elif n <= 1000:
            # 7.5% chance to get reward 12
            collected_rewards.append(12)
    # Return the number of turns taken to collect all rewards
    return turn

def verify(l : list) -> bool:
    """
    Verifies if the list contains all integers from 1 to 12.
    Args:
        l (list): The list to check.
        item (str): The item to verify.
    
    Returns:
        bool: True if the list contains all integers from 1 to 12, False otherwise.
    """
    return all(i in l for i in range(1, 13))

def gems_cost(spins : int, one_spin : int, five_spins : int) -> int:
    """
    Calculates the total cost in gems for the given number of spins.
    Args:
        spins (int): The number of spins.
        one_spin (int): The cost of a single spin.
        five_spins (int): The cost of a five-spin bundle.
    Returns:
        int: The total cost in gems.
    """
    total_cost = 0
    while spins > 0:
        if spins >= 5:
            total_cost += five_spins
            spins -= 5
        else:
            total_cost += one_spin * spins
            spins = 0
    return total_cost

def simulation_stats():
    import matplotlib.pyplot as plt

    # Run multiple simulations and collect data
    num_simulations = 10000
    results = [ZoeysYardSale() for _ in range(num_simulations)]

    # Print the average number of turns taken
    average_turns = sum(results) / num_simulations
    print(f"Average turns taken to collect all rewards: {average_turns}")

    # Print the maximum number of turns taken
    max_turns = max(results)
    print(f"Maximum turns taken to collect all rewards: {max_turns}")

    # Print the minimum number of turns taken
    min_turns = min(results)
    print(f"Minimum turns taken to collect all rewards: {min_turns}")

    # Print the average gem cost
    average_gem_cost = gems_cost(round(average_turns, 0), 250, 1100)  
    print(f"Average gem cost for {average_turns} turns: {average_gem_cost}")

    # Plotting the results
    plt.hist(results, bins=range(1, max(results) + 1), alpha=0.75, color='blue')
    plt.title("Distribution of Turns Taken to Collect All Rewards")
    plt.xlabel("Number of Turns")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    print("Running Zoey's Yard Sale Simulation...")
    simulation_stats()
