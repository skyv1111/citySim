import pygame

# Initialize Pygame
pygame.init()

# Define dimensions and settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
GRID_WIDTH, GRID_HEIGHT = 3000, 1600
TILE_WIDTH, TILE_HEIGHT = 60, 40
cameraX, cameraY, cameraTargetX, cameraTargetY, cameraSpeed = 0, 0, 0, 0, 0.1
gridAlpha, fadeSpeed, fadeDirection = 255, 10, 0

# Set up screen, clock, and images
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("City Simulator")
clock = pygame.time.Clock()
backgroundImage = pygame.image.load("assets/images/misc/background.png").convert_alpha()
gridImage = pygame.image.load("assets/images/misc/grid_tiles.png").convert_alpha()

# Load and scale the UI image to take up 15% of the screen height and full width
ui_image = pygame.image.load("assets/images/ui/ui_bg.png").convert_alpha()
ui_height = int(SCREEN_HEIGHT * 0.15)
ui_image = pygame.transform.scale(ui_image, (SCREEN_WIDTH, ui_height))

# Pre-render grid surface
gridSurface = pygame.Surface((GRID_WIDTH, GRID_HEIGHT), pygame.SRCALPHA)
gridSurface.blit(gridImage, (0, 0))

# Convert mouse coords to grid coords
def mouse_to_grid_coords(x, y): return (x + cameraX) // TILE_WIDTH, (y + cameraY) // TILE_HEIGHT
def grid_to_mouse_coords(x, y): return (x * TILE_WIDTH) - cameraX, (y * TILE_HEIGHT) - cameraY

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Check if the UI image area is clicked
            if SCREEN_HEIGHT - ui_height <= mouse_y <= SCREEN_HEIGHT:
                print("Pressed UI")
            else:
                grid_x, grid_y = mouse_to_grid_coords(*pygame.mouse.get_pos())
                print(f"Clicked on tile at grid position: ({grid_x}, {grid_y})")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_g] and fadeDirection == 0:
        fadeDirection = 1 if gridAlpha == 0 else -1
    if fadeDirection:
        gridAlpha += fadeSpeed if fadeDirection == 1 else -fadeSpeed
        gridAlpha = max(0, min(255, gridAlpha))
        fadeDirection = 0 if gridAlpha in {0, 255} else fadeDirection
    gridSurface.set_alpha(gridAlpha)

    # Camera movement and smoothing
    cameraTargetX += (keys[pygame.K_d] - keys[pygame.K_a]) * 10
    cameraTargetY += (keys[pygame.K_s] - keys[pygame.K_w]) * 10
    cameraTargetX, cameraTargetY = max(0, min(GRID_WIDTH - SCREEN_WIDTH, cameraTargetX)), max(0, min(GRID_HEIGHT - SCREEN_HEIGHT, cameraTargetY))
    cameraX += (cameraTargetX - cameraX) * cameraSpeed
    cameraY += (cameraTargetY - cameraY) * cameraSpeed

    # Drawing
    screen.fill((0, 0, 0))  # Clear the screen each frame (black background)
    screen.blit(backgroundImage, (0, 0), (cameraX, cameraY, SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(gridSurface, (0, 0), (cameraX, cameraY, SCREEN_WIDTH, SCREEN_HEIGHT))

    # Draw the UI image at the bottom
    screen.blit(ui_image, (0, SCREEN_HEIGHT - ui_height))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
