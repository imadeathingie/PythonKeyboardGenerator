# PythonKeyboardGenerator

### Python + Config -> openSCAD

Define keyboard in defaults.py and note the index (0-based).

Algorithms support `x`, `y` (column/row), `abs`, `min`, and `max`.

Adjust `main.sh` to point to the openSCAD binary on your system.

cd to this directory and run:

`./main.sh <index>` or `./main.sh <start> <end>`.
