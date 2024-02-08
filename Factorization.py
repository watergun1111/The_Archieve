print('\033[33m' + "\n\n\n\n\n\n\n\nPlease enter a number or command in the blank below to run the program.\nIf you enter '/help' in the blank, you can see help related to input and output. If this is your first time using it, we recommend checking the help." + '\033[0m')
print('\033[91m' + "※ If the program does not run, please check for any typos in the number or command." + '\033[0m')
div = 2
divs = []
count = 2
result = '\033[90m' + "==> "
num = input('\033[90m' + ">> " + '\033[0m')
while True:
    if num == "/help":
        print('\033[96m' + "\nThis is the help for running and using the program.\nInput: Enter a natural number in Arabic numeral format.\nOutput: Prime factors p and q along with natural numbers m and n are printed in the format '==> (p**m) (q**n)'.\n       (Here, p and q are prime factors, and m and n are their respective powers)." + '\033[0m')
        num = input('\033[90m' + ">> " + '\033[0m')
    else:
        try:
            num = int(num)
        except ValueError:
            print('\033[91m' + "\n\n\n\n\n\n\n\n\n\nThis is an unknown command." + '\033[0m')
            num = input('\033[90m' + ">> " + '\033[0m')
        else:
            num = int(num)
            input = num
            while div <= num:
                if num % div == 0:
                    divs.append(div)
                    num /= div
                    div = 2
                    continue
                else:
                    div += 1
        while len(divs) > 0:
            if divs.count(count) > 0:
                result += '\033[92m' + "(" + str(count) + "**" + str(divs.count(count)) + ") "
                for x in range(divs.count(count)):
                    divs.remove(count)
            count += 1
        if result == '\033[90m' + "==> " + '\033[92m' + "(" + str(input) + "**1" + ") ":
            print('\033[90m' + "==> " + '\033[31m' + "It is a prime number." + '\033[0m')
        else:
            print(result.rstrip(" "))
        print('\033[0m' + "")
        break
