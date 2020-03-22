import os


def listArq():
    listaArq = []
    for arquivo in os.listdir('dochumb'):
        listaArq.append(str(arquivo))
    return listaArq


def extractName(lista):
    names = []
    for filename in lista:
        names.append(filename.split('.')[0])
    return names


def read_meta_data(path):
    data = open(path, "rt")
    meta_data = []
    for line in data:
        line_data = line.split('\t')
        meta_data.append((line_data[0], line_data[1], line_data[2]))
    data.close()
    return meta_data