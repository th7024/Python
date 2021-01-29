def sumOfDigits(number):
    if number >=1:
        return number % 10 + sumOfDigits(number //10)
    else:
        return 0


print(sumOfDigits(47253))
print(sumOfDigits(643))