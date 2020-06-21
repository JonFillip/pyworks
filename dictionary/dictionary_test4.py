chess_pieces = {
    'black': {
        'a8': 'brook',
        'b8': 'bknight',
        'c8': 'bbishop',
        'd8': 'bking',
        'e8': 'bqueen',
        'f8': 'bbishop',
        'g8': 'bknight',
        'h8': 'brook',
        'a7': 'bpawn',
        'b7': 'bpawn',
        'c7': 'bpawn',
        'd7': 'bpawn',
        'e7': 'bpawn',
        'f7': 'bpawn',
        'g7': 'bpawn',
        'h7': 'bpawn'
    },
    'white': {
        'a1': 'wrook',
        'b1': 'wknight',
        'c1': 'wbishop',
        'd1': 'wking',
        'e1': 'wqueen',
        'f1': 'wbishop',
        'g1': 'wknight',
        'h1': 'wrook',
        'a2': 'wpawn',
        'b2': 'wpawn',
        'c2': 'wpawn',
        'd2': 'wpawn',
        'e2': 'wpawn',
        'f2': 'wpawn',
        'g2': 'wpawn',
        'h2': 'wpawn' 
    }
}

def isValidChessBoard(player, piece):
    """"Checks that the pieces of the chess board are in their right position"""
    # check to see the number of chess pieces on the board is 16
    white_pieces = 0
    black_pieces = 0
    for color, pieces in player.items():
        if color == 'black':
            black_pieces += pieces.get(piece, 0)
            return black_pieces
        elif color == 'white':
            white_pieces += pieces.get(piece, 0)
            return white_pieces
    if black_pieces > 16 or black_pieces <= 17:
        return False
    if white_pieces > 16 or white_pieces <= 17:
        return False
    
    # check that the number of pawns for both the black and white players is not less or more than 8
    if sum(pawn == 'bpawn' for pawn in piece.values()) >= 9:
        return False
    if sum(pawn == 'wpawn' for pawn in piece.values()) >= 9:
        return False
    
    # Check to validate the position of a piece on the board
    board_keys = list(piece.keys()) # Creates a list of dictionary keys e.g ['a1', 'b2', 'h8',...]
    row = str([x for x in range(9)]) 
    board_row = [s[:1] for s in board_keys]
    if not all(elem in row for elem in board_row):
        return False
    
    column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    board_column = [s[1:] for s in board_keys]
    if not all(elem in column for elem in board_column):
        return False
    
    # Check if the name of the chess piece starts with a "w" or "b"
    for pieces in piece.values():
        if pieces[0] != 'b' or pieces[0] != 'w':
            return False
    
    # Check the distinct names of the pieces
    pieces_name = ['pawn', 'rook', 'bishop', 'king', 'queen', 'knight']
    for name in piece.values():
        if name[1:] not in pieces_name:
            return False

# Testing function
print(isValidChessBoard(chess_pieces, {'h1': 'wrook'}))