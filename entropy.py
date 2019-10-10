#!/usr/bin/env python3
import math
import sys
from PIL import Image
import numpy as np


def H(data):
    ''' Calculate the entropy of a given data block '''
    entropy = 0
    for x in range(256):
        p_x = data.count((x).to_bytes(1, 'little'))/len(data)
        if p_x > 0:
            entropy += -p_x*math.log(p_x, 2)
    return entropy

def block_entropy(data, block_size):
    ''' Generator for calculating the entropy of a file,
        given a size for the data blocks '''
    for x in range(0, len(data)//block_size):
        start = x * block_size
        end = start + block_size
        yield H(data[start:end])

def graph(matrix):
    ''' Saves an image of the entropy matrix '''
    arr = np.array(matrix)
    im = Image.fromarray(arr * 255/8).convert('L')
    im.save(f'{filename}_entropy.png')
    print(f'Generated {len(matrix)}:{len(matrix[0])} image')
    print(f'Imaged saved as {filename}_entropy.png')
    print('-------- FINISHED ---------')
    return

if __name__ == '__main__':
    if (len(sys.argv) < 1 or len(sys.argv) > 3):
        print('''
        Usage: ./entropy [FILENAME] <BLOCKSIZE INT>(optional)
        ''')
        sys.exit(1)
    try:
        print('------- RUNNING --------')
        with open(sys.argv[1], 'rb') as f:
            if len(sys.argv) > 2:
                filename = sys.argv[1]
                block_size = int(sys.argv[2])
            else:
                filename = sys.argv[1]
                block_size = 256

            entropy_list = []
            data = f.read()
            for b in block_entropy(data, block_size):
                entropy_list.append(b)
            sq = int(math.sqrt(len(entropy_list)))
            matrix = [entropy_list[i*sq:i*sq+sq] for i in range(0, sq)]
            graph(matrix)
            sys.exit(0)
    except Exception as e:
        print('Failed execution. Unexpected error:')
        print(e)
        sys.exit(1)
