i = 0#python counts from 1
while i < 100:#python stops exactly at 100 when using <
    i = i + 1#increment the while loop by 1
    if i % 15 == 0:# Check if divisible by 15 using modulo
        print("FizzBuzz")
    elif i % 3 == 0:# Check divisibility by 3 using elif  
        print("Fizz")
    elif i % 5 == 0:# Similar check if divisible by 5
        print("Buzz")
    else:
        print (i)# Print the number itself if none of the above
