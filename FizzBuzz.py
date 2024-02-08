i = 0#python counts from 1
while i < 100:#python stops exactly at 100 when using <
    i = i + 1#increment the while loop by 1
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print (i)
