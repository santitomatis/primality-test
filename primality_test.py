def is_primal(number):
    result = True
    if number == 1:
        return(False)
    else:
        result = True

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue

        if number % i == 0:
            result = False

    if result == True:
        return(True)
    
    else:
        return(False)
        

def run():
    number = int(input("Type a   number to execute a primality test: "))
    if is_primal(number):
        print("It is a prime number")
    
    else: 
        print("It is not a primer number")


if __name__ == "__main__":
    run()

