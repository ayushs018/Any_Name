from itertools import permutations

def get_all_permutations(s):
    perm_list = list(permutations(s))
    return [''.join(p) for p in perm_list]

def print_permutations(perms):
    print(f"Total permutations: {len(perms)}")
    print("All permutations:")
    for i, p in enumerate(perms, start=1):
        print(f"{i}: {p}")

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

word = "abc" 
print(f"Generating permutations for: {word}")

expected_count = factorial(len(word))
print(f"Expected number of permutations (n!): {expected_count}")

permutations_list = get_all_permutations(word)
if len(permutations_list) != expected_count:
    print("Warning: Permutation count mismatch!")

print_permutations(permutations_list)
    

