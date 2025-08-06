def ZoeysYardSale() -> int:
    """
    Simulates a gacha event for Hill Climb Racing 2 where the player has a chance to roll for 12 random rewards.
    """
    import random

    # Initialize the sky rock balance
    sky_rock_balance = 0
    # Initialize the turn counter
    turn = 1
    # Initialize the list to keep track of collected rewards
    collected_rewards = []

    # Main loop to collect rewards until all 12 are collected
    # The loop continues until the collected_rewards list contains all integers from 1 to 12
    while not verify(collected_rewards):

        n = random.randint(1, 1000)
        turn += 1

        # Determine the reward based on the random number. Get skyrocks from duplicates
        if n <= 25:
            # 2.5% chance to get reward 1
            collected_rewards.append(1)
            if 1 in collected_rewards:
                sky_rock_balance += 200
        elif n <= 125:
            # 10 % chance to get reward 2
            collected_rewards.append(2)
            if 2 in collected_rewards:
                sky_rock_balance += 50
        elif n <= 200:
            # 7.5% chance to get reward 3
            collected_rewards.append(3)
            if 3 in collected_rewards:
                sky_rock_balance += 70
        elif n <= 225:
            # 2.5% chance to get reward 4
            collected_rewards.append(4)
            if 4 in collected_rewards:
                sky_rock_balance += 200
        elif n <= 275:
            # 5% chance to get reward 5
            collected_rewards.append(5)
            if 5 in collected_rewards:
                sky_rock_balance += 100
        elif n <= 425:
            # 15 % chance to get reward 6
            collected_rewards.append(6)
            if 6 in collected_rewards:
                sky_rock_balance += 30
        elif n <= 450:
            # 2.5% chance to get reward 7
            collected_rewards.append(7)
            if 7 in collected_rewards:
                sky_rock_balance += 200
        elif n <= 650:
            # 20 % chance to get reward 8
            collected_rewards.append(8)
            if 8 in collected_rewards:
                sky_rock_balance += 30
        elif n <= 750:
            # 10 % chance to get reward 9
            collected_rewards.append(9)
            if 9 in collected_rewards:
                sky_rock_balance += 50
        elif n <= 775:
            # 2.5% chance to get reward 10
            collected_rewards.append(10)
            if 10 in collected_rewards:
                sky_rock_balance += 200
        elif n <= 925:
            # 15 % chance to get reward 11
            collected_rewards.append(11)
            if 11 in collected_rewards:
                sky_rock_balance += 30
        elif n <= 1000:
            # 7.5% chance to get reward 12
            collected_rewards.append(12)
            if 12 in collected_rewards:
                sky_rock_balance += 70

        # Spending skyrocks for non-collected rewards
        # If the player has enough sky rocks, they can buy the rewards directly
        if 1 not in collected_rewards and sky_rock_balance >= 400:
            collected_rewards.append(1)
            sky_rock_balance -= 400
        if 4 not in collected_rewards and sky_rock_balance >= 400:
            collected_rewards.append(4)
            sky_rock_balance -= 400
        if 7 not in collected_rewards and sky_rock_balance >= 400:
            collected_rewards.append(7)
            sky_rock_balance -= 400
        if 10 not in collected_rewards and sky_rock_balance >= 400:
            collected_rewards.append(10)
            sky_rock_balance -= 400
        if 5 not in collected_rewards and sky_rock_balance >= 180:
            collected_rewards.append(5)
            sky_rock_balance -= 180
        if 3 not in collected_rewards and sky_rock_balance >= 120:
            collected_rewards.append(3)
            sky_rock_balance -= 120
        if 12 not in collected_rewards and sky_rock_balance >= 120:
            collected_rewards.append(12)
            sky_rock_balance -= 120
        if 2 not in collected_rewards and sky_rock_balance >= 90:
            collected_rewards.append(2)
            sky_rock_balance -= 90
        if 9 not in collected_rewards and sky_rock_balance >= 90:
            collected_rewards.append(9)
            sky_rock_balance -= 90
        if 6 not in collected_rewards and sky_rock_balance >= 50:
            collected_rewards.append(6)
            sky_rock_balance -= 50
        if 8 not in collected_rewards and sky_rock_balance >= 50:
            collected_rewards.append(8)
            sky_rock_balance -= 50
        if 11 not in collected_rewards and sky_rock_balance >= 50:
            collected_rewards.append(11)
            sky_rock_balance -= 50

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
