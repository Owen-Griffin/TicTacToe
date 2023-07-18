import random

def main():
    def ticTacToe():
        board = ['-', '-', '-',
                '-', '-', '-',
                '-', '-', '-']
        playerIntToBoard = {1: 0, 
                            2: 1, 
                            3: 2,
                            4: 3,
                            5: 4,
                            6: 5,
                            7: 6,
                            8: 7,
                            9: 8}
        validSymbols = ['X', 'O']

        # get player prefered symbol
        while True:
            playerSymbol = input(f'Do you want to play as {validSymbols[0]} or {validSymbols[1]}? ({validSymbols[0]}/{validSymbols[1]}) ').upper()

            if playerSymbol in validSymbols:
                print(f'You will play as {playerSymbol}')
                if playerSymbol == validSymbols[0]:
                    computerSymbol = validSymbols[1]
                elif playerSymbol == validSymbols[1]:
                    computerSymbol = validSymbols[0]
                else:
                    print('Broken')
                    break
                print(f'The computer will play as {computerSymbol}')
                break
            else:
                print(f'Invalid Input. Please enter a valid symbol ({validSymbols[0]}/{validSymbols[1]}).')

        currentTurn = random.choice(validSymbols)
        print(f'\n{currentTurn} will go first.')

        # check win function
        def checkWin(board, symbol):
            for i in range(0, 9, 3):
                if board[i] == board[i + 1] == board[i + 2] and board[i] == symbol:
                    return True
            for i in range(3):
                if board[i] == board[i+3] == board[i+6] and board[i] == symbol:
                    return True
            if board[0] == board[4] == board[8] == symbol:
                return True
            elif board[2] == board[4] == board[6] == symbol:
                return True
            else:
                return False
            
        # check for tie function
        def checkTie(board, validSymbols):
            for cell in board:
                if cell == '-':
                    return False
            return True
        
        # print board function
        def printBoard(board):
            print(f'|{board[0]}|{board[1]}|{board[2]}|    1|2|3')
            print(f'-------    -----')
            print(f'|{board[3]}|{board[4]}|{board[5]}|    4|5|6')
            print(f'-------    -----')
            print(f'|{board[6]}|{board[7]}|{board[8]}|    7|8|9')
            print('\n')
                
        gameOn = True

        while gameOn:
            print(f'Current Turn = {currentTurn}')
            printBoard(board)
            
            # get player move
            if currentTurn == playerSymbol:
                while True:
                    placeSymbol = input(f'Where would you like to place your {playerSymbol}? (1-9) ')
                    if placeSymbol.isdigit():
                        placeSymbol = int(placeSymbol)
                        if 1 <= placeSymbol <= 9:
                            boardPlaceSpot = playerIntToBoard[placeSymbol]
                            if board[boardPlaceSpot] != '-':
                                print(f'Invalid Input! Must place {playerSymbol} in empty (-) spot.')
                            else:
                                board[int(boardPlaceSpot)] = playerSymbol
                                currentTurn = computerSymbol
                                break
                        else:
                            print('Invalid Input! Input must be an interger between 1 and 9!')
                    else:
                        print('Invalid Input! Input must be an interger between 1 and 9!')
            
            # get computer move
            elif currentTurn == computerSymbol:
                vaildBoardIndexes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                for i in range(0, 9):
                    if board[i] != '-':
                        vaildBoardIndexes.remove(i)
                
                board[random.choice(vaildBoardIndexes)] = computerSymbol
                currentTurn = playerSymbol
            
            # check win/tie conditions
            if checkWin(board, playerSymbol):
                printBoard(board)
                print('Player wins! Congratulations!')
                gameOn = False
                return 'p'
            elif checkWin(board, computerSymbol):
                printBoard(board)
                print('Sorry, Computer Wins...')
                gameOn = False
                return 'c'
            elif checkTie(board, playerSymbol):
                printBoard(board)
                print('Tie Game!')
                gameOn = False
                return 't'
    
    # returns:
    #   t = tie
    #   p = player
    #   c = computer
    print(ticTacToe())
    while True:
        playAgain = input('Would you like to play again? (y/n) ').upper()
        if playAgain == 'Y':
            print(ticTacToe())
        elif playAgain == 'N':
            print('Bye!')
            exit()
        else:
            print('Invalid Input.')

if __name__ == '__main__':
    main()