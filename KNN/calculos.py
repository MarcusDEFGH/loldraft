import math
import numpy as np

def somar(valores):
    soma = 0
    for v in valores:
        soma += v
    return soma


def media(valores):
    soma = somar(valores)
    qtd_elementos = len(valores)
    media = soma / float(qtd_elementos)
    return media


def variancia(valores):
    _media = media(valores)
    soma = 0
    _variancia = 0

    for valor in valores:
        soma += math.pow( (valor - _media), 2)
    _variancia = soma / float( len(valores) )
    return _variancia


def desvio_padrao(valores):
    return math.sqrt( variancia(valores) )


a = [0.702, 0.722, 0.732, 0.715, 0.749, 0.726, 0.741, 0.707, 0.698, 0.734, 0.722, 0.695, 0.683, 0.729, 0.725, 0.683]
a = [0.7182973213563163, 0.7143319575948854, 0.7176499150279194, 0.7157886218337784, 0.7259043457149794, 0.7223436109087966]
print('media = ' + str(media(a)))
print('desvio_padrao = ' + str(desvio_padrao(a)))
print('variancia = ' + str(variancia(a)))
print('erro medio = ' + str(np.mean(a)**2))
