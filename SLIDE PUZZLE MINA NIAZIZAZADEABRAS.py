# MINA NIAZIZADEABRAS
# SLIDE PUZZLE OR (معمای 16)
# COMPUTER SCIENCE

import random
import sys

Game_Play = True
move = 0

fifteen_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

random.shuffle(fifteen_list)
print('\n' * 2)

matrix = []

while fifteen_list:
    matrix.append(fifteen_list[:4])
    fifteen_list = fifteen_list[4:]

def zero(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                return (x, y)

def draw(board):
    print('\n\t  -☆-M-☆-M-☆-M-☆-M-☆-M-☆-M-☆- ')
    for row in board:
        for num in row:
            if num == 0:
                print('\t|  ', end=' ')
            else:
                print('\t| {0:2d}'.format(num), end=' ')
        print('|\n\t -☆-M-☆-M-☆-M-☆-M-☆-M-☆-M-☆- ')

def asknumber():
    while True:
        num = input('\nPlease type the number of the block to move (q to quit): ')
        if num.lower() in ['q', 'quit']:
            print('\n\nGame is Over')
            sys.exit()
        try:
            num = int(num)
            if num < 0 or num > 15:
                print('Please enter a number between 0 and 15 or q to quit.')
            else:
                return num
        except ValueError:
            print('Please enter a number or q to quit.')

while Game_Play:
    draw(matrix)
    num = asknumber()
    
    empty_space = zero(matrix)
    block = None

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if num == matrix[i][j]:
                block = (i, j)
                break
        if block is not None:
            break

    if (empty_space == (block[0] - 1, block[1]) or 
        empty_space == (block[0] + 1, block[1]) or 
        empty_space == (block[0], block[1] - 1) or 
        empty_space == (block[0], block[1] + 1)):
        
        matrix[empty_space[0]][empty_space[1]] = num
        matrix[block[0]][block[1]] = 0
        
        move += 1
        print(f'\n You have made {move} moves so far\n')
    else:
        print('Invalid move, try again!')
