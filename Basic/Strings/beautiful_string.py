def beautiful_string(binary_str):
    operation_count = 0

    for i in range(1, len(binary_str)):
        # Check if the current character is the same as the previous one
        if binary_str[i] == binary_str[i - 1]:
            # Increment the operation count, and change the current character to break the repetition
            operation_count += 1
            binary_str = binary_str[:i] + ('0' if binary_str[i] == '1' else '1') + binary_str[i + 1:]

    return operation_count

# Example usage
binary_str = "0000"
print(beautiful_string(binary_str))
