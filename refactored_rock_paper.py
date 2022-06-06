# Define User Moves Function
def userMoves():
    choices = ['Rock','Paper', 'Scissors']
    for i in choices:
        R = choices[0].capitalize()
        P = choices[1].capitalize()
        S = choices[2].capitalize()
    while True:
        print(R, P, S)
        usermove = input('Pick: R for Rock, P for Paper or S for Scissors)\n').capitalize()
        if usermove.startswith('P'):
            usermove = P
            print('You picked:',P.capitalize())
            return usermove
        elif usermove.startswith('R'):
            usermove = R
            print('You picked:',R.capitalize())
            return usermove 
        elif usermove.startswith('S'):
            usermove = S
            print('You picked:',S.capitalize())
            return usermove
        else:
            print("Invalid choice selected. Try again!")

# Define Computer Moves Function
def computerMoves():
    import random 
    choices = ['Rock','Paper', 'Scissors'] 
    computermove = random.choice(choices).capitalize()
    print('Computer picked:',computermove.capitalize())
    return computermove

#Define Comparator Function 
def comparator(usermove, computermove):
    if usermove == computermove:
        result = 'Tie'
        return result 
    elif usermove == 'Rock' and computermove == 'Paper':
        result = 'Computer Won'
        return result
    elif usermove == 'Paper' and computermove == 'Scissors':
        result = 'Computer Won'
        return result
    elif usermove == 'Scissors' and computermove == 'Rock':
        result = 'Computer Won'
        return result
    else:
        result = 'You Won'
        return result 
        
# Define Judge Function 
def judge():
    result = comparator(userMoves(), computerMoves())
    print(result)
    if result == 'Tie':
        print('Play again')
        judge()
    else:
        return result

judge()
