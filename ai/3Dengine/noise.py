import numpy as np

def lerp(a, b, x):
    return a + x * (b - a)

def fade(t):
    return 6 * t**5 - 15 * t**4 + 10 * t**3

def gradient(h, x):
    h = h & 15
    g = 1 + (h & 7) if h < 8 else -1 - (h & 7)
    return g * x if h < 4 else g * x

def perlin_noise(x, repeat=256):
    x = np.array(x)
    X = (x // 1) % repeat
    x = x % 1
    u = fade(x)
    A = np.random.randint(0, repeat, len(x))
    B = (A + 1) % repeat
    return lerp(gradient(A, x), gradient(B, x - 1), u)
