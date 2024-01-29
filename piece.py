class Piece:

    SHAPES = {
        'Q': ((1, 1), (1, 1)),
        'Z': ((1, 1, 0), (0, 1, 1)),
        'S': ((0, 1, 1), (1, 1, 0)),
        'T': ((1, 1, 1), (0, 1, 0)),
        'I': ((1, 1, 1, 1),),
        'L': ((1, 0), (1, 0), (1, 1)),
        'J': ((0, 1), (0, 1), (1, 1))
    }

    def __init__(self, shape, position) -> None:
        self.shape = shape
        self.position = position
    

    @classmethod
    def create(cls, piece_type, position):
        shape = cls.SHAPES[piece_type]
        return cls(shape, position)
