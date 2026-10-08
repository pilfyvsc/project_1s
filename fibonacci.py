def fibonacci(n):
    # Base cases for n <= 0 or 1
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]

    for i in range(2, n):
        # Add the sum of the last two numbers to the list
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)

    return sequence

# Example usage: Get the first 10 numbers
print(fibonacci(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]