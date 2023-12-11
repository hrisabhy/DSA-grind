def encode(input_str):
    result_str = ""
    count = 1
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            result_str += input_str[i - 1] + str(count)
            count = 1
    result_str += input_str[-1] + str(count)
    return result_str

def main():
    num_strings = int(input())
    for i in range(num_strings):
        input_string = input()
        encoded_string = encode(input_string)
        print(encoded_string)
if __name__ == "__main__":
    main()
