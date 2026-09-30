# import pygame
# from .paddle import Paddle
# from .ball import Ball
# from .brick import Brick

# # Game Engine

# WHITE = (255, 255, 255)
# BG = (15, 15, 25)
# BRICK_COLORS = [
#     (200, 60, 60),
#     (200, 140, 60),
#     (200, 200, 60),
#     (80, 180, 80),
#     (80, 140, 200),
# ]

# class GameEngine:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#         self.paddle = Paddle(width // 2 - 50, height - 30, 100, 14)

#         self.ball = Ball(width // 2, height - 50, radius=8)
#         self.ball.vx, self.ball.vy = 4, -4

#         self.rows, self.cols = 5, 8
#         self.bricks = self._build_bricks(self.rows, self.cols)

#         self.lives = 3
#         self.score = 0
#         self.font = pygame.font.SysFont("Arial", 28)
#         self.game_over = False
#         self.result = None  # "win" or "lose"

#     def _build_bricks(self, rows, cols):
#         bricks = []
#         margin, gap, top = 30, 6, 60
#         brick_w = (self.width - margin * 2 - gap * (cols - 1)) // cols
#         brick_h = 22
#         for r in range(rows):
#             for c in range(cols):
#                 x = margin + c * (brick_w + gap)
#                 y = top + r * (brick_h + gap)
#                 bricks.append(Brick(x, y, brick_w, brick_h))
#         return bricks

#     def handle_event(self, event):
#         # This game only needs continuously-held-key input for the
#         # paddle, handled in handle_input each frame.
#         pass

#     def handle_input(self):
#         if self.game_over:
#             return
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT] or keys[pygame.K_a]:
#             self.paddle.move(-self.paddle.speed, self.width)
#         if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
#             self.paddle.move(self.paddle.speed, self.width)

#     def update(self):
#         if self.game_over:
#             return

#         self.ball.move()

#         if self.ball.x - self.ball.radius <= 0 or self.ball.x + self.ball.radius >= self.width:
#             self.ball.vx *= -1
#         if self.ball.y - self.ball.radius <= 0:
#             self.ball.vy *= -1

#         if self.ball.rect().colliderect(self.paddle.rect()):
#             # NOTE: always flips the ball's vertical velocity on a
#             # paddle collision, regardless of which side of the paddle
#             # was actually hit. See Task 1 in the README.
#             self.ball.vy *= -1

#         for brick in self.bricks:
#             if brick.alive and self.ball.rect().colliderect(brick.rect()):
#                 brick.alive = False
#                 self.score += 1
#                 # NOTE: same unconditional vertical-velocity flip as
#                 # the paddle collision above - a brick hit from the
#                 # left or right should redirect the ball sideways
#                 # (flip vx), but this always flips vy instead. See
#                 # Task 1 in the README.
#                 self.ball.vy *= -1
#                 break

#         if self.ball.y - self.ball.radius > self.height:
#             self.lives -= 1
#             if self.lives <= 0:
#                 self.game_over = True
#                 self.result = "lose"
#             else:
#                 self._reset_ball()

#         if all(not b.alive for b in self.bricks):
#             self.game_over = True
#             self.result = "win"

#     def _reset_ball(self):
#         self.ball.x, self.ball.y = self.width // 2, self.height - 50
#         self.ball.vx, self.ball.vy = 4, -4

#     def render(self, screen):
#         screen.fill(BG)

#         pygame.draw.rect(screen, WHITE, self.paddle.rect())
#         pygame.draw.circle(screen, WHITE, (int(self.ball.x), int(self.ball.y)), self.ball.radius)

#         for i, brick in enumerate(self.bricks):
#             if brick.alive:
#                 row = i // self.cols
#                 color = BRICK_COLORS[row % len(BRICK_COLORS)]
#                 pygame.draw.rect(screen, color, brick.rect())

#         score_text = self.font.render(f"Score: {self.score}", True, WHITE)
#         screen.blit(score_text, (10, 10))
#         lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)
#         screen.blit(lives_text, (self.width - 130, 10))

#         if self.game_over and not getattr(self, "_game_over_logged", False):
#             # NOTE: no proper end screen yet - see Task 2 in the README.
#             if self.result == "win":
#                 print("You win! Final score:", self.score)
#             else:
#                 print("Game over! Final score:", self.score)
#             self._game_over_logged = True



#task 1
# import pygame
# from .paddle import Paddle
# from .ball import Ball
# from .brick import Brick

# # Colors
# WHITE = (255, 255, 255)
# BG = (15, 15, 25)

# BRICK_COLORS = [
#     (200, 60, 60),
#     (200, 140, 60),
#     (200, 200, 60),
#     (80, 180, 80),
#     (80, 140, 200),
# ]


# class GameEngine:

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#         # Paddle
#         self.paddle = Paddle(
#             width // 2 - 50,
#             height - 30,
#             100,
#             14
#         )

#         # Ball
#         self.ball = Ball(
#             width // 2,
#             height - 50,
#             radius=8
#         )

#         self.ball.vx = 4
#         self.ball.vy = -4

#         # Bricks
#         self.rows = 5
#         self.cols = 8
#         self.bricks = self._build_bricks(
#             self.rows,
#             self.cols
#         )

#         # Game information
#         self.lives = 3
#         self.score = 0

#         self.font = pygame.font.SysFont(
#             "Arial",
#             28
#         )

#         self.game_over = False
#         self.result = None

#     def _build_bricks(self, rows, cols):

#         bricks = []

#         margin = 30
#         gap = 6
#         top = 60

#         brick_w = (
#             self.width
#             - margin * 2
#             - gap * (cols - 1)
#         ) // cols

#         brick_h = 22

#         for r in range(rows):
#             for c in range(cols):

#                 x = margin + c * (brick_w + gap)
#                 y = top + r * (brick_h + gap)

#                 bricks.append(
#                     Brick(
#                         x,
#                         y,
#                         brick_w,
#                         brick_h
#                     )
#                 )

#         return bricks

#     def handle_event(self, event):
#         pass

#     def handle_input(self):

#         if self.game_over:
#             return

#         keys = pygame.key.get_pressed()

#         if keys[pygame.K_LEFT] or keys[pygame.K_a]:
#             self.paddle.move(
#                 -self.paddle.speed,
#                 self.width
#             )

#         if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
#             self.paddle.move(
#                 self.paddle.speed,
#                 self.width
#             )

#     # Determine which side of a rectangle was hit
#     def _collision_side(self, ball_rect, object_rect):

#         dx_left = abs(
#             ball_rect.right - object_rect.left
#         )

#         dx_right = abs(
#             object_rect.right - ball_rect.left
#         )

#         dy_top = abs(
#             ball_rect.bottom - object_rect.top
#         )

#         dy_bottom = abs(
#             object_rect.bottom - ball_rect.top
#         )

#         horizontal = min(dx_left, dx_right)
#         vertical = min(dy_top, dy_bottom)

#         if horizontal < vertical:
#             return "horizontal"

#         return "vertical"

#     def update(self):

#         if self.game_over:
#             return

#         # Move ball
#         self.ball.move()

#         ball_rect = self.ball.rect()

#         # Left and right walls
#         if (
#             self.ball.x - self.ball.radius <= 0
#             or
#             self.ball.x + self.ball.radius >= self.width
#         ):
#             self.ball.vx *= -1

#             self.ball.x = max(
#                 self.ball.radius,
#                 min(
#                     self.ball.x,
#                     self.width - self.ball.radius
#                 )
#             )

#         # Top wall
#         if self.ball.y - self.ball.radius <= 0:

#             self.ball.vy *= -1

#             self.ball.y = self.ball.radius

#         # Paddle collision
#         paddle_rect = self.paddle.rect()

#         if ball_rect.colliderect(paddle_rect):

#             side = self._collision_side(
#                 ball_rect,
#                 paddle_rect
#             )

#             if side == "horizontal":

#                 self.ball.vx *= -1

#             else:

#                 self.ball.vy *= -1

#                 # Make sure ball moves upward
#                 if self.ball.vy > 0:
#                     self.ball.vy *= -1

#             # Prevent repeated collision
#             self.ball.y = (
#                 self.paddle.y
#                 - self.ball.radius
#             )

#         # Brick collision
#         for brick in self.bricks:

#             if not brick.alive:
#                 continue

#             brick_rect = brick.rect()

#             if ball_rect.colliderect(brick_rect):

#                 # Find collision side
#                 side = self._collision_side(
#                     ball_rect,
#                     brick_rect
#                 )

#                 # Destroy brick
#                 brick.alive = False

#                 # Increase score
#                 self.score += 1

#                 # Correct bounce
#                 if side == "horizontal":

#                     self.ball.vx *= -1

#                 else:

#                     self.ball.vy *= -1

#                 break

#         # Ball falls below screen
#         if self.ball.y - self.ball.radius > self.height:

#             self.lives -= 1

#             if self.lives <= 0:

#                 self.game_over = True
#                 self.result = "lose"

#             else:

#                 self._reset_ball()

#         # Win condition
#         if all(
#             not brick.alive
#             for brick in self.bricks
#         ):

#             self.game_over = True
#             self.result = "win"

#     def _reset_ball(self):

#         self.ball.x = self.width // 2
#         self.ball.y = self.height - 50

#         self.ball.vx = 4
#         self.ball.vy = -4

#     def render(self, screen):

#         screen.fill(BG)

#         # Paddle
#         pygame.draw.rect(
#             screen,
#             WHITE,
#             self.paddle.rect()
#         )

#         # Ball
#         pygame.draw.circle(
#             screen,
#             WHITE,
#             (
#                 int(self.ball.x),
#                 int(self.ball.y)
#             ),
#             self.ball.radius
#         )

#         # Bricks
#         for i, brick in enumerate(self.bricks):

#             if brick.alive:

#                 row = i // self.cols

#                 color = BRICK_COLORS[
#                     row % len(BRICK_COLORS)
#                 ]

#                 pygame.draw.rect(
#                     screen,
#                     color,
#                     brick.rect()
#                 )

#         # Score
#         score_text = self.font.render(
#             f"Score: {self.score}",
#             True,
#             WHITE
#         )

#         screen.blit(
#             score_text,
#             (10, 10)
#         )

#         # Lives
#         lives_text = self.font.render(
#             f"Lives: {self.lives}",
#             True,
#             WHITE
#         )

#         screen.blit(
#             lives_text,
#             (self.width - 130, 10)
#         )

#task 2

# import pygame
# from .paddle import Paddle
# from .ball import Ball
# from .brick import Brick


# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (220, 60, 60)
# GREEN = (60, 220, 100)
# BG = (15, 15, 25)

# BRICK_COLORS = [
#     (200, 60, 60),
#     (200, 140, 60),
#     (200, 200, 60),
#     (80, 180, 80),
#     (80, 140, 200),
# ]


# class GameEngine:

#     def __init__(self, width, height):

#         self.width = width
#         self.height = height

#         # Paddle
#         self.paddle = Paddle(
#             width // 2 - 50,
#             height - 30,
#             100,
#             14
#         )

#         # Ball
#         self.ball = Ball(
#             width // 2,
#             height - 50,
#             radius=8
#         )

#         self.ball.vx = 4
#         self.ball.vy = -4

#         # Bricks
#         self.rows = 5
#         self.cols = 8

#         self.bricks = self._build_bricks(
#             self.rows,
#             self.cols
#         )

#         # Game information
#         self.lives = 3
#         self.score = 0

#         # Fonts
#         self.font = pygame.font.SysFont(
#             "Arial",
#             28
#         )

#         self.big_font = pygame.font.SysFont(
#             "Arial",
#             56,
#             bold=True
#         )

#         self.small_font = pygame.font.SysFont(
#             "Arial",
#             24
#         )

#         # Game state
#         self.game_over = False
#         self.result = None

#     def _build_bricks(self, rows, cols):

#         bricks = []

#         margin = 30
#         gap = 6
#         top = 60

#         brick_w = (
#             self.width
#             - margin * 2
#             - gap * (cols - 1)
#         ) // cols

#         brick_h = 22

#         for r in range(rows):

#             for c in range(cols):

#                 x = margin + c * (
#                     brick_w + gap
#                 )

#                 y = top + r * (
#                     brick_h + gap
#                 )

#                 bricks.append(
#                     Brick(
#                         x,
#                         y,
#                         brick_w,
#                         brick_h
#                     )
#                 )

#         return bricks

#     def handle_event(self, event):
#         pass

#     def handle_input(self):

#         # Stop paddle movement after game ends
#         if self.game_over:
#             return

#         keys = pygame.key.get_pressed()

#         if (
#             keys[pygame.K_LEFT]
#             or keys[pygame.K_a]
#         ):

#             self.paddle.move(
#                 -self.paddle.speed,
#                 self.width
#             )

#         if (
#             keys[pygame.K_RIGHT]
#             or keys[pygame.K_d]
#         ):

#             self.paddle.move(
#                 self.paddle.speed,
#                 self.width
#             )

#     # ---------------------------------------------------------
#     # Find which side of an object was hit
#     # ---------------------------------------------------------
#     def _collision_side(
#         self,
#         ball_rect,
#         object_rect
#     ):

#         dx_left = abs(
#             ball_rect.right
#             - object_rect.left
#         )

#         dx_right = abs(
#             object_rect.right
#             - ball_rect.left
#         )

#         dy_top = abs(
#             ball_rect.bottom
#             - object_rect.top
#         )

#         dy_bottom = abs(
#             object_rect.bottom
#             - ball_rect.top
#         )

#         horizontal = min(
#             dx_left,
#             dx_right
#         )

#         vertical = min(
#             dy_top,
#             dy_bottom
#         )

#         if horizontal < vertical:
#             return "horizontal"

#         return "vertical"

#     # ---------------------------------------------------------
#     # Update game
#     # ---------------------------------------------------------
#     def update(self):

#         if self.game_over:
#             return

#         # Move ball
#         self.ball.move()

#         ball_rect = self.ball.rect()

#         # -----------------------------------------------------
#         # Left and right walls
#         # -----------------------------------------------------
#         if (
#             self.ball.x - self.ball.radius <= 0
#             or
#             self.ball.x + self.ball.radius >= self.width
#         ):

#             self.ball.vx *= -1

#             self.ball.x = max(
#                 self.ball.radius,
#                 min(
#                     self.ball.x,
#                     self.width
#                     - self.ball.radius
#                 )
#             )

#         # -----------------------------------------------------
#         # Top wall
#         # -----------------------------------------------------
#         if (
#             self.ball.y
#             - self.ball.radius <= 0
#         ):

#             self.ball.vy *= -1

#             self.ball.y = self.ball.radius

#         # -----------------------------------------------------
#         # Paddle collision
#         # -----------------------------------------------------
#         paddle_rect = self.paddle.rect()

#         if ball_rect.colliderect(
#             paddle_rect
#         ):

#             side = self._collision_side(
#                 ball_rect,
#                 paddle_rect
#             )

#             if side == "horizontal":

#                 self.ball.vx *= -1

#             else:

#                 self.ball.vy *= -1

#                 # Make sure ball moves upward
#                 if self.ball.vy > 0:
#                     self.ball.vy *= -1

#             # Prevent repeated collision
#             self.ball.y = (
#                 self.paddle.y
#                 - self.ball.radius
#             )

#         # -----------------------------------------------------
#         # Brick collision
#         # -----------------------------------------------------
#         for brick in self.bricks:

#             if not brick.alive:
#                 continue

#             brick_rect = brick.rect()

#             if ball_rect.colliderect(
#                 brick_rect
#             ):

#                 side = self._collision_side(
#                     ball_rect,
#                     brick_rect
#                 )

#                 # Destroy brick
#                 brick.alive = False

#                 # Increase score
#                 self.score += 1

#                 # Correct bounce direction
#                 if side == "horizontal":

#                     self.ball.vx *= -1

#                 else:

#                     self.ball.vy *= -1

#                 break

#         # -----------------------------------------------------
#         # Ball falls below paddle
#         # -----------------------------------------------------
#         if (
#             self.ball.y
#             - self.ball.radius
#             > self.height
#         ):

#             self.lives -= 1

#             if self.lives <= 0:

#                 self.game_over = True
#                 self.result = "lose"

#             else:

#                 self._reset_ball()

#         # -----------------------------------------------------
#         # Win condition
#         # -----------------------------------------------------
#         if all(
#             not brick.alive
#             for brick in self.bricks
#         ):

#             self.game_over = True
#             self.result = "win"

#     # ---------------------------------------------------------
#     # Reset ball
#     # ---------------------------------------------------------
#     def _reset_ball(self):

#         self.ball.x = self.width // 2
#         self.ball.y = self.height - 50

#         self.ball.vx = 4
#         self.ball.vy = -4

#     # ---------------------------------------------------------
#     # Render game
#     # ---------------------------------------------------------
#     def render(self, screen):

#         screen.fill(BG)

#         # If game is over, show end screen
#         if self.game_over:

#             self._render_end_screen(screen)

#             return

#         # -----------------------------------------------------
#         # Paddle
#         # -----------------------------------------------------
#         pygame.draw.rect(
#             screen,
#             WHITE,
#             self.paddle.rect()
#         )

#         # -----------------------------------------------------
#         # Ball
#         # -----------------------------------------------------
#         pygame.draw.circle(
#             screen,
#             WHITE,
#             (
#                 int(self.ball.x),
#                 int(self.ball.y)
#             ),
#             self.ball.radius
#         )

#         # -----------------------------------------------------
#         # Bricks
#         # -----------------------------------------------------
#         for i, brick in enumerate(
#             self.bricks
#         ):

#             if brick.alive:

#                 row = i // self.cols

#                 color = BRICK_COLORS[
#                     row
#                     % len(BRICK_COLORS)
#                 ]

#                 pygame.draw.rect(
#                     screen,
#                     color,
#                     brick.rect()
#                 )

#         # -----------------------------------------------------
#         # Score
#         # -----------------------------------------------------
#         score_text = self.font.render(
#             f"Score: {self.score}",
#             True,
#             WHITE
#         )

#         screen.blit(
#             score_text,
#             (10, 10)
#         )

#         # -----------------------------------------------------
#         # Lives
#         # -----------------------------------------------------
#         lives_text = self.font.render(
#             f"Lives: {self.lives}",
#             True,
#             WHITE
#         )

#         screen.blit(
#             lives_text,
#             (
#                 self.width - 130,
#                 10
#             )
#         )

#     # ---------------------------------------------------------
#     # Game Over / Win Screen
#     # ---------------------------------------------------------
#     def _render_end_screen(
#         self,
#         screen
#     ):

#         screen.fill(BG)

#         # Decide message
#         if self.result == "win":

#             title = "YOU WIN!"
#             title_color = GREEN

#         else:

#             title = "GAME OVER"
#             title_color = RED

#         # Title
#         title_text = self.big_font.render(
#             title,
#             True,
#             title_color
#         )

#         title_rect = (
#             title_text.get_rect(
#                 center=(
#                     self.width // 2,
#                     180
#                 )
#             )
#         )

#         screen.blit(
#             title_text,
#             title_rect
#         )

#         # Final score
#         score_text = self.font.render(
#             f"Final Score: {self.score}",
#             True,
#             WHITE
#         )

#         score_rect = (
#             score_text.get_rect(
#                 center=(
#                     self.width // 2,
#                     270
#                 )
#             )
#         )

#         screen.blit(
#             score_text,
#             score_rect
#         )

#         # Instructions
#         instruction_text = (
#             "Press ENTER to continue"
#         )

#         instruction = self.small_font.render(
#             instruction_text,
#             True,
#             WHITE
#         )

#         instruction_rect = (
#             instruction.get_rect(
#                 center=(
#                     self.width // 2,
#                     350
#                 )
#             )
#         )

#         screen.blit(
#             instruction,
#             instruction_rect
#         )

#         # Exit instruction
#         exit_text = self.small_font.render(
#             "Press ESC to exit",
#             True,
#             WHITE
#         )

#         exit_rect = (
#             exit_text.get_rect(
#                 center=(
#                     self.width // 2,
#                     395
#                 )
#             )
#         )

#         screen.blit(
#             exit_text,
#             exit_rect
#         )


#task 3
# import pygame
# from .paddle import Paddle
# from .ball import Ball
# from .brick import Brick


# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (220, 60, 60)
# GREEN = (60, 220, 100)
# YELLOW = (240, 220, 70)
# BG = (15, 15, 25)

# BRICK_COLORS = [
#     (200, 60, 60),
#     (200, 140, 60),
#     (200, 200, 60),
#     (80, 180, 80),
#     (80, 140, 200),
# ]


# class GameEngine:

#     def __init__(self, width, height):

#         self.width = width
#         self.height = height

#         # Default difficulty
#         self.difficulty = "Medium"

#         # Game state
#         self.game_over = False
#         self.result = None
#         self.replay_menu = False

#         # Fonts
#         self.font = pygame.font.SysFont(
#             "Arial",
#             28
#         )

#         self.big_font = pygame.font.SysFont(
#             "Arial",
#             56,
#             bold=True
#         )

#         self.small_font = pygame.font.SysFont(
#             "Arial",
#             24
#         )

#         self.menu_font = pygame.font.SysFont(
#             "Arial",
#             32,
#             bold=True
#         )

#         # Create game
#         self._create_game()

#     # ---------------------------------------------------------
#     # Create / reset game
#     # ---------------------------------------------------------
#     def _create_game(self):

#         # Difficulty settings
#         if self.difficulty == "Easy":

#             self.ball_speed = 3
#             paddle_width = 120

#         elif self.difficulty == "Hard":

#             self.ball_speed = 6
#             paddle_width = 80

#         else:

#             self.ball_speed = 4
#             paddle_width = 100

#         # Paddle
#         self.paddle = Paddle(
#             self.width // 2 - paddle_width // 2,
#             self.height - 30,
#             paddle_width,
#             14
#         )

#         # Ball
#         self.ball = Ball(
#             self.width // 2,
#             self.height - 50,
#             radius=8
#         )

#         self.ball.vx = self.ball_speed
#         self.ball.vy = -self.ball_speed

#         # Bricks
#         self.rows = 5
#         self.cols = 8

#         self.bricks = self._build_bricks(
#             self.rows,
#             self.cols
#         )

#         # Game information
#         self.lives = 3
#         self.score = 0

#         self.game_over = False
#         self.result = None
#         self.replay_menu = False

#     # ---------------------------------------------------------
#     # Build bricks
#     # ---------------------------------------------------------
#     def _build_bricks(self, rows, cols):

#         bricks = []

#         margin = 30
#         gap = 6
#         top = 60

#         brick_w = (
#             self.width
#             - margin * 2
#             - gap * (cols - 1)
#         ) // cols

#         brick_h = 22

#         for r in range(rows):

#             for c in range(cols):

#                 x = margin + c * (
#                     brick_w + gap
#                 )

#                 y = top + r * (
#                     brick_h + gap
#                 )

#                 bricks.append(
#                     Brick(
#                         x,
#                         y,
#                         brick_w,
#                         brick_h
#                     )
#                 )

#         return bricks

#     # ---------------------------------------------------------
#     # Event handling
#     # ---------------------------------------------------------
#     def handle_event(self, event):

#         # Ignore events during normal game
#         if not self.game_over:
#             return

#         if event.type != pygame.KEYDOWN:
#             return

#         # -----------------------------------------------------
#         # End screen
#         # -----------------------------------------------------
#         if not self.replay_menu:

#             # ENTER opens replay menu
#             if event.key == pygame.K_RETURN:

#                 self.replay_menu = True

#             return

#         # -----------------------------------------------------
#         # Replay menu
#         # -----------------------------------------------------

#         # Easy
#         if event.key == pygame.K_1:

#             self.difficulty = "Easy"
#             self._create_game()

#         # Medium
#         elif event.key == pygame.K_2:

#             self.difficulty = "Medium"
#             self._create_game()

#         # Hard
#         elif event.key == pygame.K_3:

#             self.difficulty = "Hard"
#             self._create_game()

#         # Exit
#         elif event.key == pygame.K_4:

#             pygame.event.post(
#                 pygame.event.Event(
#                     pygame.QUIT
#                 )
#             )

#         # ESC also exits
#         elif event.key == pygame.K_ESCAPE:

#             pygame.event.post(
#                 pygame.event.Event(
#                     pygame.QUIT
#                 )
#             )

#     # ---------------------------------------------------------
#     # Keyboard input
#     # ---------------------------------------------------------
#     def handle_input(self):

#         if self.game_over:
#             return

#         keys = pygame.key.get_pressed()

#         # Move left
#         if (
#             keys[pygame.K_LEFT]
#             or keys[pygame.K_a]
#         ):

#             self.paddle.move(
#                 -self.paddle.speed,
#                 self.width
#             )

#         # Move right
#         if (
#             keys[pygame.K_RIGHT]
#             or keys[pygame.K_d]
#         ):

#             self.paddle.move(
#                 self.paddle.speed,
#                 self.width
#             )

#     # ---------------------------------------------------------
#     # Collision side detection
#     # ---------------------------------------------------------
#     def _collision_side(
#         self,
#         ball_rect,
#         object_rect
#     ):

#         dx_left = abs(
#             ball_rect.right
#             - object_rect.left
#         )

#         dx_right = abs(
#             object_rect.right
#             - ball_rect.left
#         )

#         dy_top = abs(
#             ball_rect.bottom
#             - object_rect.top
#         )

#         dy_bottom = abs(
#             object_rect.bottom
#             - ball_rect.top
#         )

#         horizontal = min(
#             dx_left,
#             dx_right
#         )

#         vertical = min(
#             dy_top,
#             dy_bottom
#         )

#         if horizontal < vertical:
#             return "horizontal"

#         return "vertical"

#     # ---------------------------------------------------------
#     # Update game
#     # ---------------------------------------------------------
#     def update(self):

#         if self.game_over:
#             return

#         # Move ball
#         self.ball.move()

#         ball_rect = self.ball.rect()

#         # -----------------------------------------------------
#         # Left / right walls
#         # -----------------------------------------------------
#         if (
#             self.ball.x - self.ball.radius <= 0
#             or
#             self.ball.x + self.ball.radius >= self.width
#         ):

#             self.ball.vx *= -1

#             self.ball.x = max(
#                 self.ball.radius,
#                 min(
#                     self.ball.x,
#                     self.width - self.ball.radius
#                 )
#             )

#         # -----------------------------------------------------
#         # Top wall
#         # -----------------------------------------------------
#         if self.ball.y - self.ball.radius <= 0:

#             self.ball.vy *= -1

#             self.ball.y = self.ball.radius

#         # -----------------------------------------------------
#         # Paddle collision
#         # -----------------------------------------------------
#         paddle_rect = self.paddle.rect()

#         if ball_rect.colliderect(
#             paddle_rect
#         ):

#             side = self._collision_side(
#                 ball_rect,
#                 paddle_rect
#             )

#             if side == "horizontal":

#                 self.ball.vx *= -1

#             else:

#                 self.ball.vy *= -1

#                 if self.ball.vy > 0:
#                     self.ball.vy *= -1

#             self.ball.y = (
#                 self.paddle.y
#                 - self.ball.radius
#             )

#         # -----------------------------------------------------
#         # Brick collision
#         # -----------------------------------------------------
#         for brick in self.bricks:

#             if not brick.alive:
#                 continue

#             brick_rect = brick.rect()

#             if ball_rect.colliderect(
#                 brick_rect
#             ):

#                 side = self._collision_side(
#                     ball_rect,
#                     brick_rect
#                 )

#                 # Destroy brick
#                 brick.alive = False

#                 # Score
#                 self.score += 1

#                 # Bounce
#                 if side == "horizontal":

#                     self.ball.vx *= -1

#                 else:

#                     self.ball.vy *= -1

#                 break

#         # -----------------------------------------------------
#         # Ball lost
#         # -----------------------------------------------------
#         if (
#             self.ball.y
#             - self.ball.radius
#             > self.height
#         ):

#             self.lives -= 1

#             if self.lives <= 0:

#                 self.game_over = True
#                 self.result = "lose"

#             else:

#                 self._reset_ball()

#         # -----------------------------------------------------
#         # Win
#         # -----------------------------------------------------
#         if all(
#             not brick.alive
#             for brick in self.bricks
#         ):

#             self.game_over = True
#             self.result = "win"

#     # ---------------------------------------------------------
#     # Reset ball after losing a life
#     # ---------------------------------------------------------
#     def _reset_ball(self):

#         self.ball.x = self.width // 2
#         self.ball.y = self.height - 50

#         self.ball.vx = self.ball_speed
#         self.ball.vy = -self.ball_speed

#     # ---------------------------------------------------------
#     # Render
#     # ---------------------------------------------------------
#     def render(self, screen):

#         screen.fill(BG)

#         # Game over screen
#         if self.game_over:

#             if self.replay_menu:

#                 self._render_replay_menu(screen)

#             else:

#                 self._render_end_screen(screen)

#             return

#         # -----------------------------------------------------
#         # Paddle
#         # -----------------------------------------------------
#         pygame.draw.rect(
#             screen,
#             WHITE,
#             self.paddle.rect()
#         )

#         # -----------------------------------------------------
#         # Ball
#         # -----------------------------------------------------
#         pygame.draw.circle(
#             screen,
#             WHITE,
#             (
#                 int(self.ball.x),
#                 int(self.ball.y)
#             ),
#             self.ball.radius
#         )

#         # -----------------------------------------------------
#         # Bricks
#         # -----------------------------------------------------
#         for i, brick in enumerate(
#             self.bricks
#         ):

#             if brick.alive:

#                 row = i // self.cols

#                 color = BRICK_COLORS[
#                     row
#                     % len(BRICK_COLORS)
#                 ]

#                 pygame.draw.rect(
#                     screen,
#                     color,
#                     brick.rect()
#                 )

#         # -----------------------------------------------------
#         # Score
#         # -----------------------------------------------------
#         score_text = self.font.render(
#             f"Score: {self.score}",
#             True,
#             WHITE
#         )

#         screen.blit(
#             score_text,
#             (10, 10)
#         )

#         # -----------------------------------------------------
#         # Lives
#         # -----------------------------------------------------
#         lives_text = self.font.render(
#             f"Lives: {self.lives}",
#             True,
#             WHITE
#         )

#         screen.blit(
#             lives_text,
#             (
#                 self.width - 130,
#                 10
#             )
#         )

#         # -----------------------------------------------------
#         # Difficulty
#         # -----------------------------------------------------
#         difficulty_text = self.small_font.render(
#             f"Difficulty: {self.difficulty}",
#             True,
#             WHITE
#         )

#         screen.blit(
#             difficulty_text,
#             (10, 40)
#         )

#     # ---------------------------------------------------------
#     # End screen
#     # ---------------------------------------------------------
#     def _render_end_screen(
#         self,
#         screen
#     ):

#         screen.fill(BG)

#         if self.result == "win":

#             title = "YOU WIN!"
#             title_color = GREEN

#         else:

#             title = "GAME OVER"
#             title_color = RED

#         # Title
#         title_text = self.big_font.render(
#             title,
#             True,
#             title_color
#         )

#         title_rect = title_text.get_rect(
#             center=(
#                 self.width // 2,
#                 170
#             )
#         )

#         screen.blit(
#             title_text,
#             title_rect
#         )

#         # Final score
#         score_text = self.font.render(
#             f"Final Score: {self.score}",
#             True,
#             WHITE
#         )

#         score_rect = score_text.get_rect(
#             center=(
#                 self.width // 2,
#                 260
#             )
#         )

#         screen.blit(
#             score_text,
#             score_rect
#         )

#         # Current difficulty
#         difficulty_text = self.small_font.render(
#             f"Difficulty: {self.difficulty}",
#             True,
#             WHITE
#         )

#         difficulty_rect = (
#             difficulty_text.get_rect(
#                 center=(
#                     self.width // 2,
#                     305
#                 )
#             )
#         )

#         screen.blit(
#             difficulty_text,
#             difficulty_rect
#         )

#         # Continue
#         continue_text = self.small_font.render(
#             "Press ENTER to continue",
#             True,
#             YELLOW
#         )

#         continue_rect = (
#             continue_text.get_rect(
#                 center=(
#                     self.width // 2,
#                     370
#                 )
#             )
#         )

#         screen.blit(
#             continue_text,
#             continue_rect
#         )

#         # Exit
#         exit_text = self.small_font.render(
#             "Press ESC to exit",
#             True,
#             WHITE
#         )

#         exit_rect = exit_text.get_rect(
#             center=(
#                 self.width // 2,
#                 415
#             )
#         )

#         screen.blit(
#             exit_text,
#             exit_rect
#         )

#     # ---------------------------------------------------------
#     # Replay menu
#     # ---------------------------------------------------------
#     def _render_replay_menu(
#         self,
#         screen
#     ):

#         screen.fill(BG)

#         # Title
#         title = self.big_font.render(
#             "PLAY AGAIN?",
#             True,
#             WHITE
#         )

#         title_rect = title.get_rect(
#             center=(
#                 self.width // 2,
#                 100
#             )
#         )

#         screen.blit(
#             title,
#             title_rect
#         )

#         # Easy
#         easy = self.menu_font.render(
#             "1 - EASY",
#             True,
#             GREEN
#         )

#         easy_rect = easy.get_rect(
#             center=(
#                 self.width // 2,
#                 200
#             )
#         )

#         screen.blit(
#             easy,
#             easy_rect
#         )

#         # Medium
#         medium = self.menu_font.render(
#             "2 - MEDIUM",
#             True,
#             YELLOW
#         )

#         medium_rect = medium.get_rect(
#             center=(
#                 self.width // 2,
#                 260
#             )
#         )

#         screen.blit(
#             medium,
#             medium_rect
#         )

#         # Hard
#         hard = self.menu_font.render(
#             "3 - HARD",
#             True,
#             RED
#         )

#         hard_rect = hard.get_rect(
#             center=(
#                 self.width // 2,
#                 320
#             )
#         )

#         screen.blit(
#             hard,
#             hard_rect
#         )

#         # Exit
#         exit_option = self.menu_font.render(
#             "4 - EXIT",
#             True,
#             WHITE
#         )

#         exit_rect = exit_option.get_rect(
#             center=(
#                 self.width // 2,
#                 380
#             )
#         )
#         screen.blit(
#             exit_option,
#             exit_rect
#         )

#         # Instruction
#         instruction = self.small_font.render(
#             "Choose a difficulty",
#             True,
#             WHITE
#         )

#         instruction_rect = (
#             instruction.get_rect(
#                 center=(
#                     self.width // 2,
#                     460
#                 )
#             )
#         )

#         screen.blit(
#             instruction,
#             instruction_rect
#         )

#task 4
import pygame
import math
from array import array

from .paddle import Paddle
from .ball import Ball
from .brick import Brick


# ---------------------------------------------------------
# Colors
# ---------------------------------------------------------
WHITE = (255, 255, 255)
RED = (220, 60, 60)
GREEN = (60, 220, 100)
YELLOW = (240, 220, 70)
BG = (15, 15, 25)

BRICK_COLORS = [
    (200, 60, 60),
    (200, 140, 60),
    (200, 200, 60),
    (80, 180, 80),
    (80, 140, 200),
]


class GameEngine:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        # -------------------------------------------------
        # Difficulty
        # -------------------------------------------------
        self.difficulty = "Medium"

        # -------------------------------------------------
        # Game state
        # -------------------------------------------------
        self.game_over = False
        self.result = None
        self.replay_menu = False

        # -------------------------------------------------
        # Fonts
        # -------------------------------------------------
        self.font = pygame.font.SysFont(
            "Arial",
            28
        )

        self.big_font = pygame.font.SysFont(
            "Arial",
            56,
            bold=True
        )

        self.small_font = pygame.font.SysFont(
            "Arial",
            24
        )

        self.menu_font = pygame.font.SysFont(
            "Arial",
            32,
            bold=True
        )

        # -------------------------------------------------
        # Sound initialization
        # -------------------------------------------------
        self.sound_enabled = False

        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()

            self.sound_enabled = True

            self.wall_sound = self._create_sound(
                350,
                0.08
            )

            self.paddle_sound = self._create_sound(
                500,
                0.10
            )

            self.brick_sound = self._create_sound(
                700,
                0.12
            )

            self.win_sound = self._create_sound(
                900,
                0.30
            )

            self.game_over_sound = self._create_sound(
                180,
                0.35
            )

        except pygame.error:

            self.sound_enabled = False

        # -------------------------------------------------
        # Create game
        # -------------------------------------------------
        self._create_game()

    # ---------------------------------------------------------
    # Create a simple sound
    # ---------------------------------------------------------
    def _create_sound(
        self,
        frequency,
        duration
    ):

        sample_rate = 44100

        number_of_samples = int(
            sample_rate * duration
        )

        amplitude = 10000

        samples = array("h")

        for i in range(number_of_samples):

            value = int(
                amplitude
                * math.sin(
                    2
                    * math.pi
                    * frequency
                    * i
                    / sample_rate
                )
            )

            samples.append(value)

        return pygame.mixer.Sound(
            buffer=samples.tobytes()
        )

    # ---------------------------------------------------------
    # Play sound safely
    # ---------------------------------------------------------
    def _play_sound(self, sound):

        if self.sound_enabled:

            try:
                sound.play()

            except pygame.error:
                pass

    # ---------------------------------------------------------
    # Create / reset game
    # ---------------------------------------------------------
    def _create_game(self):

        # Difficulty settings
        if self.difficulty == "Easy":

            self.ball_speed = 3
            paddle_width = 120

        elif self.difficulty == "Hard":

            self.ball_speed = 6
            paddle_width = 80

        else:

            self.ball_speed = 4
            paddle_width = 100

        # Paddle
        self.paddle = Paddle(
            self.width // 2 - paddle_width // 2,
            self.height - 30,
            paddle_width,
            14
        )

        # Ball
        self.ball = Ball(
            self.width // 2,
            self.height - 50,
            radius=8
        )

        self.ball.vx = self.ball_speed
        self.ball.vy = -self.ball_speed

        # Bricks
        self.rows = 5
        self.cols = 8

        self.bricks = self._build_bricks(
            self.rows,
            self.cols
        )

        # Game information
        self.lives = 3
        self.score = 0

        self.game_over = False
        self.result = None
        self.replay_menu = False

    # ---------------------------------------------------------
    # Build bricks
    # ---------------------------------------------------------
    def _build_bricks(self, rows, cols):

        bricks = []

        margin = 30
        gap = 6
        top = 60

        brick_w = (
            self.width
            - margin * 2
            - gap * (cols - 1)
        ) // cols

        brick_h = 22

        for r in range(rows):

            for c in range(cols):

                x = margin + c * (
                    brick_w + gap
                )

                y = top + r * (
                    brick_h + gap
                )

                bricks.append(
                    Brick(
                        x,
                        y,
                        brick_w,
                        brick_h
                    )
                )

        return bricks

    # ---------------------------------------------------------
    # Event handling
    # ---------------------------------------------------------
    def handle_event(self, event):

        if not self.game_over:
            return

        if event.type != pygame.KEYDOWN:
            return

        # End screen
        if not self.replay_menu:

            if event.key == pygame.K_RETURN:

                self.replay_menu = True

            elif event.key == pygame.K_ESCAPE:

                pygame.event.post(
                    pygame.event.Event(
                        pygame.QUIT
                    )
                )

            return

        # Replay menu

        # Easy
        if event.key == pygame.K_1:

            self.difficulty = "Easy"
            self._create_game()

        # Medium
        elif event.key == pygame.K_2:

            self.difficulty = "Medium"
            self._create_game()

        # Hard
        elif event.key == pygame.K_3:

            self.difficulty = "Hard"
            self._create_game()

        # Exit
        elif event.key == pygame.K_4:

            pygame.event.post(
                pygame.event.Event(
                    pygame.QUIT
                )
            )

        elif event.key == pygame.K_ESCAPE:

            pygame.event.post(
                pygame.event.Event(
                    pygame.QUIT
                )
            )

    # ---------------------------------------------------------
    # Keyboard input
    # ---------------------------------------------------------
    def handle_input(self):

        if self.game_over:
            return

        keys = pygame.key.get_pressed()

        if (
            keys[pygame.K_LEFT]
            or keys[pygame.K_a]
        ):

            self.paddle.move(
                -self.paddle.speed,
                self.width
            )

        if (
            keys[pygame.K_RIGHT]
            or keys[pygame.K_d]
        ):

            self.paddle.move(
                self.paddle.speed,
                self.width
            )

    # ---------------------------------------------------------
    # Collision side detection
    # ---------------------------------------------------------
    def _collision_side(
        self,
        ball_rect,
        object_rect
    ):

        dx_left = abs(
            ball_rect.right
            - object_rect.left
        )

        dx_right = abs(
            object_rect.right
            - ball_rect.left
        )

        dy_top = abs(
            ball_rect.bottom
            - object_rect.top
        )

        dy_bottom = abs(
            object_rect.bottom
            - ball_rect.top
        )

        horizontal = min(
            dx_left,
            dx_right
        )

        vertical = min(
            dy_top,
            dy_bottom
        )

        if horizontal < vertical:
            return "horizontal"

        return "vertical"

    # ---------------------------------------------------------
    # Update game
    # ---------------------------------------------------------
    def update(self):

        if self.game_over:
            return

        # Move ball
        self.ball.move()

        ball_rect = self.ball.rect()

        # -----------------------------------------------------
        # Left / right walls
        # -----------------------------------------------------
        if (
            self.ball.x - self.ball.radius <= 0
            or
            self.ball.x + self.ball.radius >= self.width
        ):

            self.ball.vx *= -1

            self.ball.x = max(
                self.ball.radius,
                min(
                    self.ball.x,
                    self.width - self.ball.radius
                )
            )

            # Wall sound
            self._play_sound(
                self.wall_sound
            )

        # -----------------------------------------------------
        # Top wall
        # -----------------------------------------------------
        if self.ball.y - self.ball.radius <= 0:

            self.ball.vy *= -1

            self.ball.y = self.ball.radius

            # Wall sound
            self._play_sound(
                self.wall_sound
            )

        # -----------------------------------------------------
        # Paddle collision
        # -----------------------------------------------------
        paddle_rect = self.paddle.rect()

        if ball_rect.colliderect(
            paddle_rect
        ):

            side = self._collision_side(
                ball_rect,
                paddle_rect
            )

            if side == "horizontal":

                self.ball.vx *= -1

            else:

                self.ball.vy *= -1

                if self.ball.vy > 0:
                    self.ball.vy *= -1

            self.ball.y = (
                self.paddle.y
                - self.ball.radius
            )

            # Paddle sound
            self._play_sound(
                self.paddle_sound
            )

        # -----------------------------------------------------
        # Brick collision
        # -----------------------------------------------------
        for brick in self.bricks:

            if not brick.alive:
                continue

            brick_rect = brick.rect()

            if ball_rect.colliderect(
                brick_rect
            ):

                side = self._collision_side(
                    ball_rect,
                    brick_rect
                )

                # Destroy brick
                brick.alive = False

                # Increase score
                self.score += 1

                # Correct bounce
                if side == "horizontal":

                    self.ball.vx *= -1

                else:

                    self.ball.vy *= -1

                # Brick sound
                self._play_sound(
                    self.brick_sound
                )

                break

        # -----------------------------------------------------
        # Ball lost
        # -----------------------------------------------------
        if (
            self.ball.y
            - self.ball.radius
            > self.height
        ):

            self.lives -= 1

            if self.lives <= 0:

                self.game_over = True
                self.result = "lose"

                # Game over sound
                self._play_sound(
                    self.game_over_sound
                )

            else:

                self._reset_ball()

        # -----------------------------------------------------
        # Win condition
        # -----------------------------------------------------
        if all(
            not brick.alive
            for brick in self.bricks
        ):

            self.game_over = True
            self.result = "win"

            # Win sound
            self._play_sound(
                self.win_sound
            )

    # ---------------------------------------------------------
    # Reset ball
    # ---------------------------------------------------------
    def _reset_ball(self):

        self.ball.x = self.width // 2
        self.ball.y = self.height - 50

        self.ball.vx = self.ball_speed
        self.ball.vy = -self.ball_speed

    # ---------------------------------------------------------
    # Render
    # ---------------------------------------------------------
    def render(self, screen):

        screen.fill(BG)

        # End screen
        if self.game_over:

            if self.replay_menu:

                self._render_replay_menu(screen)

            else:

                self._render_end_screen(screen)

            return

        # Paddle
        pygame.draw.rect(
            screen,
            WHITE,
            self.paddle.rect()
        )

        # Ball
        pygame.draw.circle(
            screen,
            WHITE,
            (
                int(self.ball.x),
                int(self.ball.y)
            ),
            self.ball.radius
        )

        # Bricks
        for i, brick in enumerate(
            self.bricks
        ):

            if brick.alive:

                row = i // self.cols

                color = BRICK_COLORS[
                    row
                    % len(BRICK_COLORS)
                ]

                pygame.draw.rect(
                    screen,
                    color,
                    brick.rect()
                )

        # Score
        score_text = self.font.render(
            f"Score: {self.score}",
            True,
            WHITE
        )

        screen.blit(
            score_text,
            (10, 10)
        )

        # Lives
        lives_text = self.font.render(
            f"Lives: {self.lives}",
            True,
            WHITE
        )

        screen.blit(
            lives_text,
            (
                self.width - 130,
                10
            )
        )

        # Difficulty
        difficulty_text = self.small_font.render(
            f"Difficulty: {self.difficulty}",
            True,
            WHITE
        )

        screen.blit(
            difficulty_text,
            (10, 40)
        )

    # ---------------------------------------------------------
    # End screen
    # ---------------------------------------------------------
    def _render_end_screen(
        self,
        screen
    ):

        screen.fill(BG)

        if self.result == "win":

            title = "YOU WIN!"
            title_color = GREEN

        else:

            title = "GAME OVER"
            title_color = RED

        # Title
        title_text = self.big_font.render(
            title,
            True,
            title_color
        )

        title_rect = title_text.get_rect(
            center=(
                self.width // 2,
                170
            )
        )

        screen.blit(
            title_text,
            title_rect
        )

        # Final score
        score_text = self.font.render(
            f"Final Score: {self.score}",
            True,
            WHITE
        )

        score_rect = score_text.get_rect(
            center=(
                self.width // 2,
                260
            )
        )

        screen.blit(
            score_text,
            score_rect
        )

        # Difficulty
        difficulty_text = self.small_font.render(
            f"Difficulty: {self.difficulty}",
            True,
            WHITE
        )

        difficulty_rect = (
            difficulty_text.get_rect(
                center=(
                    self.width // 2,
                    305
                )
            )
        )

        screen.blit(
            difficulty_text,
            difficulty_rect
        )

        # Continue
        continue_text = self.small_font.render(
            "Press ENTER to continue",
            True,
            YELLOW
        )

        continue_rect = (
            continue_text.get_rect(
                center=(
                    self.width // 2,
                    370
                )
            )
        )

        screen.blit(
            continue_text,
            continue_rect
        )

        # Exit
        exit_text = self.small_font.render(
            "Press ESC to exit",
            True,
            WHITE
        )

        exit_rect = (
            exit_text.get_rect(
                center=(
                    self.width // 2,
                    415
                )
            )
        )

        screen.blit(
            exit_text,
            exit_rect
        )

    # ---------------------------------------------------------
    # Replay menu
    # ---------------------------------------------------------
    def _render_replay_menu(
        self,
        screen
    ):

        screen.fill(BG)

        # Title
        title = self.big_font.render(
            "PLAY AGAIN?",
            True,
            WHITE
        )

        title_rect = title.get_rect(
            center=(
                self.width // 2,
                100
            )
        )

        screen.blit(
            title,
            title_rect
        )

        # Easy
        easy = self.menu_font.render(
            "1 - EASY",
            True,
            GREEN
        )

        easy_rect = easy.get_rect(
            center=(
                self.width // 2,
                200
            )
        )

        screen.blit(
            easy,
            easy_rect
        )

        # Medium
        medium = self.menu_font.render(
            "2 - MEDIUM",
            True,
            YELLOW
        )

        medium_rect = medium.get_rect(
            center=(
                self.width // 2,
                260
            )
        )

        screen.blit(
            medium,
            medium_rect
        )

        # Hard
        hard = self.menu_font.render(
            "3 - HARD",
            True,
            RED
        )

        hard_rect = hard.get_rect(
            center=(
                self.width // 2,
                320
            )
        )

        screen.blit(
            hard,
            hard_rect
        )

        # Exit
        exit_option = self.menu_font.render(
            "4 - EXIT",
            True,
            WHITE
        )

        exit_rect = exit_option.get_rect(
            center=(
                self.width // 2,
                380
            )
        )

        screen.blit(
            exit_option,
            exit_rect
        )

        # Instruction
        instruction = self.small_font.render(
            "Choose a difficulty",
            True,
            WHITE
        )

        instruction_rect = (
            instruction.get_rect(
                center=(
                    self.width // 2,
                    460
                )
            )
        )

        screen.blit(
            instruction,
            instruction_rect
        )