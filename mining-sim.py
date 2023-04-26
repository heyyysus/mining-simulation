import pygame
import random
import hashlib

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1200, 800))

# Title and Icon
pygame.display.set_caption("Mining Simulator")

class Block:
    def __init__(self, id, x, y , prev_hash, data, nonce, hash):
        self.id = id
        self.x = x
        self.y = y
        self.size = 200
        self.background_color = (0, 0, 255)
        self.color = (255, 255, 255)
        self.prev_hash = prev_hash
        self.data = data
        self.nonce = nonce
        self.hash = hash

    def Draw(self):
        pygame.draw.rect(screen, self.background_color, (self.x, self.y, self.size, self.size))
        pygame.draw.rect(screen, self.color, (self.x+5, self.y+5, self.size-10, self.size-10))

        # Draw id string
        font = pygame.font.Font('freesansbold.ttf', 14)
        text = font.render("ID: " + str(self.id), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.x + self.size/2, self.y + 20)
        screen.blit(text, textRect)

        # Draw prev_hash string
        font = pygame.font.Font('freesansbold.ttf', 14)
        text = font.render("Prev Hash: " + self.prev_hash[0:10], True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.x + self.size/2, self.y + 40)
        screen.blit(text, textRect)

        # Draw data string
        font = pygame.font.Font('freesansbold.ttf', 14)
        text = font.render(self.data, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.x + self.size/2, self.y + 60)
        screen.blit(text, textRect)

        # Draw nonce string
        font = pygame.font.Font('freesansbold.ttf', 14)
        text = font.render("Nonce: " + str(self.nonce), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.x + self.size/2, self.y + 80)
        screen.blit(text, textRect)

        # Draw hash string
        font = pygame.font.Font('freesansbold.ttf', 14)
        text = font.render("Hash: " + self.hash[0:10], True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.x + self.size/2, self.y + 100)
        screen.blit(text, textRect)




    def Update(self):
        pass

def GenerateRandomData():
    names = ["Alice", "Bob", "Charlie"]
    actions = ["sent", "received"]

    return random.choice(names) + " " + random.choice(actions) + " " + str(random.randint(0, 100)) + " BTC"

init_block = Block(0, 0, 0, "00aaa32122aa2", GenerateRandomData(), 0, "qef13r124")

blocks = [init_block]

def Update():
    # Mine the current block
    id = blocks[-1].id
    prev_hash = blocks[-1].prev_hash
    data = blocks[-1].data
    nonce = random.randint(0, 10000000000)
    
    hash_obj = hashlib.sha256()
    hash_obj.update((str(prev_hash) + data + str(nonce)).encode('utf-8'))
    hash = hash_obj.hexdigest()

    blocks[-1] = Block(id, blocks[-1].x, blocks[-1].y, prev_hash, data, nonce, hash)

    # Create a new block if the current block is mined
    if hash[0:2] == "00":

        blocks[-1].background_color = (0, 255, 0)

        new_id = blocks[-1].id + 1
        new_x = blocks[-1].x + blocks[-1].size
        new_y = blocks[-1].y

        # Move to new row if the current row is full
        if new_x + blocks[-1].size > screen.get_width():
            new_x = 0
            new_y += blocks[-1].size

        blocks.append(Block(new_id, new_x, new_y, hash, GenerateRandomData(), 0, hash))

def Draw():
    for b in blocks:
        b.Draw()



# Main loop
running = True
while running:
    
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Update()
    Draw()

    pygame.display.update()

    pygame.time.Clock().tick(60)