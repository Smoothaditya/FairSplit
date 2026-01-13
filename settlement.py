from collections import defaultdict

def calculate_settlement(expenses, people):
    total = sum(e[2] for e in expenses)
    per_head = total / len(people)

    paid = defaultdict(float)
    for payer, _, amount, _ in expenses:
        paid[payer] += amount

    balance = {p: round(paid[p] - per_head, 2) for p in people}

    debtors = [(p, -amt) for p, amt in balance.items() if amt < 0]
    creditors = [(p, amt) for p, amt in balance.items() if amt > 0]

    settlements = []
    i = j = 0

    while i < len(debtors) and j < len(creditors):
        d, d_amt = debtors[i]
        c, c_amt = creditors[j]
        x = min(d_amt, c_amt)

        settlements.append(f"{d} pays {c} ₹{x:.2f}")

        debtors[i] = (d, d_amt - x)
        creditors[j] = (c, c_amt - x)

        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    return per_head, settlements
