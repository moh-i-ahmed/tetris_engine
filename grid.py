class Grid:
    
    def __init__(self) -> None:
        self.width = 10
        self.clear()

    # TODO
    def add_piece(self, piece):
        return

    # TODO 
    def calculate_height(self):
        return

    def clear(self) -> None:
        self.cells = [ [0] * self.width for _ in range(self.width) ]