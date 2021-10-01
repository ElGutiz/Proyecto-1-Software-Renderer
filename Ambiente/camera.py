from gl import *
import random
from random import randint

def gourad(render, **kwargs):
    w, v, u = kwargs['bar']
    tx, ty = kwargs['tex_coords']
    nA, nB, nC = kwargs['varying_normales']
    
    tcolor = render.current_texture.get_color(tx, ty)

    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    
    intensity = w*iA + v*iB + u*iC
    
    return tcolor * intensity

def grass_color(render, **kwargs):
    w, v, u = kwargs['bar']
    nA, nB, nC = kwargs['varying_normales']
    A, B, C = kwargs['triangle']

    tcolor = color(121, 173, 83)
    
    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    
    intensity = w*iA + v*iB + u*iC
    
    return tcolor * intensity

def mountain_color(render, **kwargs):
    w, v, u = kwargs['bar']
    nA, nB, nC = kwargs['varying_normales']
    A, B, C = kwargs['triangle']
    
    if A.y < 600:
        tcolor = color(92, randint(78, 88), randint(60, 70))
    else:
        tcolor = color(201, 201, 201)
    
    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    
    intensity = w*iA + v*iB + u*iC
    
    return tcolor * intensity

def rock_color(render, **kwargs):
    w, v, u = kwargs['bar']
    nA, nB, nC = kwargs['varying_normales']
    A, B, C = kwargs['triangle']
    
    tcolor = color(145, 145, 145)
    
    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    
    intensity = w*iA + v*iB + u*iC
    
    return tcolor * intensity

pi = 3.14
j = 0
e = 0
white = color(255, 255, 255)

p_f = 0
x_slide = 0

p_b = 0
x_slide_b = 0

p_b_b = 0
x_slide_b_b = 0

r = Renderer(1000, 1000)
r.lookAt(V3(0, 0, 5), V3(0, 0, 0), V3(0, 1, 0))

#---------------------------ESTRELLAS---------------------
while e < 500:
    r.point(randint(10, 999), randint(400, 999), white)
    e += 1
    
#---------------------------LUNA---------------------------
r.current_texture = Texture('./models/Sphere_texture.bmp')
r.light = V3(-1, 0, 0)
r.load('./models/Sphere.obj', (-0.6, 0.5, 0), (0.15, 0.15, 0.15), (0, pi/2, 0), True)
r.active_shader = gourad
r.draw_arrays('TRIANGLES')

#---------------------------VENADO #1---------------------------
r.current_texture = Texture('./models/DeerTexture.bmp')
r.light = V3(-0.5, 0.5, 0.05)
r.load('./models/Deeeer.obj', (0.7, -0.6, 0.5), (0.11, 0.11, 0.11), (0, pi/2, 0), True)
r.active_shader = gourad
r.draw_arrays('TRIANGLES')

#---------------------------VENADO #2---------------------------
r.current_texture = Texture('./models/DeerTexture.bmp')
r.light = V3(0.5, 0.5, -0.05)
r.load('./models/Deeeer.obj', (0.5, -0.6, 0.4), (0.11, 0.11, 0.11), (0, -pi/6, 0), True)
r.active_shader = gourad
r.draw_arrays('TRIANGLES')

#---------------------------VENADO #3---------------------------
r.current_texture = Texture('./models/DeerTexture.bmp')
r.light = V3(0.5, 0.5, -0.05)
r.load('./models/Deeeer.obj', (0.35, -0.6, 0), (0.11, 0.11, 0.11), (0, -5*pi/6, 0), True)
r.active_shader = gourad
r.draw_arrays('TRIANGLES')

#---------------------------CHOZA---------------------------
r.current_texture = Texture('./models/Diffuse_map_f.bmp')
r.light = V3(-0.4, 0.6, 0.3)
r.load('./models/Alpine_chalett.obj', (-0.40, -0.6, -1), (0.40, 0.40, 0.40), (0, pi/10, 0), True)
r.active_shader = gourad
r.draw_arrays('TRIANGLES')

#---------------------------PIEDRAS------------------------
r.current_texture = None
r.light = V3(-0.4, 0.6, 0.3)
r.load('./models/RockF.obj', (0.1, -0.7, 0.5), (0.15, 0.15, 0.15), (0, pi/10, 0), True)
r.active_shader = rock_color
r.draw_arrays('TRIANGLES')

r.load('./models/RockF.obj', (0.8, -0.7, -0.9), (0.25, 0.15, 0.15), (0, 0, 0), True)
r.active_shader = rock_color
r.draw_arrays('TRIANGLES')

r.load('./models/RockF.obj', (-1.4, -0.75, -0.9), (0.45, 0.25, 0.25), (0, 0, 0), True)
r.active_shader = rock_color
r.draw_arrays('TRIANGLES')

#---------------------------GRAMA---------------------------
r.current_texture = None
r.light = V3(0.5, 0.5, -0.5)

while j < 850: 
    r.load('./models/grassD.obj', (round(random.uniform(0.04, 0.99), 2), -0.6, round(random.uniform(-1.5, 2), 2)), (0.04, round(random.uniform(0.04, 0.08), 2), 0.04), (-pi/10, pi/randint(1, 5), 0), True)
    r.active_shader = grass_color
    r.draw_arrays('TRIANGLES')
    j += 1

j =0
while j < 200: 
    r.load('./models/grassD.obj', (round(random.uniform(-0.6, 0), 2), -0.6, round(random.uniform(1.2, 1.9), 2)), (0.04, round(random.uniform(0.04, 0.08), 2), 0.04), (-pi/10, pi/randint(1, 5), 0), True)
    r.active_shader = grass_color
    r.draw_arrays('TRIANGLES')
    j += 1

j = 0
while j < 400: 
    r.load('./models/grassD.obj', (round(random.uniform(-1.2, 1.2), 2), -0.6, round(random.uniform(-2, -0.9), 2)), (0.04, round(random.uniform(0.04, 0.08), 2), 0.04), (-pi/10, pi/randint(1, 5), 0), True)
    r.active_shader = grass_color
    r.draw_arrays('TRIANGLES')
    j += 1

j = 0
while j < 100:
    z = randint(-15, 195)
    x = -60
    if z < 50:
        x -= randint(20, 40)
    if z >= 50 and z < 100:
        x -= randint(8, 20)
    if z >= 100 and z < 150:
        x -= randint(0, 15)
    if z >= 150 and z < 170:
        x -= randint(0, 8)
    r.load('./models/grassD.obj', (x/100, -0.6, z/100), (0.04, round(random.uniform(0.04, 0.08), 2), 0.04), (-pi/10, pi/randint(1, 5), 0), True)
    r.active_shader = grass_color
    r.draw_arrays('TRIANGLES')
    j += 1

#---------------------------MONTAÑA FINAL---------------------------
r.current_texture = None
r.light = V3(1, -0.5, -0.5)
r.load('./models/MountainD.obj', (0, -0.6, -2.9), (1.5, 1.5, 1.5), (0, pi/2, 0), True)
r.active_shader = mountain_color
r.draw_arrays('TRIANGLES')

#------------------------------PINOS-------------------------------
r.current_texture = Texture('./models/TreePineTexture.bmp')
r.light = V3(-0.4, 0.4, 0.4)

while p_f < 10:
    r.load('./models/PineTree.obj', (-1 + x_slide, -0.6, -1.1), (0.2, 0.45, 0.2), (pi/20, 0, 0), True)
    r.active_shader = gourad
    r.draw_arrays('TRIANGLES')
    x_slide += round(random.uniform(0.2, 0.3), 2) 
    p_f += 1

while p_b < 13:
    r.light = V3(-0.25, 0.25, 0.25)
    r.load('./models/PineTree.obj', (-1.2 + x_slide_b, -0.6, -1.2), (0.2, 0.45, 0.2), (pi/20, 0, 0), True)
    r.active_shader = gourad
    r.draw_arrays('TRIANGLES')
    x_slide_b += round(random.uniform(0.1, 0.3), 2) 
    p_b += 1

while p_b_b < 19:
    r.light = V3(-0.1, 0.1, 0.1)
    r.load('./models/PineTree.obj', (-1.3 + x_slide_b_b, -0.6, -1.3), (0.2, 0.45, 0.2), (pi/20, 0, 0), True)
    r.active_shader = gourad
    r.draw_arrays('TRIANGLES')
    x_slide_b_b += round(random.uniform(0.1, 0.2), 2) 
    p_b_b += 1

r.render()
