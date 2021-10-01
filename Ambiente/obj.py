import struct
from lib import *

class Obj(object):
    def __init__(self, filename, opcion):
        with open(filename) as f:
            self.lines = f.read().splitlines()

        self.vertices = []
        self.tvertices = []
        self.normales = []
        self.faces = []
        self.opcion = opcion
        self.read()

    def read(self):
        maxy = 0
        maxx = 0
        maxz = 0
        
        miny = 0
        minx = 0
        minz = 0
        for line in self.lines:        
            if line:
                try:
                    prefix, value = line.split(' ', 1)
                except:
                    prefix = ''            
                if prefix == 'v':
                    if self.opcion == True:
                        vertice = list(map(float, value.split(' ')))
                        self.vertices.append(vertice)
                        if vertice[0]>maxx:
                            maxx = vertice[0]
                        if vertice[1]>maxy:
                            maxy = vertice[1]
                        if vertice[2]>maxz:
                            maxz = vertice[2]
                        if vertice[0]<minx:
                            minx = vertice[0]
                        if vertice[1]<miny:
                            miny = vertice[1]
                        if vertice[2]<minz:
                            minz = vertice[2]
                    else:
                        self.vertices.append(
                            list(map(float, value.split(' '))))                    
                elif prefix == 'vt':
                    self.tvertices.append(
                        list(map(float, value.split(' ')))
                  )
                elif prefix == 'vn':
                    self.normales.append(
                        list(map(float, value.split(' ')))
                  )
                elif prefix == 'f':
                    self.faces.append(
                        [list(map(int, face.split('/'))) for face in value.split(' ')]
                    )
        if self.opcion == True:
            if maxx == 0:
                maxx = -1 * minx
            if maxy == 0:
                maxy = -1 * miny
            if maxz == 0:
                maxz = -1 * minz
                
            self.vertexN = [[i[0]/maxx, i[1]/maxy, i[2]/maxz] for i in self.vertices]
            self.vertices = self.vertexN

class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()
    
    def read(self):
        image = open(self.path, 'rb')
        
        image.seek(10)
        headerSize = struct.unpack('=l', image.read(4))[0]

        image.seek(18)
        self.width = struct.unpack('=l', image.read(4))[0]
        self.height = struct.unpack('=l', image.read(4))[0]
        image.seek(headerSize)
        self.pixels = []
        
        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(image.read(1))
                g = ord(image.read(1))
                r = ord(image.read(1))
                self.pixels[y].append(color(r, g, b))
        image.close()
        
    def get_color(self, tx, ty):
        x = int(tx * self.width)
        y = int(ty * self.height)
        try:
            return self.pixels[y][x]
        except:
            return color(255, 255, 255)
        

    
    
    
    
    
    