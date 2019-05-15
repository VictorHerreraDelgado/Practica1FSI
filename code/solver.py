#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymzn
import numpy as np
import time

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    data = dict()
    first_line = lines[0].split()
    data.update({'nNodos': int(first_line[0])})
    data.update({'nRelaciones': int(first_line[1])})

    edges = []
    for i in range(1, data['nRelaciones'] + 1):
        line = lines[i]
        parts = line.split()
        edges.append({int(parts[0]), int(parts[1])})


    flat_list = [item for sublist in edges for item in sublist]
    counts = [flat_list.count(number) for number in range(int(first_line[0]))]
    maxNode = np.argmax(np.array(counts))
    data.update({'fix_node': maxNode})
    data.update({'parejas': edges})
    #pprint(dzn)
    toc = time.time()
    solution = pymzn.minizinc('ejercicioColores.mzn', data=data)
    tic = time.time()
    solution = solution[0]['colors'].values()
    #print(solution[0])
    # build a trivial solution
    # every node has its own color
    #solution = range(0, node_count)

    # prepare the solution in the specified output format
    output_data = str(data['nNodos']) + ' ' + str(0)
    output_data += ' ' + str(len(set(solution))) + '\n'
    output_data += ' '.join(map(str, solution)) + '\n'
    output_data += 'time: {}s'.format(tic - toc)
    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

