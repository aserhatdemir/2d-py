import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock-Paper-Scissors Simulation")

# Load images
ROCK_IMAGE = pygame.image.load("assets/rock.png")
PAPER_IMAGE = pygame.image.load("assets/paper.png")
SCISSORS_IMAGE = pygame.image.load("assets/scissors.png")

# Scale images
OBJECT_SIZE = (40, 40)
ROCK_IMAGE = pygame.transform.scale(ROCK_IMAGE, OBJECT_SIZE)
PAPER_IMAGE = pygame.transform.scale(PAPER_IMAGE, OBJECT_SIZE)
SCISSORS_IMAGE = pygame.transform.scale(SCISSORS_IMAGE, OBJECT_SIZE)

# Define object types
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

# Game object class
class GameObject:
    def __init__(self, obj_type):
        self.type = obj_type
        if obj_type == ROCK:
            self.image = ROCK_IMAGE
        elif obj_type == PAPER:
            self.image = PAPER_IMAGE
        elif obj_type == SCISSORS:
            self.image = SCISSORS_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - OBJECT_SIZE[0])
        self.rect.y = random.randint(0, HEIGHT - OBJECT_SIZE[1])
        self.speed = [random.choice([-2, -1, 1, 2]), random.choice([-2, -1, 1, 2])]

    def move(self):
        # Move the object
        self.rect = self.rect.move(self.speed)
        # Bounce off the walls
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed[1] = -self.speed[1]

# Collision detection and resolution
def handle_collisions(objects):
    for obj1 in objects:
        for obj2 in objects:
            if obj1 != obj2 and obj1.rect.colliderect(obj2.rect):
                # Apply Rock-Paper-Scissors rules
                if obj1.type != obj2.type:
                    if (obj1.type == ROCK and obj2.type == SCISSORS) or \
                       (obj1.type == PAPER and obj2.type == ROCK) or \
                       (obj1.type == SCISSORS and obj2.type == PAPER):
                        if obj2 in objects:
                            objects.remove(obj2)
                    else:
                        if obj1 in objects:
                            objects.remove(obj1)

# Main game loop
def main():
    clock = pygame.time.Clock()

    # Create initial objects
    objects = []
    for _ in range(5):
        objects.append(GameObject(ROCK))
        objects.append(GameObject(PAPER))
        objects.append(GameObject(SCISSORS))

    running = True
    while running:
        clock.tick(60)  # Limit to 60 frames per second
        WINDOW.fill((255, 255, 255))  # Clear the screen with a white background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move and draw all game objects
        for obj in objects:
            obj.move()
            WINDOW.blit(obj.image, obj.rect)

        # Handle collisions
        handle_collisions(objects)

        # Update the display
        pygame.display.flip()

        # Check for a win condition
        types_remaining = set(obj.type for obj in objects)
        if len(types_remaining) == 1:
            print(f"Game Over! {types_remaining.pop().capitalize()} wins!")
            pygame.time.delay(2000)
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
