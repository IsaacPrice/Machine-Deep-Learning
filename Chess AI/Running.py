import tensorflow as tf

def print_board(board):
    reverse_mapping = {v: k for k, v in piece_mapping.items()}
    for row in board:
        row_symbols = [reverse_mapping.get(cell, ' ') for cell in row]
        print(' '.join(row_symbols))
    print("\n")

# Load the model
model = tf.keras.models.load_model('Chess AI/chessModel.h5')

# This is where the thingie gets extra complicated