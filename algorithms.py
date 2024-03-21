def count_five_digit_numbers():
    count = 0
    for num in range(10000, 100000):
        digits = [int(d) for d in str(num)]
        if all(digits[i] != digits[i+1] for i in range(len(digits)-1)) and num % 3 == 0:
            count += 1
    return count


result = count_five_digit_numbers()
print("Number of five-digit numbers meeting the conditions:", result)