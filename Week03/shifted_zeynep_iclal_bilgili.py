def shifted(lst):
    total = 0
    for i in range(1, len(lst)):
        diff = abs(lst[i] - lst[i-1])
        if diff > 1:
            total += diff - 1
    return total
