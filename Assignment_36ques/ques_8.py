

player1 = input("Name of player 1: ")
player2 = input("Name of player 2: ")

move1 = input("Make a choice " + player1 + " out of rock/paper/scissor: ")
move2 = input("Make a choice " + player2 + " out of rock/paper/scissor: ")

def compare_moves(m1, m2):
    if m1 == m2:
        return "Its a tie!"
    elif m1 == 'rock':
        if m2 == 'scissor':
            return 'Congrats Player 1'
        elif m2 == 'paper':
            return 'Congrats Player 2'
    elif m1 == 'scissor':
        if m2 == 'paper':
            return 'Congrats Player 1'
        elif m2 == 'rock':
            return 'Congrats Player 2'
    elif m1 == 'paper':
        if m2 == 'rock':
            return 'Congrats Player 1'
        elif m2 == 'scissor':
            return 'Congrats Player 2'
    else:
        return "Wrong option! Try Again! Choose rock/paper/scissor"

print(compare_moves(move1, move2))


