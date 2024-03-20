from itertools import permutations

def is_magic_square(square):
    target_sum = sum(square[0])
    # Check rows
    if any(sum(row) != target_sum for row in square):
        return False
    # Check columns
    if any(sum(square[i][j] for i in range(3)) != target_sum for j in range(3)):
        return False
    # Check diagonals
    if sum(square[i][i] for i in range(3)) != target_sum or sum(square[i][2 - i] for i in range(3)) != target_sum:
        return False
    return True

def find_magic_square():
    for perm in permutations(range(1, 10)):
        square = [perm[:3], perm[3:6], perm[6:]]
        square = [[x**2 for x in row] for row in square]  # Convert to square numbers
        if is_magic_square(square):
            return square
    return None

# Find and print a magic square
magic_square = find_magic_square()

if magic_square:
    for row in magic_square:
        print(row)
else:
    print("No magic square found.")
