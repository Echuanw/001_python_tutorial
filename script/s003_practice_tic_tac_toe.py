import os

# Print chessboard
def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def check_victory_all_status(check_path, check_turn, board):
    match check_path:
        case 'r1': return (board['TL'] == check_turn and board['TM'] == check_turn and board['TR'] == check_turn)
        case 'r2': return (board['ML'] == check_turn and board['MM'] == check_turn and board['MR'] == check_turn)
        case 'r3': return (board['BL'] == check_turn and board['BM'] == check_turn and board['BR'] == check_turn)
        case 'c1': return (board['TL'] == check_turn and board['ML'] == check_turn and board['BL'] == check_turn)
        case 'c2': return (board['TM'] == check_turn and board['MM'] == check_turn and board['BM'] == check_turn)
        case 'c3': return (board['TR'] == check_turn and board['MR'] == check_turn and board['BR'] == check_turn)
        case 'x1': return (board['TL'] == check_turn and board['MM'] == check_turn and board['BR'] == check_turn)
        case 'x2': return (board['TR'] == check_turn and board['MM'] == check_turn and board['BL'] == check_turn)
        case _: RuntimeError('Failed to open database')
def check_victory(move, board):
    curr_turn = board[move]
    if move == 'TL': return (check_victory_all_status('r1', curr_turn, board) or check_victory_all_status('c1', curr_turn, board) or check_victory_all_status('x1', curr_turn, board))
    if move == 'ML': return (check_victory_all_status('r2', curr_turn, board) or check_victory_all_status('c1', curr_turn, board))
    if move == 'BL': return (check_victory_all_status('r3', curr_turn, board) or check_victory_all_status('c1', curr_turn, board) or check_victory_all_status('x2', curr_turn, board))
    if move == 'TM': return (check_victory_all_status('r1', curr_turn, board) or check_victory_all_status('c2', curr_turn, board))
    if move == 'MM': return (check_victory_all_status('r2', curr_turn, board) or check_victory_all_status('c2', curr_turn, board) or check_victory_all_status('x1', curr_turn, board) or check_victory_all_status('x2', curr_turn, board))
    if move == 'BM': return (check_victory_all_status('r3', curr_turn, board) or check_victory_all_status('c2', curr_turn, board) or check_victory_all_status('x1', curr_turn, board))
    if move == 'TR': return (check_victory_all_status('r1', curr_turn, board) or check_victory_all_status('c3', curr_turn, board) or check_victory_all_status('x2', curr_turn, board))
    if move == 'MR': return (check_victory_all_status('r2', curr_turn, board) or check_victory_all_status('c3', curr_turn, board))
    if move == 'BR': return (check_victory_all_status('r3', curr_turn, board) or check_victory_all_status('c3', curr_turn, board) or check_victory_all_status('x1', curr_turn, board))
    
def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy() 
        begin = False
        winner_exists = False
        turn = 'x'
        counter = 0
        os.system('cls')
        print_board(curr_board)
        while counter < 9 and (not winner_exists):
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            while curr_board[move] != ' ':
                move = input('位置已有棋子，轮到%s重新走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                winner_exists = check_victory(move, curr_board)
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('cls')
            print_board(curr_board)
            if winner_exists:
                print(f"胜利者为{turn}")
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'

if __name__ == '__main__':
    main()