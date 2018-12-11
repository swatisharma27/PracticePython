def tictactoe(moves):
    for i in range(0,3):
        if moves[i] == [1, 1, 1]:
            return "'1' wins (horizontal)."
            break
        elif moves[i] == [2, 2, 2]:
            return "'2' wins (horizontal)."
            break
        elif [x[i] for x in moves] == [1, 1, 1]:
            return "'1' wins (vertical)."
            break
        elif [x[i] for x in moves] == [2, 2, 2]:
            return "'2' wins (vertical)."
            break
        else:
            continue

    if moves[0][0] == moves[1][1] == moves[2][2] == 1 or moves[0][2] == moves[1][1] == moves[2][0] == 1:
        return "'1' wins (diagonal)."
    elif moves[0][0] == moves[1][1] == moves[2][2] == 2 or moves[0][2] == moves[1][1] == moves[2][0] == 2:
        return "'2' wins (diagonal)."
    else:
        return 'Draw. No one wins!'