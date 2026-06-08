balance = 100
print('Terminal ATM Interface')
print('======================')
print('Use appropriate keys for the required operation.')
print('\n')
while True:
    print('1. Check your Balance')
    print('2. WIthdraw Amount')
    print('3. Deposit Amount')
    print('4. Quit')
    try:
        response = int(input('Enter the key  \n'))
    except ValueError:
        print('Invalid Key! Try Again')
        continue
    if response == 1:
        print(f'Your Balance is ${balance}.\n')
        continue
    elif response == 2:
        try:
            withdraw = int(input('Enter the amount you would like to withdraw in numbers\n'))
        except ValueError:
            print('Invalid format! Try Again.\n')
        balance -= withdraw
        print('Amount was successfully withdrawn')
        print(f'Your New Balance is ${balance}.\n')
    elif response == 3:
        try:
            deposit = int(input('Enter the amount you would like to deposit in numbers\n'))
        except ValueError:
            print('Invalid format! Try Again.')
        balance += deposit
        print('Amount was successfully deposited')
        print(f'Your New Balance is ${balance}.')
    elif response == 4:
        break
    else:
        print('The value of key should be between among 1 , 2 , 3, 4 only! Try Again.')
        continue

