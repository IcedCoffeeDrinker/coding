import pygame
import numpy as np
import wireframe

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

    A0 = np.random.randint(0, repeat)
    A1 = (A0 + 1) % repeat
    B0 = np.random.randint(0, repeat)
    B1 = (B0 + 1) % repeat

    G_A0 = gradient(A0, x)
    G_A1 = gradient(A1, x - 1)
    G_B0 = gradient(B0, x)
    G_B1 = gradient(B1, x - 1)

    return lerp(lerp(G_A0, G_A1, u), lerp(G_B0, G_B1, u), u)



pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("3D Wireframe Engine")
clock = pygame.time.Clock()

terrain_size = 100
terrain_scale = 5
noise_scale = 0.1

terrain = wireframe.Wireframe()
for x in range(terrain_size):
    for y in range(terrain_size):
        h = perlin_noise(np.array([x * noise_scale, y * noise_scale])) * terrain_scale
        terrain.add_vertex((x, y, h))

for x in range(terrain_size - 1):
    for y in range(terrain_size - 1):
        terrain.add_edge(x * terrain_size + y, x * terrain_size + y + 1)
        terrain.add_edge(x * terrain_size + y, (x + 1) * terrain_size + y)

# Player
player = wireframe.Vertex(0, 0, 0)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= 1
    if keys[pygame.K_s]:
        player.y += 1
    if keys[pygame.K_a]:
        player.x -= 1
    if keys[pygame.K_d]:
        player.x += 1

    # Render
    screen.fill((0, 0, 0))
    terrain.draw(screen, player)
    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()
