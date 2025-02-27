def calculScore(ops):
    pile = []
    for op in ops:
        if op == '+':
            if len(pile) > 1:
                pile.append(pile[-1] + pile[-2])
            else:
                pile.append(pile[-1])
        elif op == 'C':
            pile.pop()
        elif op == 'D':
            pile.append(2 * pile[-1])
        else:
            pile.append(int(op))

    return sum(pile)


print(calculScore(["10", "+", "2", "C", "D", "+"]))
