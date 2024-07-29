import numpy

def arrays(array):
    array = numpy.array([int(item) for item in array.split()])
    reshaped = numpy.reshape(array, (3, 3))
    return reshaped