def primecounter_py(range_from: int, range_til: int) -> (int, int):
    """ Returns the number of found prime numbers using range"""
    check_count = 0
    prime_count = 0
    prime_numbers = []
    range_from = range_from if range_from >= 2 else 2
    for num in range(range_from, range_til + 1):
        for divnum in range(2, num):
            check_count += 1
            if (num % divnum) == 0:
                break
        else:
            prime_count += 1
            prime_numbers.append(num)
    return prime_numbers, prime_count

