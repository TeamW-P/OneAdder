import sys
from core.Adder import Adder

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit('Received an illegal number of arguments.')

    try:
        input = (int) (sys.argv[1])
    except ValueError:
         sys.exit('Received an invalid argument. Please enter an integer.')

    print(Adder.oneAdder(input))
