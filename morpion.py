import copy

'''Affiche les numéros a entrer pour jouer a tel case'''
def start():
    print("Pour jouer, mémoriser juste le numéro des cases suivant : ")
    print("#-----#-----#-----#")
    print("| 1 1 | 1 2 | 1 3 |")
    print("#-----#-----#-----#")
    print("| 2 1 | 2 2 | 2 3 |")
    print("#-----#-----#-----#")
    print("| 3 1 | 3 2 | 3 3 |")
    print("#-----#-----#-----#")

'''Affiche le tableau'''
def print_board(board):
    print("#-----#-----#-----#")
    print("| ",board[0][0]," | ",board[0][1]," | ", board[0][2]," |")
    print("#-----#-----#-----#")
    print("| ",board[1][0]," | ",board[1][1]," | ", board[1][2]," |")
    print("#-----#-----#-----#")
    print("| ", board[2][0]," | ", board[2][1]," | ", board[2][2]," |")
    print("#-----#-----#-----#")

'''Verifie le tableau pour voir si il y a un gagnant'''
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

'''Vérifie que le tableau n'est pas plein'''
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

'''Récupère les cases vides'''
def get_empty_cells(board):
    cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                cells.append((i, j))
    return cells

'''Applique et fais tourner l'algorithme minimax'''
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner:
        return 10 - depth if winner == 'X' else -10 + depth

    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, False)
            board[i][j] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, True)
            board[i][j] = ' '
            best_score = min(score, best_score)
        return best_score

'''Cherche le meilleur coup possible'''
def get_best_move(board):
    best_score = float('-inf')
    best_move = (-1, -1)

    for i, j in get_empty_cells(board):
        board[i][j] = 'X'
        score = minimax(board, 0, False)
        board[i][j] = ' '

        if score > best_score:
            best_score = score
            best_move = (i, j)

    return best_move

'''Fais tourner le jeu'''
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Bienvenue au jeu du Morpion! Vous jouez contre une IA qui utilise l'algorithme Minmax.")
    print("Entrer les coordonnées pour effectuer votre coup. Par exemple, '1 2' pour jouer votre coup a la case se situant a la première ligne et deuxième colonne.")
    start()
    print("\n")
    while True:
        print_board(board)
        row, col = map(int, input("Entrez la ligne et la colonne (1 2, séparé d'un espace): ").split())
        row -= 1
        col -= 1

        if board[row][col] != ' ':
            print("Coup impossible. Réessayer")
            continue

        board[row][col] = 'O'

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Félicitations {winner} gagne!")
            break

        if is_board_full(board):
            print_board(board)
            print("Egalité!")
            break

        best_move = get_best_move(board)
        board[best_move[0]][best_move[1]] = 'X'

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Désolé, {winner} gagne! Vous avez perdu.")
            break

        if is_board_full(board):
            print_board(board)
            print("Egalité!")
            break

'''Lance le programme'''
if __name__ == "__main__":
    play_game()
