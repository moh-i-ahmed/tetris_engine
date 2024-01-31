# Tetris Engine

**Author**: [Mohammed Ibrahim Ahmed](https://www.linkedin.com/in/moh-i-ahmed/) | [github.com/moh-i-ahmed](https://github.com/moh-i-ahmed)

**Description**: My implementation of the Tetris programming challenge to create a simplified Tetris engine.

## Pre-requisites/Setup

The following run instructions have been tested on Windows 11 and Ubuntu 22.04.3 LTS.

If you're running on Windows,  you'l need to create an executable using the following instructions. There's already a provided executable for Ubuntu but the steps are included as well.

### How to create an executable

1. Install pyinstaller using pip.
    - ```pip install pyinstaller```

2. Create the executable using the following command.
    - ```pyinstaller --onefile main.py --name=tetris```

3. The created executable will be stored in the **/dist** folder with the name:
    - ***tetrix.exe*** for Windows
    - ***tetrix*** for Ubuntu/Linux

### Run instructions

**Normal mode:** Run the provided executable files in the **/dist** folder.

- (**Windows**) ```type <input.txt> | .\dist\tetris.exe > output.txt```
- (**Ubuntu**) ```cat input.txt | .\dist\tetris > output.txt```

**Dev mode**: Provides more insight into the Tetris engine state.

- (**Optional**) Place a different **input.txt** file in the main folder (**/tetris_engine**)

- Run the *main.py* file directly. The command works for both Windows & Ubuntu.
  - ```python main.py --use-file```
