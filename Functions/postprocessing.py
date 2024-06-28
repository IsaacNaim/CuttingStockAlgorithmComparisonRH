def best_fit_algorithm(shortage_cuts, existing_rolls, standard_length):
    rolls = existing_rolls.copy()
    for cut_length in shortage_cuts:
        placed = False
        # Try to place the cut into an existing roll
        for roll in rolls:
            if sum(roll) + cut_length <= standard_length:
                roll.append(cut_length)
                placed = True
                break
        # If the cut doesn't fit into any existing roll, create a new roll
        if not placed:
            rolls.append([cut_length])
    return rolls

def post_process_shortages(data, rolls, standard_length=192000):
    quantities = [item[0] for item in data]
    lengths = [item[1] for item in data]

    # Count the cuts in the output rolls
    actual_quantities = {length: 0 for length in lengths}
    for roll in rolls:
        for cut in roll:
            actual_quantities[cut] += 1

    # Identify shortages
    shortages = {length: quantities[i] - actual_quantities[length] for i, length in enumerate(lengths)}

    # Create a list of all the cuts needed to fill the shortages
    shortage_cuts = []
    for length, shortage in shortages.items():
        if shortage > 0:
            shortage_cuts.extend([length] * shortage)

    # Use the best-fit algorithm to fill shortages
    all_rolls = best_fit_algorithm(shortage_cuts, rolls, standard_length)

    # Recalculate the total material used and waste
    total_cuts_length = sum(sum(roll) for roll in all_rolls)
    total_material_used = len(all_rolls) * standard_length
    total_waste = total_material_used - total_cuts_length
    waste_percentage = (total_waste / total_material_used) * 100

    return all_rolls, waste_percentage