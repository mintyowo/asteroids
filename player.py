from main import *
from circleshape import *
from constants import *
class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.timer = PLAYER_SHOOT_COOLDOWN

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw (self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
    # manages movement and rotation

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt 

    def lateral(self, dt):
        
        lateral = pygame.Vector2(1, 0).rotate(self.rotation)
        self.position += lateral * PLAYER_SPEED * dt

    def rotate(self, dt):

        self.rotation += PLAYER_TURN_SPEED * dt
    # spawns projectles and makes them move, probably a really scuffed way to make different firing
    # modes but idgaf lmao
    def shoot(self):
        shot_list = []
        if self.timer <= 0:
            if SHOTTYPE == 1:
                cool_rotation = -30
                for _ in range(3):
                    shot = Shot(self.position,self.position,SHOT_RADIUS)
                    shot_list.append(shot)
                for shot in shot_list:
                    shot.velocity = pygame.Vector2(0,1).rotate(self.rotation + cool_rotation) * PLAYER_SHOOT_SPEED
                    cool_rotation += 30
            shot = Shot(self.position,self.position,SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN

            # gets inputs and does actions accordingly, yanderedev ass code over here
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-abs(dt))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:

            self.move(-abs(dt))
        if keys[pygame.K_q]:
            self.lateral(dt)
        if keys[pygame.K_e]:
            self.lateral(-abs(dt))
        
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_1]:
            global SHOTTYPE
            SHOTTYPE = 0
        if keys[pygame.K_2]:
            SHOTTYPE = 1

