class Grid:
    def __init__(self) -> None:
        self.width = 10
        self.height = 20
        self.cells = [[0] * self.width for _ in range(self.height)]


    def add_piece(self, piece) -> None:
        # top down search for free position to add piece
        for row in range(self.height - len(piece.shape) + 1):
            # move down until collision or bottom of grid
            if not self._can_place_piece(piece, row + 1):
                self._place_piece(piece, row)
                break

        self._clear_filled_rows()

        return


    def clear(self) -> None:
        self.cells = [[0] * self.width for _ in range(self.height)]
        return


    def calculate_height(self) -> int:
        height = 0
        for row in self.cells:
            if any(cell > 0 for cell in row): height += 1

        return height


    def _can_place_piece(self, piece, start_row):
        for row_index, row in enumerate(piece.shape):
            for col_index, cell in enumerate(row):

                # get current position in grid
                grid_row = start_row + row_index
                grid_col = piece.position + col_index

                # check if within the bounds & empty
                if cell and ( (grid_row >= self.height) or (grid_col < 0) or (grid_col >= self.width) or (self.cells[grid_row][grid_col]) ): return False

        return True


    def _place_piece(self, piece, start_row) -> None:
        for row_index, row in enumerate(piece.shape):
            for col_index, cell in enumerate(row):
                if cell:
                    grid_row = start_row + row_index
                    grid_col = piece.position + col_index
                    self.cells[grid_row][grid_col] = 1
                    
        return


    def _clear_filled_rows(self) -> None:
        # pop filled rows
        self.cells = [row for row in self.cells if not all(row)]

        # add new empty rows to top
        while len(self.cells) < self.height: self.cells.insert(0, [0] * self.width)
        
        return
