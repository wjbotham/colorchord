import pygame
from threading import Thread
from time import clock
from bullet import Bullet
from player import Player

class Game:
    def __init__(self, width=500, height=500):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        self.graphics_loop_running = False
        self.game_running = False
        self.bullets = []
        self.player = Player(250, 250, 0, 0)

    def quit(self):
        while self.graphics_loop_running:
            pass
        pygame.quit()

    def play(self):
        gu_thread = Thread(target=self.graphics_update_loop)
        self.game_running = True
        gu_thread.start()
        while self.game_running:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.shoot(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == 119:   # W
                    self.player.w_down = True
                elif event.key == 97:  # A
                    self.player.a_down = True
                elif event.key == 115: # S
                    self.player.s_down = True
                elif event.key == 100: # D
                    self.player.d_down = True
                else:
                    print(event)
            elif event.type == pygame.KEYUP:
                if event.key == 119:   # W
                    self.player.w_down = False
                elif event.key == 97:  # A
                    self.player.a_down = False
                elif event.key == 115: # S
                    self.player.s_down = False
                elif event.key == 100: # D
                    self.player.d_down = False
                else:
                    print(event)
            elif event.type == pygame.QUIT:
                self.game_running = False
            #else:
                #print(event)
        self.quit()

    def shoot(self, pos):
        self.bullets.append(Bullet(self.player, pos[0], pos[1], 2, 30))

    def tick(self):
        cleanup = []
        for bullet in self.bullets:
            bullet.tick()
            if bullet.needs_cleanup:
                cleanup.append(bullet)
        self.player.tick()
        for bullet in cleanup:
            self.bullets.remove(bullet)

    def graphics_update_loop(self):
        seconds_per_frame = 1/30
        next_update = clock() + seconds_per_frame
        self.graphics_loop_running = True
        while self.game_running:
            while clock() < next_update:
                pass
            self.tick()
            self.update()
            next_update += seconds_per_frame
        self.graphics_loop_running = False

    def update(self):
        self.window.fill((0,0,0))
        for bullet in self.bullets:
            pygame.draw.circle(self.window, (255,255,255), bullet.position, 0, 0)
        pygame.draw.circle(self.window, (255,0,0), self.player.position, 3, 0)
        pygame.display.flip()
