import pygame
from os import path
from sys import exit
from random import choice, randint

pygame.init()

level = []
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WIDTH = 650
HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
wi = False
BALL_RADIUS = 200
BALL_SPEED_X = 5
BALL_SPEED_Y = -5
leve = 5
BLOCK_WIDTH = 70
BLOCK_HEIGHT = 20
BLOCK_MARGIN = 10
BLOCK_ROWS = 5
BLOCK_COLS = 8
color = 'white'
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоид")
live = 3
clock = pygame.time.Clock()


def load_image(name: str) -> pygame.Surface:
    fullname = path.join('data', name)
    if not path.exists(fullname):
        print(f'Файл с изображением {fullname} не найден')
        exit(1)
    image = pygame.image.load(fullname)
    return image


def win_screen():
    global leve
    pygame.display.set_caption('game')
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    intro_text = ['', '', 'Нажмите любую клавишу клавиатуры', 'чтобы перейти на следующий уровень',
                  'Нажмите любую клавшину мыши', 'чтобы начать заново', f'Вы на уровне {leve}']
    background = pygame.transform.scale(
        load_image('фон4.jpeg'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        text = font.render(line, 1, pygame.Color('green'))
        text_rect = text.get_rect()
        text_rect.top = text_coord
        text_rect.left = 10
        text_coord += 10
        text_coord += text_rect.height
        screen.blit(text, text_rect)
    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 7
            elif event.type in [pygame.KEYDOWN]:
                leve += 1
                return 2
            elif event.type in [pygame.MOUSEBUTTONDOWN]:
                return 2
        pygame.display.flip()
        clock.tick(FPS)


def over_screen():
    global leve
    pygame.display.set_caption('game')
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    intro_text = ['', '', 'Нажмите любую клавшину', 'чтобы начать заново', f'Вы на уровне {leve}',
                  'Игра начнётся сначала (уровня 1)']
    background = pygame.transform.scale(
        load_image('фон6.jpeg'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        text = font.render(line, 1, pygame.Color('green'))
        text_rect = text.get_rect()
        text_rect.top = text_coord
        text_rect.left = 10
        text_coord += 10
        text_coord += text_rect.height
        screen.blit(text, text_rect)
    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 7
                pygame.quit()
            elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
                # leve = 1
                return 2
                is_running = False
                break
        pygame.display.flip()
        clock.tick(FPS)


def end_screen():
    pygame.init()
    pygame.display.set_caption('Арканоид')
    pygame.mixer.music.pause()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    global leve
    intro_text = ["       Поздравляю!", 'Вы прошли все уровни!',
                  '    Чтобы начать всё сначала, ',
                  '       нажмите любую клавшину клавиатуры', '     Чтобы выйти, нажмите любую клавишу мыши ']
    background = pygame.transform.scale(
        load_image('фон12.jpeg'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        text = font.render(line, 1, pygame.Color('green'))
        text_rect = text.get_rect()
        text_rect.top = text_coord
        text_rect.left = 10
        text_coord += 10
        text_coord += text_rect.height
        screen.blit(text, text_rect)
    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 7
            elif event.type in [pygame.KEYDOWN]:
                leve = 1
                pygame.mixer.music.unpause()
                return 1
            elif event.type in [pygame.MOUSEBUTTONDOWN]:
                leve = 1
                pygame.mixer.music.unpause()
                return 1
        pygame.display.flip()
        clock.tick(FPS)
    leve = 1
    return 1


def start_screen():
    pygame.init()
    pygame.display.set_caption('Арканоид')
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    global leve
    intro_text = ['                                      АРКАНОИД', '', 'Чтобы сделать паузу в игре, нажмите пробел',
                  'Красные бонусы с "Ш" уменьшают шар,', ' а зелёные увеличивают',
                  'Красные бонусы с "П" уменьшают платформу,', ' а зелёные увеличивают',
                  'Синие со стрелкой вверх ускоряют мяч, вниз - замедляют', '', '',
                  'Платформа перемещается с помощью ', 'стрелок на клавиатуре', 'Нажмите любую клавшину чтобы начать',
                  f'Вы на уровне {leve}']
    background = pygame.transform.scale(
        load_image('фон12.jpeg'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        text = font.render(line, 1, pygame.Color('green'))
        text_rect = text.get_rect()
        text_rect.top = text_coord
        text_rect.left = 10
        text_coord += 10
        text_coord += text_rect.height
        screen.blit(text, text_rect)
    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 7
                pygame.quit()
            elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
                is_running = False
                return 2
        pygame.display.flip()
        clock.tick(FPS)
    return 2


def exit_screen():
    pygame.init()
    pygame.display.set_caption('Арканоид')
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    global leve
    leve = 1
    intro_text = [" ", '', '', '', '', '                          Вы уверены, что хотите выйти?!', ' ', ' ', ' ', ' ',
                  ' ', ' ',
                  '                          если ДА, то нажмите на крестик ',
                  '                          если НЕТ, то нажмите на любую кнопку']
    background = pygame.transform.scale(
        load_image('фон11.jpeg'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        text = font.render(line, 1, pygame.Color('yellow'))
        text_rect = text.get_rect()
        text_rect.top = text_coord
        text_rect.left = 10
        text_coord += 10
        text_coord += text_rect.height
        screen.blit(text, text_rect)
    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 5
                pygame.quit()
            elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
                is_running = False
                leve = 1
                return 2
        pygame.display.flip()
        clock.tick(FPS)
    return 2


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH - self.width) // 2
        self.rect.y = HEIGHT - self.height - 10
        self.direction = 0
        self.speed = 10

    def update(self):
        self.rect.x += self.direction * self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - PADDLE_WIDTH:
            self.rect.x = WIDTH - PADDLE_WIDTH

    def bigger(self):
        self.width += 20
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 100, 100))
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def smaller(self):
        self.width -= 20
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 100, 100))
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


class Bonus(pygame.sprite.Sprite):
    type_of_bonus = ["Шар увеличение.png", "Шар уменьшение.png", 'Ускорение шара.png', "Замедление шара.png",
                     "Панель увеличение.png", "Панель уменьшение.png"]
    def __init__(self):
        super().__init__()
        self.n = 8
        self.t = choice([1, 2, 3, 5, 6])
        sheet = load_image(self.type_of_bonus[self.t - 1])
        self.frames = []
        self.cut_sheet(sheet, 4, self.n)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(20, 20)
        self.rect.x = randint(100, 600)
        self.rect.y = 100
        self.speed_x = 0
        self.speed_y = 2

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, ball, paddle):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x < 0 or self.rect.x > WIDTH - 10 * 2:
            self.speed_x *= -1
        if self.rect.y < 0:
            self.speed_y *= -1
        if pygame.sprite.collide_rect(self, paddle):
            if self.t == 1:
                ball.bigger()
                # Бон_расшир_шар.png
            elif self.t == 2:
                ball.smaller()
                #
            elif self.t == 3:
                if ball.speed_y > 0:
                    ball.speed_y += 2
                else:
                    ball.speed_y -= 2
                if ball.speed_x > 0:
                    ball.speed_x += 2
                else:
                    ball.speed_x -= 2
                # Бон_ускор_шар.png
            elif self.t == 4:
                ball.speed_y /= 2
                ball.speed_x /= 2
            elif self.t == 5:
                paddle.bigger()
            else:
                paddle.smaller()
            self.kill()


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, BALL_RADIUS):
        super().__init__()
        self.rad = BALL_RADIUS
        self.image = pygame.Surface([self.rad * 2, self.rad * 2])
        self.image.set_colorkey(BLACK)
        self.colors = color
        pygame.draw.circle(self.image, self.colors, (self.rad, self.rad), self.rad)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH - BALL_RADIUS) // 2
        self.rect.y = HEIGHT - PADDLE_HEIGHT - BALL_RADIUS * 2 - 10
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x < 0 or self.rect.x > WIDTH - self.rad * 2:
            self.speed_x *= -1
        if self.rect.y < 0:
            self.speed_y *= -1

    def bigger(self):
        self.rad *= 2
        self.image = pygame.Surface([self.rad * 2, self.rad * 2])
        self.image.set_colorkey(BLACK)
        pygame.draw.circle(self.image, self.colors, (self.rad, self.rad), self.rad)
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def smaller(self):
        self.rad /= 2
        self.image = pygame.Surface([self.rad * 2, self.rad * 2])
        self.image.set_colorkey(BLACK)
        pygame.draw.circle(self.image, self.colors, (self.rad, self.rad), self.rad)
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface([BLOCK_WIDTH, BLOCK_HEIGHT])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 1

    def update(self, ball, all_blocks, all_sprites, all_bonus):
        if pygame.sprite.collide_rect(ball, self):
            self.hp -= 1
            print(self.hp)
            if self.hp == 2:
                Block2(self.rect.x, self.rect.y, all_blocks, all_sprites)
                bonus = Bonus()
                all_sprites.add(bonus)
                all_bonus.add(bonus)
            #     TODO
            # жизни
            # картинки и анимация к бонусам

            if self.hp == 1:
                Block1(self.rect.x, self.rect.y, all_blocks, all_sprites)
            ball.speed_y *= -1
            self.kill()


class Block1(Block):
    def __init__(self, x, y, *groups):
        super().__init__(x, y, *groups)
        self.image.fill(GREEN)
        self.hp = 1


class Block2(Block):
    def __init__(self, x, y, *groups):
        super().__init__(x, y, *groups)
        self.image.fill('yellow')
        self.hp = 2


class Block3(Block):
    def __init__(self, x, y, *groups):
        super().__init__(x, y, *groups)
        self.image.fill(RED)
        self.hp = 3


def load_level(number: int):
    global level
    global leve
    global con
    fullname = path.join('levels', f'{number}.txt')
    if not path.exists(fullname):
        print('ERROR: Такого уровня не существует')
        con = end_screen()
        if con == 1:
            leve = 1
            number = 1
        else:
            exit(1)
    fullname = path.join('levels', f'{number}.txt')
    file = open(fullname, 'rt', encoding='utf-8')
    level = file.readlines()
    for i in range(len(level)):
        level[i] = (level[i].strip()).split()
    file.close()


def create_blocks(all_blocks, all_sprites):
    block_list = pygame.sprite.Group()
    le = leve
    load_level(leve)
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLS):
            if level[row][col] == '1':
                block = Block1(col * (BLOCK_WIDTH + BLOCK_MARGIN) + BLOCK_MARGIN,
                              row * (BLOCK_HEIGHT + BLOCK_MARGIN) + BLOCK_MARGIN, all_blocks, all_sprites)
                block_list.add(block)
            elif level[row][col] == '2':
                block = Block2(col * (BLOCK_WIDTH + BLOCK_MARGIN) + BLOCK_MARGIN,
                               row * (BLOCK_HEIGHT + BLOCK_MARGIN) + BLOCK_MARGIN, all_blocks, all_sprites)
                block_list.add(block)
            elif level[row][col] == '3':
                block = Block3(col * (BLOCK_WIDTH + BLOCK_MARGIN) + BLOCK_MARGIN,
                               row * (BLOCK_HEIGHT + BLOCK_MARGIN) + BLOCK_MARGIN, all_blocks, all_sprites)
                block_list.add(block)
            else:
                pass
    return block_list


def game(lev):
    pygame.init()
    pygame.mixer.music.load("Exyl - A Rare Call in Winter.mp3")
    pygame.mixer.music.play(-1)
    pygame.display.set_caption('Арканоид')
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    paddle = Paddle()
    ball = Ball(color, BALL_RADIUS)
    all_bonus = pygame.sprite.Group()
    all_blocks = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(paddle)
    all_sprites.add(ball)
    blocks = create_blocks(all_blocks, all_sprites)
    score = 0
    life = live
    is_running = True
    play = True
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.pause()
                return 7
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play = False
                if event.key == pygame.K_LEFT:
                    paddle.direction = -1
                elif event.key == pygame.K_RIGHT:
                    paddle.direction = 1
            elif event.type == pygame.KEYUP and event.type != pygame.K_SPACE:
                paddle.direction = 0

        if play:
            if len(all_blocks) == 0:
                pygame.mixer.music.pause()
                return 3
            if pygame.sprite.collide_rect(ball, paddle):
                ball.speed_y *= -1
            if ball.rect.y > HEIGHT:
                pygame.mixer.music.pause()
                return 4
            if leve % 3 == 0:
                background = pygame.transform.scale(
                    load_image('фон5.jpeg'), (WIDTH, HEIGHT))
            if leve % 3 == 1:
                background = pygame.transform.scale(
                    load_image('фон9.jpeg'), (WIDTH, HEIGHT))
            if leve % 3 == 2:
                background = pygame.transform.scale(
                    load_image('фон7.jpeg'), (WIDTH, HEIGHT))
            screen.blit(background, (0,0))
            ball.update()
            paddle.update()
            all_bonus.update(ball, paddle)
            all_blocks.update(ball, all_blocks, all_sprites, all_bonus)
            all_sprites.draw(screen)
            pygame.display.flip()
            clock.tick(60)
        else:
            pygame.mixer.music.pause()
            intro_text = ['', '', 'Нажмите любую клавшину', 'чтобы продолжить',
                          '', '=]']
            background = pygame.transform.scale(
                load_image('фон3.jpeg'), (WIDTH, HEIGHT))
            screen.blit(background, (0, 0))
            font = pygame.font.Font(None, 30)
            text_coord = 50
            for line in intro_text:
                text = font.render(line, 1, pygame.Color('green'))
                text_rect = text.get_rect()
                text_rect.top = text_coord
                text_rect.left = 10
                text_coord += 10
                text_coord += text_rect.height
                screen.blit(text, text_rect)
            running = True
            clock = pygame.time.Clock()
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return 7
                        pygame.quit()
                    elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
                        play = True
                        pygame.mixer.music.unpause()
                        running = False
                pygame.display.flip()
                clock.tick(FPS)
    return 5
    pygame.quit()


con = 1
if __name__ == "__main__":
    while con:
        if con == 1:
            con = start_screen()
        elif con == 2:
            con = game(leve)
        elif con == 3:
            con = win_screen()
        elif con == 4:
            con = over_screen()
        elif con == 6:
            con = end_screen()
        elif con == 7:
            con = exit_screen()
        else:
            break
