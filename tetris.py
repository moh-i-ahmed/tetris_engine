from piece import Piece
from grid import Grid

class TetrisEngine:
    
    def __init__(self) -> None:
        self.grid = Grid()


    def add_piece(self, piece_type, position) -> None:
        piece = Piece.create(piece_type, position)
        self.grid.add_piece(piece)
        return


    def get_grid_height(self) -> int:
        return self.grid.calculate_height()


    def clear_grid(self) -> None:
        self.grid.clear()
        return