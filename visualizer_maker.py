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
import Points
from datetime import datetime
# ----------------------------------------------


start_time = datetime.now()

points = [\n'''



    point_file = open(point_file_name, 'w')
    point_file.write(point_file_header)
    with open(file_path, 'r') as f:
        for data in f:
            index_start = len(data) - data[::-1].find(':')
            index_end = data.find('[')
            x,y,z= data[index_start:index_end].replace(' ', '').split(',')

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
# Cloud
# ----------------------------------------------
cloud = Points.Points()
cloud.addPoints(points)
# ----------------------------------------------

# ----------------------------------------------
# View
# ----------------------------------------------
obj=App.ActiveDocument.addObject("Points::Feature")
obj.Points=cloud
App.ActiveDocument.recompute()
obj.ViewObject.PointSize=3.0
obj.ViewObject.ShapeColor=(1.,0.,0.)
# ----------------------------------------------


term_time = datetime.now()
print('Term Time {}'.format(str(term_time - start_time)))


'''
    point_file.write(processing)
            

if __name__ == '__main__':
    main()
