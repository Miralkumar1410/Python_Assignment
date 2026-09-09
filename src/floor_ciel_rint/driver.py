import numpy

from floor_ciel_rint.util import floor_ceil_rint
if __name__ == '__main__':

    array = numpy.array(input().split(), float)
    numpy.set_printoptions(legacy='1.13')
    floor_ceil_rint(array)