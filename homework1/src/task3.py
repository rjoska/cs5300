import math

def is_prime(y):
    if y <= 1:
        return False
    #now do the check until we get to the square root of the number as described in the wiki article
    # https://en.wikipedia.org/wiki/Prime_number
    for i in range(2, int(math.sqrt(y)) + 1): #the +1 is needed to ensure we reach the number above sqrt of n. 
        if y % i == 0: #check if the remainder is 0
            return False
    return True

def what_type_of_num(z):
    #if for the first part should say is the number "x" is positive, negative, or zero
    if z > 0:
        #print("is positive ", x) #used for testing
        return "positive"
    elif z == 0:
        #print("is Zero ", x)
        return "zero"
    else:
        #print("is negative ", x)
        return "negative"

def first_10_primes():
    count = 0
    start = 0
    prime_list = list()
    # a while loop to find the first 10 primes
    while count < 10:
        isIt = is_prime(start)
        if isIt == True:
            prime_list.append(start)
            count = count + 1
        start = start + 1
    return prime_list
        
def while_sum():
    while_result = 0
    while_start = 1
    while while_start <= 100:
        while_result = while_start + while_result
        while_start = while_start + 1
    #print(while_result) #test print
    return while_result

def main(x):
    pos_or_neg = what_type_of_num(x)
    list_of_primes = first_10_primes()
    # the requested for loop to print the first 10 primes
    for item in list_of_primes:
        print(item)
    sum_total = while_sum()

# An AI told me about this method to ensure when I want to just run the code it will run with this number but
# test cases will not run this.
#code to make functions run also setting a number for the if
if __name__ == "__main__":
    main(-12)