def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    count = 0
    for index, value in enumerate(strand_a):
        count += 1 if value != strand_b[index] else 0

    return count
