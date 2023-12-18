import numpy as np
import random

def droplet_movement():
    x = np.linspace(start=2, stop=213.996, num=800)
    y = -0.2/(x-214)
    return x, y

def dopant_pos():
    pos = []
    for i in range(20):
        pos.append((random.randint(50, 103), random.randint(-14, 14)))
    for i in range(5):
        pos.append((random.randint(65, 88), random.randint(16, 29)))
    for i in range(5):
        pos.append((random.randint(65, 88), random.randint(-29, -16)))
    return pos

def helium_pos():
    pos = []
    for i in range(15):
        pos.append((random.randint(170, 204), random.randint(-4, 4)))
    for i in range(8):
        pos.append((random.randint(172, 172), random.randint(-4, 27)))
    return pos