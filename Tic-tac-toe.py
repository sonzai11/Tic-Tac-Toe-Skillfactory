rules = ('Игроки по очереди ставят на свободные клетки поля 3×3 знаки \n'
         '(один всегда крестики, другой всегда нолики). \n'
         'Первый, выстроивший в ряд 3 своих фигуры по вертикали, \n'
         'горизонтали или большой диагонали, выигрывает. \n'
         'Если игроки заполнили все 9 ячеек и оказалось, \n'
         'что ни в одной вертикали, горизонтали или большой диагонали нет \n'
         'трёх одинаковых знаков, партия считается закончившейся в ничью. \n'
         'Первый ход делает игрок, ставящий крестики.\n')

def gridPrint(gameGrid):
    print('\n  0 1 2\n'
          '0', *gameGrid[0],'\n'
          '1', *gameGrid[1],'\n'
          '2', *gameGrid[2],'\n')

def winCheck(winningCondition):
    for row in range(3):
        if (gameGrid[row][0] == gameGrid[row][1] == gameGrid[row][2] !='-'):
            winningCondition = True
    for col in range(3):
        if (gameGrid[0][col] == gameGrid[1][col] == gameGrid[2][col] != '-'):
            winningCondition = True
    if (gameGrid[0][0] == gameGrid[1][1] == gameGrid[2][2] != '-') or (gameGrid[0][2] == gameGrid[1][1] == gameGrid[2][0] != '-'):
        winningCondition = True
    return winningCondition

def makeMove(moveCounter):
    rowMove = int(input('Введите ряд следующего хода:'))
    colMove = int(input('Введите колонку следующего хода:'))
    if (0 <= rowMove <= 2) and (0 <= colMove <= 2):
        if gameGrid[rowMove][colMove] != '-':
            print(f'ХОД [{rowMove},{colMove}] уже был совершен!')
            return 0
        else:
            if moveCounter:
                gameGrid[rowMove].pop(colMove)
                gameGrid[rowMove].insert(colMove,'x')
                moveCounter = False
            else:
                gameGrid[rowMove].pop(colMove)
                gameGrid[rowMove].insert(colMove,'o')
                moveCounter = True
            return 1
    else:
        print(f'ХОД [{rowMove},{colMove}] выходит за границы игрового поля!')
        return 0

gameGrid = (['-','-','-'],
            ['-','-','-'],
            ['-','-','-'])

moveCounter = True
winningCondition = False
tieCondition = 0


print(f'НАЧАЛО ИГРЫ!\n\n'
      f'ПРАВИЛА:\n'
      f'{rules}')

while (not winningCondition and tieCondition != 9):
    gridPrint(gameGrid)
    if moveCounter:
        print('Ход "КРЕСТИКОВ"')
        if makeMove(moveCounter) == 1:
            tieCondition +=1
            moveCounter = False
    else:
        print('Ход "НОЛИКОВ"')
        if makeMove(moveCounter) == 1:
            tieCondition +=1
            moveCounter = True
    if tieCondition == 9:
        print(f'\n\n\n'
              f'ИГРА ЗАВЕРШИЛАСЬ В НИЧЬЮ!')
        gridPrint(gameGrid)
    if winCheck(winningCondition):
        winningCondition = True
        if not moveCounter:
            print(f'\n\n\n'
                  f'ПОБЕДА КРЕСТИКОВ! Игра завершилась на {tieCondition} ходу')
            gridPrint(gameGrid)
        else:
            print(f'\n\n\n'
                  f'ПОБЕДА НОЛИКОВ! Игра завершилась на {tieCondition} ходу')
            gridPrint(gameGrid)
