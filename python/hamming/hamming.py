def distance(strand_a, strand_b):
    """Calculate Hamming distance between DNA strands"""
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be equal length')
    return sum(1 for a, b in zip(strand_a, strand_b) if a != b)
