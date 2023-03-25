import numpy as np
import matplotlib.pyplot as plt

from leitorarquivo import LeitorArquivo

def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)
    plt.plot(valores)
    plt.show()

main()