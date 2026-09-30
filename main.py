# import pygame
# from game.game_engine import GameEngine

# # Initialize pygame/Start application
# pygame.init()

# # Screen dimensions
# WIDTH, HEIGHT = 640, 560
# SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Brick Breaker - Pygame Version")

# # Clock
# clock = pygame.time.Clock()
# FPS = 60

# # Game loop
# engine = GameEngine(WIDTH, HEIGHT)

# def main():
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             engine.handle_event(event)

#         engine.handle_input()
#         engine.update()
#         engine.render(SCREEN)

#         pygame.display.flip()
#         clock.tick(FPS)

#     pygame.quit()

# if __name__ == "__main__":
#     main()

#task 2
# import pygame
# from game.game_engine import GameEngine


# # Initialize pygame
# pygame.init()


# # Screen dimensions
# WIDTH, HEIGHT = 640, 560


# # Create screen
# SCREEN = pygame.display.set_mode(
#     (WIDTH, HEIGHT)
# )

# pygame.display.set_caption(
#     "Brick Breaker - Pygame Version"
# )


# # Clock
# clock = pygame.time.Clock()
# FPS = 60


# # Create game engine
# engine = GameEngine(
#     WIDTH,
#     HEIGHT
# )


# def main():

#     running = True

#     while running:

#         # -----------------------------------------------------
#         # Handle events
#         # -----------------------------------------------------
#         for event in pygame.event.get():

#             if event.type == pygame.QUIT:

#                 running = False

#             # -------------------------------------------------
#             # Game Over input
#             # -------------------------------------------------
#             if (
#                 engine.game_over
#                 and event.type
#                 == pygame.KEYDOWN
#             ):

#                 # Press ESC to exit
#                 if event.key == pygame.K_ESCAPE:

#                     running = False

#                 # Press ENTER
#                 elif event.key == pygame.K_RETURN:

#                     # For Task 2, ENTER exits
#                     # Task 3 will add replay options
#                     running = False

#             engine.handle_event(event)

#         # -----------------------------------------------------
#         # Game input
#         # -----------------------------------------------------
#         engine.handle_input()

#         # -----------------------------------------------------
#         # Update game
#         # -----------------------------------------------------
#         engine.update()

#         # -----------------------------------------------------
#         # Draw game
#         # -----------------------------------------------------
#         engine.render(SCREEN)

#         # Update display
#         pygame.display.flip()

#         # Maintain FPS
#         clock.tick(FPS)

#     # Quit pygame
#     pygame.quit()


# # Start program
# if __name__ == "__main__":
#     main()




#task 3

# import pygame
# from game.game_engine import GameEngine


# # Initialize pygame
# pygame.init()


# # Screen dimensions
# WIDTH, HEIGHT = 640, 560


# # Create screen
# SCREEN = pygame.display.set_mode(
#     (WIDTH, HEIGHT)
# )

# pygame.display.set_caption(
#     "Brick Breaker - Pygame Version"
# )


# # Clock
# clock = pygame.time.Clock()
# FPS = 60


# # Create game engine
# engine = GameEngine(
#     WIDTH,
#     HEIGHT
# )


# def main():

#     running = True

#     while running:

#         # -----------------------------------------------------
#         # Events
#         # -----------------------------------------------------
#         for event in pygame.event.get():

#             if event.type == pygame.QUIT:

#                 running = False

#             # Send event to game engine
#             engine.handle_event(event)

#         # -----------------------------------------------------
#         # Input
#         # -----------------------------------------------------
#         engine.handle_input()

#         # -----------------------------------------------------
#         # Update
#         # -----------------------------------------------------
#         engine.update()

#         # -----------------------------------------------------
#         # Render
#         # -----------------------------------------------------
#         engine.render(SCREEN)

#         # Update screen
#         pygame.display.flip()

#         # Maintain FPS
#         clock.tick(FPS)

#     # Quit pygame
#     pygame.quit()


# # Run program
# if __name__ == "__main__":
#     main()

#task 4
import pygame
from game.game_engine import GameEngine


# ---------------------------------------------------------
# Initialize Pygame
# ---------------------------------------------------------
pygame.init()


# ---------------------------------------------------------
# Screen dimensions
# ---------------------------------------------------------
WIDTH, HEIGHT = 640, 560


# ---------------------------------------------------------
# Create screen
# ---------------------------------------------------------
SCREEN = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Brick Breaker - Pygame Version"
)


# ---------------------------------------------------------
# Clock
# ---------------------------------------------------------
clock = pygame.time.Clock()
FPS = 60


# ---------------------------------------------------------
# Create game engine
# ---------------------------------------------------------
engine = GameEngine(
    WIDTH,
    HEIGHT
)


# ---------------------------------------------------------
# Main game loop
# ---------------------------------------------------------
def main():

    running = True

    while running:

        # -------------------------------------------------
        # Handle events
        # -------------------------------------------------
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

            # Send event to game engine
            engine.handle_event(event)

        # -------------------------------------------------
        # Handle keyboard
        # -------------------------------------------------
        engine.handle_input()

        # -------------------------------------------------
        # Update game
        # -------------------------------------------------
        engine.update()

        # -------------------------------------------------
        # Draw game
        # -------------------------------------------------
        engine.render(SCREEN)

        # -------------------------------------------------
        # Update display
        # -------------------------------------------------
        pygame.display.flip()

        # -------------------------------------------------
        # Maintain FPS
        # -------------------------------------------------
        clock.tick(FPS)

    # -----------------------------------------------------
    # Quit Pygame
    # -----------------------------------------------------
    pygame.quit()


# ---------------------------------------------------------
# Start program
# ---------------------------------------------------------
if __name__ == "__main__":
    main()


