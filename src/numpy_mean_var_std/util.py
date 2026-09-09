import numpy


def tools(n):
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    mat = numpy.array(arr)

    mean = numpy.mean(mat, axis=1).tolist()
    var = numpy.var(mat, axis=0).tolist()
    std = round(float(numpy.std(mat, axis=None)), 11)

    return mean, var, std