from itertools import permutations
def generate_permutations(n):
    perms = permutations(range(1, n + 1))
    return [list(p) for p in perms]
