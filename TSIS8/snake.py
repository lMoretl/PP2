import pygame, sys, random, time, os
pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((500,400))
clock = pygame.time.Clock()
font = pygame.font.Font(None,72)
font1 = pygame.font.Font(None,32)
text1 = font1.render("Score", True, (0,0,255))
text2 = font1.render("Level", True, (0,0,255))
score = 0
level = 1
head1 = 0
head2 = 0
chfps = 5
FPS = 4
Over = False
Victory = False
class Snake:
    def __init__(self, x, y):
        self.body = [[x,y], [x+1,y],[x+2,y]]
        self.dx = -1
        self.dy = 0
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.body[1][1] != self.body[0][1] - 1:
                    self.dy = -1
                    self.dx = 0
                if event.key == pygame.K_DOWN and self.body[1][1] != self.body[0][1] + 1:
                    self.dy = 1
                    self.dx = 0
                if event.key == pygame.K_RIGHT and self.body[1][0] != self.body[0][0] + 1:
                    self.dx = 1
                    self.dy = 0
                if event.key == pygame.K_LEFT and self.body[1][0] != self.body[0][0] - 1:
                    self.dx = -1
                    self.dy = 0
        for i in range (len(self.body)-1,0,-1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy
        if self.body[0][0] == -1:
            self.body[0][0] = 19
        if self.body[0][0] == 20:
            self.body[0][0] = 0
        if self.body[0][1] == -1:
            self.body[0][1] = 19
        if self.body[0][1] == 20:
            self.body[0][1] = 0
    def draw(self,screen):
        i, u = self.body[0]
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(i * 20, u * 20, 20, 20))
        for q in self.body[1:]:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(q[0] * 20, q[1] * 20, 20, 20))
    def new(self, x, y):
        self.body = [[x,y], [x+1,y], [x+2,y]]
        self.dx = -1
        self.dy = 0
class Food:
    def __init__(self, S, W):
        self.x = random.randint(0,19)
        self.y = random.randint(0,19)
        q = [self.x, self.y]
        while q in S.body or q in W.body:
            self.x = random.randint(0,19)
            self.y = random.randint(0,19)
            q = [self.x, self.y]
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x*20,self.y*20,20,20))
    def new(self, S, W):
        self.x = random.randint(0,19)
        self.y = random.randint(0,19)
        q = [self.x, self.y]
        while q in S.body or q in W.body:
            self.x = random.randint(0,19)
            self.y = random.randint(0,19)
            q = [self.x, self.y]
class Wall:
    def __init__(self, level):
        self.body = []
        text = r"levels\{}.txt".format(level)
        if os.path.exists(text):
            f = open(text, "r")
            i = 0
            u = 0
            line = f.readline()
            while line != None and i < 20:
                for x in line:
                    if x == "#":
                        self.body.append([u,i])
                    elif x == "$":
                        global head1, head2
                        head1 = u
                        head2 = i
                    u += 1
                    if u == 20:
                        break
                i += 1
                u = 0
                line = f.readline()
        else:
            global Victory
            Victory = True
    def draw(self, screen):
        for x in range(len(self.body)):
            pygame.draw.rect(screen, (165,42,42), pygame.Rect(self.body[x][0]*20,self.body[x][1]*20,20,20))
    def new(self, level):
        self.body = []
        text = r"levels\{}.txt".format(level)
        if os.path.exists(text):
            f = open(text, "r")
            i = 0
            u = 0
            line = f.readline()
            while line != None and i < 20:
                for x in line:
                    if x == "#":
                        self.body.append([u,i])
                    elif x == "$":
                        global head1, head2
                        head1 = u
                        head2 = i
                    u += 1
                    if u == 20:
                        break
                i += 1
                u = 0
                line = f.readline()
        else:
            global Victory
            Victory = True
def Grid(screen):
    for x in range(0, 400, 20):
        for y in range(0, 400, 20):
            pygame.draw.rect(screen, (60, 60, 60), pygame.Rect(x, y, 20, 20), 1)
W = Wall(level)
S = Snake(head1, head2)
F = Food(S, W)
while True:
    screen.fill((0,0,0))
    Grid(screen)
    S.move()
    S.draw(screen)
    if S.body[0][0] == F.x and S.body[0][1] == F.y:
        score += 1
        F.new(S, W)
        S.body.append([F.x,F.y])
    for i in range(1,len(S.body)):
        if S.body[0][0] == S.body[i][0] and S.body[0][1] == S.body[i][1]:
            Over = True
    for i in range(len(W.body)):
        if S.body[0][0] == W.body[i][0] and S.body[0][1] == W.body[i][1]:
            Over = True
    if Over: 
        lose = font.render("Game Over", True, (255,0,0))
        screen.fill((0,0,0))
        screen.blit(lose,(250-lose.get_width()//2,200-lose.get_height()//2))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
    F.draw(screen)
    W.draw(screen)
    if score == chfps:
        FPS += 2
        chfps += 5
    Score = font.render(str(score), True, (0,0,255))
    Level = font.render(str(level), True, (0,0,255))
    screen.blit(Score,(450-Score.get_width()//2,130-Score.get_height()//2))
    screen.blit(Level,(450-Level.get_width()//2,330-Level.get_height()//2))
    screen.blit(text1,(450-text1.get_width()//2,50-text1.get_height()//2))
    screen.blit(text2,(450-text2.get_width()//2,250-text2.get_height()//2))
    if score == 15:
        time.sleep(1)
        score = 0
        FPS = 4
        chfps = 5
        level += 1
        W.new(level)
        if Victory:
            win = font.render("You win!", True, (255,215,0))
            screen.fill((0,0,0))
            screen.blit(win,(250-win.get_width()//2,200-win.get_height()//2))
            pygame.display.flip()
            time.sleep(3)
            pygame.quit()
            sys.exit()
        S.new(head1,head2)
        F.new(S,W)
    pygame.display.update()
    clock.tick(FPS)