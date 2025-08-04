"""Generate and display all permutations of a given string."""

from itertools import permutations

def get_all_permutations(s):
    """Return a list of all permutations of the string `s`."""
    perm_list = list(permutations(s))
    return [''.join(p) for p in perm_list]

def print_permutations(perms):
    """Prints total number and each permutation from the list `perms`."""
    print(f"Total permutations: {len(perms)}")
    print("All permutations:")
    for i, p in enumerate(perms, start=1):
        print(f"{i}: {p}")

def factorial(n):
    """Compute and return factorial of `n`."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

WORD = "abc"
print(f"Generating permutations for: {WORD}")

expected_count = factorial(len(WORD))
print(f"Expected number of permutations (n!): {expected_count}")

permutations_list = get_all_permutations(WORD)
if len(permutations_list) != expected_count:
    print("Warning: Permutation count mismatch!")

print_permutations(permutations_list)
