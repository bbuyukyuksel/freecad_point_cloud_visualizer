# func = "Draft.makePoint({},{},{},({},{},{}),point_size={})".format(*point, *rgb, size)
def main():
    file_path = 'mech.db'
    point_file_name = 'db.point'
    point_file_header = '''# -*- coding: utf-8 -*-

# Creator     : @Burak Büyükyüksel
# Script Name : @DB Point File
# ----------------------------------------------
# Imports
# ----------------------------------------------
import Draft
from datetime import datetime
from multiprocessing.pool import ThreadPool
import multiprocessing
# ----------------------------------------------


start_time = datetime.now()

def apply(point):
    r,g,b = (1.,0.,0.)
    size = 5
    x,y,z = point
    Draft.makePoint(x,y,z,(r,g,b),point_size=size)

points = [\n'''



    point_file = open(point_file_name, 'w')
    point_file.write(point_file_header)
    with open(file_path, 'r') as f:
        for data in f:
            splited_data = data.split('\t')
            *_, x,y,z, _ = splited_data
            point = (x,y,z)
            if 'x' in point:
                continue
            #for i,splited in enumerate(splited_data):
            #    print(i, splited) 
            #func = "\t'Draft.makePoint({},{},{},({},{},{}),point_size={})'".format(*point, *rgb, size)
            points = "\t({},{},{})".format(*point)
            point_file.write(points + ',\n')
    point_file.write(']')
    
    processing = '''

# ----------------------------------------------
# Multiprocessing
# ----------------------------------------------
multiprocessing.freeze_support()
pool = ThreadPool(processes=16)
pool.map(apply, points)
# ----------------------------------------------

term_time = datetime.now()
print('Term Time {}'.format(str(term_time - start_time)))


'''
    point_file.write(processing)
            

if __name__ == '__main__':
    main()
