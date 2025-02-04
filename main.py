# # from os import path
# # from sys import exit
# # import pygame
# #
# # FPS = 60
# # WIDTH = 800
# # HEIGHT = 450
# # CELL_WIDTH = 50
# # CELL_HEIGHT = 50
# #
# #
# # def load_image(name: str) -> pygame.Surface:
# #     fullname = path.join('data', name)
# #     if not path.exists(fullname):
# #         print(f'Файл с изображением {fullname} не найден')
# #         exit(1)
# #     image = pygame.image.load(fullname)
# #     return image
# #
# #
# # def terminate():
# #     pygame.quit()
# #     exit()
# #
# #
# # def start_screen():
# #     intro_text = ['ЗАСТАВКА', '', 'Герой перемещается с помощью стрелок',
# #                   'на клавиатуре', 'Нажмите любую клавшину чтобы продолжить']
# #     background = pygame.transform.scale(
# #         load_image('fon.jpg'), (WIDTH, HEIGHT))
# #     screen.blit(background, (0, 0))
# #     font = pygame.font.Font(None, 30)
# #     text_coord = 50
# #     for line in intro_text:
# #         text = font.render(line, 1, pygame.Color('black'))
# #         text_rect = text.get_rect()
# #         text_rect.top = text_coord
# #         text_rect.left = 10
# #         text_coord += 10
# #         text_coord += text_rect.height
# #         screen.blit(text, text_rect)
# #     is_running = True
# #     clock = pygame.time.Clock()
# #     while is_running:
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 terminate()
# #             elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
# #                 is_running = False
# #                 break
# #         pygame.display.flip()
# #         clock.tick(FPS)
# #
# #
# # class Player(pygame.sprite.Sprite):
# #     image = load_image('mar.png')
# #
# #     def __init__(self, x, y):
# #         super().__init__(player_group)
# #         self.image = Player.image
# #         self.rect = self.image.get_rect()
# #         self.rect.x = x * CELL_WIDTH + 13
# #         self.rect.y = y * CELL_HEIGHT + 5
# #
# #     def update(self, event=None):
# #         if not event:
# #             return
# #         if hasattr(event, 'key'):
# #             last_position = self.rect.x, self.rect.y
# #             if event.key == pygame.K_UP:
# #                 self.rect.y -= CELL_HEIGHT
# #             elif event.key == pygame.K_DOWN:
# #                 self.rect.y += CELL_HEIGHT
# #             elif event.key == pygame.K_LEFT:
# #                 self.rect.x -= CELL_WIDTH
# #             elif event.key == pygame.K_RIGHT:
# #                 self.rect.x += CELL_WIDTH
# #             else:
# #                 return
# #             if self.rect.y < 0 or self.rect.x < 0 or self.rect.y >= HEIGHT\
# #                     or self.rect.x >= WIDTH or pygame.sprite.spritecollideany(self, boxes):
# #                 self.rect.x, self.rect. y = last_position
# #
# #
# # class Cell(pygame.sprite.Sprite):
# #     def __init__(self, x, y, image, group):
# #         super().__init__(group)
# #         self.image = image
# #         self.rect = self.image.get_rect()
# #         self.rect.x = x * CELL_WIDTH
# #         self.rect.y = y * CELL_HEIGHT
# #
# #
# # class Grass(Cell):
# #     image = load_image('grass.png')
# #
# #     def __init__(self, x, y):
# #         super().__init__(x, y, Grass.image, grass)
# #
# #
# # class Box(Cell):
# #     image = load_image('box.png')
# #
# #     def __init__(self, x, y):
# #         super().__init__(x, y, Box.image, boxes)
# #
# #
# # def load_level(number: int):
# #     fullname = path.join('levels', f'{number}.txt')
# #     if not path.exists(fullname):
# #         print('ERROR: Такого уровня не существует')
# #         terminate()
# #     file = open(fullname, 'rt', encoding='utf-8')
# #     level = file.readlines()
# #     for i in range(len(level)):
# #         level[i] = level[i].strip()
# #     file.close()
# #     player_group.empty()
# #     boxes.empty()
# #     grass.empty()
# #     for i in range(len(level)):
# #         for j in range(len(level[0])):
# #             sym = level[i][j]
# #             if sym == '*':
# #                 Box(j, i)
# #             elif sym == '.':
# #                 Grass(j, i)
# #             elif sym == '@':
# #                 Player(j, i)
# #                 Grass(j, i)
# #
# #
# # if __name__ == '__main__':
# #     print('Введите номер уровня (1 и так далее)')
# #     number = int(input())
# #     pygame.init()
# #     pygame.display.set_caption('Перемещение героя')
# #     size = WIDTH, HEIGHT
# #     screen = pygame.display.set_mode(size)
# #     grass = pygame.sprite.Group()
# #     boxes = pygame.sprite.Group()
# #     player_group = pygame.sprite.GroupSingle()
# #     is_running = True
# #     clock = pygame.time.Clock()
# #     start_screen()
# #     load_level(number)
# #     while is_running:
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 is_running = False
# #                 break
# #             elif event.type == pygame.KEYDOWN:
# #                 player_group.update(event)
# #         screen.fill('black')
# #         grass.update()
# #         boxes.update()
# #         player_group.update()
# #         grass.draw(screen)
# #         boxes.draw(screen)
# #         player_group.draw(screen)
# #         pygame.display.flip()
# #         clock.tick(FPS)
# #     terminate()
# #
# # # if __name__ == '__main__':
# # #     paddle = Paddle()
# # #     ball = Ball()
# # #     blocks = create_blocks()
# # #     all_sprites = pygame.sprite.Group()
# # #     all_sprites.add(paddle)
# # #     all_sprites.add(ball)
# # #     all_sprites.add(blocks)
# # #     score = 0
# # #     running = True
# # #     while running:
# # #         for event in pygame.event.get():
# # #             if event.type == pygame.QUIT:
# # #                 running = False
# # #             elif event.type == pygame.KEYDOWN:
# # #                 if event.key == pygame.K_LEFT:
# # #                     paddle.direction = -1
# # #                 elif event.key == pygame.K_RIGHT:
# # #                     paddle.direction = 1
# # #             elif event.type == pygame.KEYUP:
# # #                 paddle.direction = 0
# # #         if pygame.sprite.spritecollide(ball, blocks, True):
# # #
# # #             ball.speed_y *= -1
# # #             score += 1
# # #         if len(blocks) == 0:
# # #             running = False
# # #
# # #         if pygame.sprite.collide_rect(ball, paddle):
# # #             ball.speed_y *= -1
# # #         if ball.rect.y > HEIGHT:
# # #             running = False
# # #
# # #         screen.fill(BLACK)
# # #         all_sprites.update()
# # #         all_sprites.draw(screen)
# # #         pygame.display.flip()
# # #         clock.tick(60)
# import pygame
# from random import randint
#
# all_sprites = pygame.sprite.Group()
# vertical_borders = pygame.sprite.Group()
# horizontal_borders = pygame.sprite.Group()
#
#
# class Ball(pygame.sprite.Sprite):
#     def __init__(self, radius, x, y):
#         super().__init__(all_sprites)
#         self.radius = radius
#         self.image = pygame.Surface((2 * radius, 2 * radius),
#                                     pygame.SRCALPHA, 32)
#         pygame.draw.circle(self.image, pygame.Color("red"),
#                            (radius, radius), radius)
#         self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
#         self.vx = randint(-5, 5)
#         self.vy = randint(-5, 5)
#
#     def update(self):
#         self.rect = self.rect.move(self.vx, self.vy)
#         if pygame.sprite.spritecollideany(self, horizontal_borders):
#             self.vy = -self.vy
#         if pygame.sprite.spritecollideany(self, vertical_borders):
#             self.vx = -self.vx
#
#
# class Border(pygame.sprite.Sprite):
#     def __init__(self, x1, y1, x2, y2):
#         super().__init__(all_sprites)
#         if x1 == x2:  # вертикальная стенка
#             self.add(vertical_borders)
#             self.image = pygame.Surface([1, y2 - y1])
#             self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
#         else:  # горизонтальная стенка
#             self.add(horizontal_borders)
#             self.image = pygame.Surface([x2 - x1, 1])
#             self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
#
#
# if __name__ == '__main__':
#     width = 500
#     height = 500
#     # Border(5, 5, width - 5, 5)
#     # Border(5, height - 5, width - 5, height - 5)
#     # Border(5, 5, 5, height - 5)
#     Border(width - 5, 5, width - 5, height - 5)
#
#     for i in range(20):
#         Ball(20, 100, 100)
#
#     pygame.init()
#     pygame.display.set_caption('Balls')
#     size = width, height = 500, 500
#     screen = pygame.display.set_mode(size)
#     is_running = True
#     clock = pygame.time.Clock()
#     while is_running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 is_running = False
#                 break
#         screen.fill('white')
#         all_sprites.update()
#         vertical_borders.update()
#         horizontal_borders.update()
#
#         all_sprites.draw(screen)
#         vertical_borders.draw(screen)
#         horizontal_borders.draw(screen)
#         pygame.display.flip()
#         clock.tick(60)
#     pygame.quit()
