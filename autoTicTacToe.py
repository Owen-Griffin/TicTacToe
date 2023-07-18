def main():
    import random

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

        playerSymbol = random.choice(validSymbols)
        if playerSymbol == validSymbols[0]:
            computerSymbol = validSymbols[1]
        elif playerSymbol == validSymbols[1]:
            computerSymbol = validSymbols[0]  
                

        currentTurn = random.choice(validSymbols)

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
                
        gameOn = True

        while gameOn:
            # get player move
            if currentTurn == playerSymbol:
                vaildBoardIndexes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                for i in range(0, 9):
                    if board[i] != '-':
                        vaildBoardIndexes.remove(i)
                
                board[random.choice(vaildBoardIndexes)] = playerSymbol
                currentTurn = computerSymbol

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
                gameOn = False
                return 'p'
            elif checkWin(board, computerSymbol):
                gameOn = False
                return 'c'
            elif checkTie(board, playerSymbol):
                gameOn = False
                return 't'
    '''
    import timeit  
    elapsed_time = timeit.timeit(ticTacToe, number=10000)
    print(elapsed_time)
    '''
    import threading, locale
    locale.setlocale(locale.LC_ALL, '')
    global winTracker
    winTracker = {
        'ties': 0,
        'playerWins': 0,
        'computerWins': 0
    }
    global numToRun
    numToRun = int(input('How Many (Value will be multiplied by 10): '))

    def mainTic():
        for i in range(1, numToRun + 1):
            output = ticTacToe()
            if output == 't':
                winTracker['ties'] += 1
            if output == 'p':
                winTracker['playerWins'] += 1
            if output == 'c':
                winTracker['computerWins'] += 1
    def mainWithLoggerTic():
        iterValue = 100/numToRun
        for i in range(1, numToRun + 1):
            output = ticTacToe()
            if output == 't':
                winTracker['ties'] += 1
            if output == 'p':
                winTracker['playerWins'] += 1
            if output == 'c':
                winTracker['computerWins'] += 1
            print(iterValue*i, end='\r')

    thread1 = threading.Thread(target=mainWithLoggerTic, args=())
    thread2 = threading.Thread(target=mainTic, args=())
    thread3 = threading.Thread(target=mainTic, args=())
    thread4 = threading.Thread(target=mainTic, args=())
    thread5 = threading.Thread(target=mainTic, args=())
    thread6 = threading.Thread(target=mainTic, args=())
    thread7 = threading.Thread(target=mainTic, args=())
    thread8 = threading.Thread(target=mainTic, args=())
    thread9 = threading.Thread(target=mainTic, args=())
    thread10 = threading.Thread(target=mainTic, args=())

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()

    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()
    thread1.join()

    print(winTracker)
    print(f"Ties: {winTracker['ties']}. This is {str(winTracker['ties']/(numToRun*10)*100)}%")
    print(f"Player: {winTracker['playerWins']}. This is {str(winTracker['playerWins']/(numToRun*10)*100)}%")
    print(f"Computer: {winTracker['computerWins']}. This is {str(winTracker['computerWins']/(numToRun*10)*100)}%")
    print(f'Played {locale.format_string("%d", (numToRun*10), grouping=True)} games.')

if __name__ == "__main__":
    import timeit
    elapsed_time = timeit.timeit(main, number=1)
    print(f'Function took {elapsed_time} seconds')