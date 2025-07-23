import numpy as np

def arraycreation (dtype, rows, columns, min, max): 

    if dtype :
        arrayfloat = np.random.rand(rows, columns)
        arrayint = np.random.randint(min, max, size=(rows, columns))
        fullarray = np.add(arrayfloat, arrayint)
        #print(arrayint)
        return fullarray
    else :
        max += 1
        arrayint = np.random.randint(min, max, size=(rows, columns))
        return arrayint