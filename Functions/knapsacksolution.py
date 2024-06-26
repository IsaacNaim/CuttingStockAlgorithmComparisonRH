from gurobipy import Model, GRB, quicksum, Column
import math

def solve_cutting_stock(data, standard_length=192000, EPS=1e-6):
    print("Input data:", data)  # Debug print

    # Sanity check: Ensure no cut lengths exceed the standard length
    for sublist in data:
        if sublist[1] > standard_length:
            raise ValueError(f"Cut length {sublist[1]} exceeds the standard length {standard_length}")

    quantities = [item[0] for item in data]
    lengths = [item[1] for item in data]
    m = len(data)
    t = []
    K = 0

    # Create initial patterns (trivial solution: one piece per pattern)
    for i in range(m):
        t.append([1 if i == j else 0 for j in range(m)])

    # Create the master problem
    master = Model("master")
    master.setParam('OutputFlag', 0)  # Disable solver output
    x = {k: master.addVar(obj=1, vtype="I", name=f"x[{k}]") for k in range(len(t))}
    master.update()

    # Add constraints to the master problem
    orders = [master.addConstr(quicksum(t[k][i] * x[k] for k in x) >= quantities[i], name=f"order[{i}]") for i in range(m)]
    master.update()

    # Column generation loop
    while True:
        # Solve the relaxed master problem
        relax = master.relax()
        relax.optimize()
        pi = [c.Pi for c in relax.getConstrs()]

        # Solve the knapsack problem to find a new pattern
        knapsack = Model("KP")
        knapsack.ModelSense = -1
        y = {i: knapsack.addVar(ub=quantities[i], vtype="I", name=f"y[{i}]") for i in range(m)}
        knapsack.update()
        knapsack.addConstr(quicksum(lengths[i] * y[i] for i in range(m)) <= standard_length, "width")
        knapsack.setObjective(quicksum(pi[i] * y[i] for i in range(m)), GRB.MAXIMIZE)
        knapsack.optimize()

        # Check if the new pattern has a significant impact
        if knapsack.ObjVal < 1 + EPS:
            break

        # Extract the new pattern
        pat = [int(y[i].X + 0.5) for i in y]
        t.append(pat)
        col = Column()
        for i in range(m):
            if pat[i] > 0:
                col.addTerms(pat[i], orders[i])
        x[K] = master.addVar(obj=1, vtype="I", name=f"x[{K}]", column=col)
        master.update()
        K += 1

    # Solve the final master problem
    master.optimize()

    # Extract the final cutting patterns
    rolls = []
    total_cuts_length = 0
    for k in x:
        if x[k].X > 0.5:  # Only consider patterns used
            for _ in range(int(x[k].X + 0.5)):
                roll = []
                for i in range(m):
                    roll.extend([lengths[i]] * t[k][i])
                rolls.append(sorted(roll))
                total_cuts_length += sum(roll)
    rolls.sort()

    # Calculate the total material used and waste
    total_material_used = len(rolls) * standard_length
    total_waste = total_material_used - total_cuts_length
    waste_percentage = (total_waste / total_material_used) * 100

    # Debug prints
    print("Total material used:", total_material_used)
    print("Total cuts length:", total_cuts_length)
    print("Total waste:", total_waste)
    print("Waste percentage:", waste_percentage)

    return rolls, waste_percentage
