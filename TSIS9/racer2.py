import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode((700,800))
bg = pygame.image.load(r"images\road.png")
pygame.display.set_caption("Street Racer")
sound1 = pygame.mixer.Sound(r"sounds\normal.mp3")
sound2 = pygame.mixer.Sound(r"sounds\crash.mp3")
sound3 = pygame.mixer.Sound(r"sounds\collect.mp3")
sound4 = pygame.mixer.Sound(r"sounds\crystal.mp3")
font = pygame.font.Font(None,80)
over = font.render("Game Over", True, (255,0,0))
text = font.render("press R to restart", True, (255,0,0))
score = 0
money = 0
Mscore = 0
Mmoney = 0
FPS = 40
clock = pygame.time.Clock()
pygame.display.set_caption("Street Racer")
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"images\coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(18,682), random.randint(18,782))
    def draw(self,screen):
        screen.blit(self.image, self.rect)
    def default(self):
        global sound3
        sound3.play(0)
        self.rect.center = (random.randint(18,682), random.randint(18,782))
class Diamond(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"images\diamond.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(18,682), random.randint(18,782))
    def draw(self,screen):
        screen.blit(self.image, self.rect)
    def default(self):
        global sound4
        sound4.play(0)
        self.rect.center = (random.randint(18,682), random.randint(18,782))
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"images\redcar.png")
        self.rect = self.image.get_rect()
        self.rect.center = (350,500)
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5,0)
        if pressed[pygame.K_RIGHT] and self.rect.right < 700:
            self.rect.move_ip(5,0)
        if pressed[pygame.K_UP] and self.rect.top > 0:
            self.rect.move_ip(0,-5)
        if pressed[pygame.K_DOWN] and self.rect.bottom < 800:
            self.rect.move_ip(0, 5)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def default(self):
        self.rect.center = (350,500)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"images\bluecar.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(35,665),0)
    def move(self):
        global score
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 800:
            score += 1
            self.top = 0
            self.rect.center = (random.randint(35,665),0)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def default(self):
        self.rect.center = (random.randint(35,665),0)
P1 = Player()
E1 = Enemy()
C = Coin()
D = Diamond()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C)
jewels = pygame.sprite.Group()
jewels.add(D)
sound1.play(-1)
while True:
    screen.blit(bg,(0,0))
    P1.move()
    E1.move()
    P1.draw(screen)
    E1.draw(screen)
    C.draw(screen)
    D.draw(screen)
    Score = font.render(str(score), True, (255,255,255))
    Money = font.render(str(money), True, (255,255,0))
    if score > Mscore:
        Mscore = score
    if money > Mmoney:
        Mmoney = money
    MScore = font.render(str(Mscore), True, (255,255,255))
    MMoney = font.render(str(Mmoney), True, (255,255,0))
    screen.blit(Score,(50-Score.get_width()//2,40-Score.get_height()//2))
    screen.blit(Money,(650-Money.get_width()//2,40-Money.get_height()//2))
    screen.blit(MScore,(50-Score.get_width()//2,760-Score.get_height()//2))
    screen.blit(MMoney,(650-Money.get_width()//2,760-Money.get_height()//2))
    if pygame.sprite.spritecollideany(P1,enemies):
        sound1.stop()
        sound2.play(0)
        P1.default()
        E1.default()
        score = 0
        money = 0
        while not pygame.key.get_pressed()[pygame.K_r]:
            screen.fill((0,0,0))
            screen.blit(over,(350-over.get_width()//2,300-over.get_height()//2))
            screen.blit(text,(350-text.get_width()//2,500-text.get_height()//2))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        sound2.stop()
        sound1.play(-1)
    if pygame.sprite.spritecollideany(P1,coins):
        money += 1
        C.default()
    if pygame.sprite.spritecollideany(P1,jewels):
        money += 3
        D.default()
    FPS = 30 + 10 * (money//10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(FPS)