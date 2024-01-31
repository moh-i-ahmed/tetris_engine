#!/usr/bin/python

from tetris import TetrisEngine
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--use-file":
        run_from_text_file()
    else:
        run_from_stdin()
    

    
def run_from_stdin() -> None:
    engine = TetrisEngine()

    for line in sys.stdin:
        # clear grid for new inputs
        engine.clear_grid()

        pieces = line.strip().split(',')
        for piece in pieces:
            piece_type, position = piece[0], int(piece[1])
            engine.add_piece(piece_type, position)

        grid_height = str(engine.get_grid_height())
        sys.stdout.write(grid_height + '\n')
    
    return


def run_from_text_file() -> None:
    engine = TetrisEngine()
    input_file, output_file = 'input.txt', 'output.txt'

    with open(input_file, 'r') as file: lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            # clear grid for new inputs
            engine.clear_grid()

            pieces = line.strip().split(',')
            for piece in pieces:
                piece_type, position = piece[0], int(piece[1])
                engine.add_piece(piece_type, position)

            grid_height = str(engine.get_grid_height())
            file.write(grid_height + '\n')
            
            print(f"\nInput: {line.strip()}")
            print(f"Output: {grid_height}")
            print("Grid state:")
            for row in engine.grid.cells: print(' '.join(str(cell) for cell in row))

    return


if __name__ == "__main__":
    main()
