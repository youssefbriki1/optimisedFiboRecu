import sys
from Fibo import Fibo

if __name__ == "__main__":
    calcul = Fibo(int(sys.argv[1]))
    print(calcul)
