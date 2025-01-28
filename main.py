from bst import bst_heights
from permutate import generate_permutations

print("Enter the number of nodes your BST should contain:")
n = int(input())

input_bsts = generate_permutations(n)
accumulated_height = 0
output = bst_heights(input_bsts)
for bst, height, tree in output:
    accumulated_height += height
    print(f"BST: {bst}, Height: {height}\nTree Representation:\n{tree}")

print(f"Average height: {accumulated_height / len(output)}")
