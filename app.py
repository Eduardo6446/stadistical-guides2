from itertools import combinations, permutations
from scipy.special import comb
import math
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        #GUIA 3
        x = [2, 3, 5, 7]
        lista = list(combinations(x, 3))
        result = comb(9, 4, exact=True)
        result1 = math.factorial(5)
        length_lista = len(lista)
        permutaciones_x = list(permutations(x))
        strings = ["Juan", "Pedro", "Pablo"]
        combinaciones_strings_2 = list(combinations(strings, 2))
        #GUIA 5
        # Definir los vectores de probabilidades
        pb = np.array([0.5, 0.3, 0.2])
        pab = np.array([0.04, 0.03, 0.02])
        # Calcular la probabilidad total de A
        pa = np.sum(pb * pab)
        pba = (pb * pab) / pa

        resultado = {
            'combinaciones':lista,
            'comb':result,
            'facotial':result1,
            'l':length_lista,
            'per':permutaciones_x,
            'str':combinaciones_strings_2,
            #guia 5
            'pb':pb,
            'pab':pab,
            'pa':pa,
            'pba':pba
        }
        
        return render_template('index.html', resultado=resultado)
    else:
        return render_template('index.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
