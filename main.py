import sys
from fibo_recu_optimised.optimisedFiboRecu.Fibo import Fibo

if __name__ == "__main__":
    calcul = Fibo(sys.argv[1])
    print(calcul)
