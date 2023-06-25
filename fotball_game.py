# Importujeme knihovnu pygame pro grafiku a zvuk
import pygame

# Inicializujeme pygame a vytvoříme okno
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fotbalová hra")

# Nastavíme barvy a fonty
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
FONT = pygame.font.SysFont("Arial", 32)

# Vytvoříme třídu pro fotbalovou branku se sítí a reálných rozměrech
class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Zavoláme konstruktor rodičovské třídy
        super().__init__()

        # Nastavíme obrázek a obdélník branky
        self.image = pygame.image.load("goal.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Zde můžeme přidat nějakou logiku pro branku
        pass

# Vytvoříme třídu pro brankáře
class Goalkeeper(pygame.sprite.Sprite):
    def __init__(self, x, y, team):
        # Zavoláme konstruktor rodičovské třídy
        super().__init__()

        # Nastavíme obrázek a obdélník brankáře podle týmu
        if team == "Slavia":
            self.image = pygame.image.load("slavia_gk.png")
        elif team == "Sparta":
            self.image = pygame.image.load("sparta_gk.png")
        elif team == "Plzeň":
            self.image = pygame.image.load("plzen_gk.png")
        elif team == "Baník":
            self.image = pygame.image.load("banik_gk.png")
        elif team == "Brno":
            self.image = pygame.image.load("brno_gk.png")
        elif team == "Liberec":
            self.image = pygame.image.load("liberec_gk.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Nastavíme nějaké atributy brankáře
        self.speed = 5 # Rychlost pohybu
        self.agility = 10 # Schopnost reagovat na střelu
        self.reflexes = 10 # Schopnost chytit míč

    def update(self):
        # Zde můžeme přidat nějakou logiku pro brankáře
        pass

# Vytvoříme třídu pro střelce
class Shooter(pygame.sprite.Sprite):
    def __init__(self, x, y, team):
        # Zavoláme konstruktor rodičovské třídy
        super().__init__()

        # Nastavíme obrázek a obdélník střelce podle týmu
        if team == "Slavia":
            self.image = pygame.image.load("slavia_sh.png")
        elif team == "Sparta":
            self.image = pygame.image.load("sparta_sh.png")
        elif team == "Plzeň":
            self.image = pygame.image.load("plzen_sh.png")
        elif team == "Baník":
            self.image = pygame.image.load("banik_sh.png")
        elif team == "Brno":
            self.image = pygame.image.load("brno_sh.png")
        elif team == "Liberec":
            self.image = pygame.image.load("liberec_sh.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Nastavíme nějaké atributy střelce
        self.speed = 5 # Rychlost pohybu
        self.power = 10 # Síla střely
        self.accuracy = 10 # Přesnost střely

    def update(self):
        # Zde můžeme přidat nějakou logiku pro střelce
        pass

# Vytvoříme třídu pro fotbalový míč
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Zavoláme konstruktor rodičovské třídy
        super().__init__()

        # Nastavíme obrázek a obdélník míče
        self.image = pygame.image.load("ball.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Nastavíme nějaké atributy míče
        self.velocity_x = 60 # Rychlost v ose x
        self.velocity_y = 60 # Rychlost v ose y

    def update(self):
        # Zde můžeme přidat nějakou logiku pro míč
        pass

# Vytvoříme skupiny pro sprity
all_sprites = pygame.sprite.Group()
goals = pygame.sprite.Group()
goalkeepers = pygame.sprite.Group()
shooters = pygame.sprite.Group()
balls = pygame.sprite.Group()

# Vytvoříme nějaké sprity a přidáme je do skupin
goal1 = Goal(100, 200)
goal2 = Goal(600, 200)
all_sprites.add(goal1, goal2)
goals.add(goal1, goal2)

gk1 = Goalkeeper(150, 250, "Slavia")
gk2 = Goalkeeper(650, 250, "Sparta")
all_sprites.add(gk1, gk2)
goalkeepers.add(gk1, gk2)

sh1 = Shooter(300, 300, "Slavia")
sh2 = Shooter(500, 300, "Sparta")
all_sprites.add(sh1, sh2)
shooters.add(sh1, sh2)

ball = Ball(400, 300)
all_sprites.add(ball)
balls.add(ball)

# Vytvoříme proměnnou pro hlavní smyčku hry
running = True

# Hlavní smyčka hry
while running:
    # Zpracujeme události jako stisk klávesy nebo myši
    for event in pygame.event.get():
        # Pokud uživatel zavře okno, ukončíme hru
        if event.type == pygame.QUIT:
            running = False

    # Aktualizujeme sprity podle jejich logiky
    all_sprites.update()

    # Vyplníme pozadí bílou barvou
    screen.fill(WHITE)

    # Nakreslíme sprity na obrazovku
    all_sprites.draw(screen)

    # Zobrazíme změny na obrazovce
    pygame.display.flip()

# Ukončíme pygame a zavřeme okno
pygame.quit()
