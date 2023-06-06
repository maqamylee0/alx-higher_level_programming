import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
if not isinstance(sys.argv[1], int):
    print("N must be a number")
    sys.exit(1)
if sys.argv[1] < 4:
    print("N must be at least 4")
    sys.exit(1)
