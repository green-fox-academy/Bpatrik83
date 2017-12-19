import random
from tkinter import *
from time import sleep
from Controller import *

root = Tk()

img_floor = PhotoImage(file = "image/floor.gif")
img_wall = PhotoImage(file = "image/wall.gif")
game_map = "map/game_map.txt"
hero_up = PhotoImage(file = "image/hero-up.gif")
hero_down = PhotoImage(file = "image/hero-down.gif")
hero_left = PhotoImage(file = "image/hero-left.gif")
hero_right = PhotoImage(file = "image/hero-right.gif")
skeleton = PhotoImage(file = "image/skeleton.gif")
boss = PhotoImage(file = "image/boss.gif")
dead = PhotoImage(file = "image/you_are_dead.gif")
skull = PhotoImage(file = "image/skull.png")
cartman = PhotoImage(file = "image/Cartman-Ninja-icon.png")

canvas = Canvas(root, width = 720, height = 800, bg = "white")
canvas.pack()


class Models():
    def __init__(self):
        self.tile_size = 72
        self.game_map = "map/game_map.txt"

    def draw_tiles(self):
        wall_list = controller.open_map_file(game_map)
        for i, lines in enumerate(wall_list):
            for j, char in enumerate(lines):
                if char == "0":
                    canvas.create_image(self.tile_size / 2 + j * self.tile_size, self.tile_size / 2 + i * self.tile_size, image = img_floor)
                else:
                    canvas.create_image(self.tile_size / 2 + j * self.tile_size, self.tile_size / 2 + i * self.tile_size, image = img_wall)

class Monsters():
    def __init__(self):
        self.wall_list = controller.open_map_file(game_map)
        self.position_x = random.randrange(36, 756, 72)
        self.position_y = random.randrange(36, 756, 72)
        self.is_wall_position_x = int((self.position_x - 36) / 72)
        self.is_wall_position_y = int((self.position_y - 36) / 72)

    def randomize(self):
        self.position_x = random.randrange(36, 756, 72)
        self.position_y = random.randrange(36, 756, 72)
        self.is_wall_position_x = int((self.position_x - 36) / 72)
        self.is_wall_position_y = int((self.position_y - 36) / 72)

    def check_position(self):
        monsters.randomize()
        while self.wall_list[self.is_wall_position_y][self.is_wall_position_x] == "1":
            monsters.randomize()

    def draw_skeleton_one(self, skeleton_image = skeleton):
        monsters.check_position()
        self.skeleton_one_position_x = (self.position_x - 36) / 72
        self.skeleton_one_position_y = (self.position_y - 36) / 72
        self.skeleton_image = canvas.create_image(self.position_x, self.position_y, image = skeleton_image)

    def draw_skeleton_two(self, skeleton_image = skeleton):
        monsters.check_position()
        self.skeleton_two_position_x = (self.position_x - 36) / 72
        self.skeleton_two_position_y = (self.position_y - 36) / 72
        self.skeleton_image = canvas.create_image(self.position_x, self.position_y, image = skeleton_image)

    def draw_skeleton_three(self, skeleton_image = skeleton):
        monsters.check_position()
        self.skeleton_three_position_x = (self.position_x - 36) / 72
        self.skeleton_three_position_y = (self.position_y - 36) / 72
        self.skeleton_image = canvas.create_image(self.position_x, self.position_y, image = skeleton_image)

    def draw_boss(self):
        monsters.check_position()
        self.boss_x = (self.position_x - 36) / 72
        self.boss_y = (self.position_y - 36) / 72
        self.skeleton_image = canvas.create_image(self.position_x, self.position_y, image=boss)

class Hero():
    def __init__(self):
        self.hero_coordinate_x = 36
        self.hero_coordinate_y = 36
        self.x_position = 0
        self.y_position = 0

    def move_hero(self, hero_position_x, hero_position_y):
        self.hero_position_x = hero_position_x
        self.hero_position_y = hero_position_y
        canvas.move(self.hero_image, hero_position_x, hero_position_y)

    def draw_hero(self, hero_image=hero_down):
        self.hero_image = canvas.create_image(self.hero_coordinate_x, self.hero_coordinate_y, image=hero_image)

class Stats():
    def basic_information(self):
        canvas.create_text(40, 730, text = "Hero HP")
        self.hp = canvas.create_rectangle(70, 723, 90, 737, fill="white")
        self.hp = canvas.create_text(80, 730, text=fight.hp_hero)
        canvas.create_text(40, 750, text="Hero Level")
        self.hp = canvas.create_rectangle(70, 743, 90, 757, fill="white")
        self.hp = canvas.create_text(80, 750, text=fight.hero_level)
        canvas.create_text(170, 730, text="Skeleton one HP")
        self.hp = canvas.create_rectangle(220, 723, 240, 737, fill="white")
        self.hp = canvas.create_text(230, 730, text=fight.hp_skeleton_one)
        canvas.create_text(370, 730, text="Skeleton two HP")
        self.hp = canvas.create_rectangle(420, 723, 440, 737, fill="white")
        self.hp = canvas.create_text(430, 730, text=fight.hp_skeleton_two)
        canvas.create_text(570, 730, text="Skeleton three HP")
        self.hp = canvas.create_rectangle(620, 723, 640, 737, fill="white")
        self.hp = canvas.create_text(630, 730, text=fight.hp_skeleton_three)
        canvas.create_text(370, 750, text="BOSS HP")
        self.hp = canvas.create_rectangle(420, 743, 440, 757, fill="white")
        self.hp = canvas.create_text(430, 750, text=fight.hp_boss)

    def Hp(self):
        self.hp = canvas.create_rectangle(70, 723, 90, 737, fill="white")
        self.hp = canvas.create_text(80, 730, text=fight.hp_hero)
        self.hp = canvas.create_rectangle(220, 723, 240, 737, fill="white")
        self.hp = canvas.create_text(230, 730, text=fight.hp_skeleton_one)
        self.hp = canvas.create_rectangle(420, 723, 440, 737, fill="white")
        self.hp = canvas.create_text(430, 730, text=fight.hp_skeleton_two)
        self.hp = canvas.create_rectangle(620, 723, 640, 737, fill="white")
        self.hp = canvas.create_text(630, 730, text=fight.hp_skeleton_three)
        self.hp = canvas.create_rectangle(420, 743, 440, 757, fill="white")
        self.hp = canvas.create_text(430, 750, text=fight.hp_boss)
        self.hp = canvas.create_rectangle(70, 743, 90, 757, fill="white")
        self.hp = canvas.create_text(80, 750, text=fight.hero_level)

class Fight():
    def __init__(self):
        self.hp_hero = 30
        self.hp_skeleton_one = 3
        self.hp_skeleton_two = 4
        self.hp_skeleton_three = 5
        self.hp_boss = 10
        self.hero_level = 1

    def check_is_fight(self):
        if hero.y_position == monsters.skeleton_one_position_y and hero.x_position == monsters.skeleton_one_position_x\
                and self.hp_skeleton_one > 0:
            self.hp_hero -= 1
            self.hp_skeleton_one -= 1
        if hero.y_position == monsters.skeleton_two_position_y and hero.x_position == monsters.skeleton_two_position_x\
                and self.hp_skeleton_two > 0:
            self.hp_hero -= 1
            self.hp_skeleton_two -= 1
        if hero.y_position == monsters.skeleton_three_position_y and hero.x_position == monsters.skeleton_three_position_x\
                and self.hp_skeleton_three > 0:
            self.hp_hero -= 1
            self.hp_skeleton_three -= 1
        if hero.y_position == monsters.boss_y and hero.x_position == monsters.boss_x\
                and self.hp_boss > 0:
            self.hp_hero -= 1
            self.hp_boss -= 1

    def is_dead(self):
        if self.hp_hero < 1:
            canvas.create_image(400, 400, image=dead)
            sleep(1)
            sys.exit()
        if self.hp_skeleton_one == 0:
            monsters.skeleton_image = canvas.create_image(monsters.skeleton_one_position_x * 72 + 36,
            monsters.skeleton_one_position_y * 72 + 36, image=skull)
        if self.hp_skeleton_two == 0:
            monsters.skeleton_image = canvas.create_image(monsters.skeleton_two_position_x * 72 + 36,
            monsters.skeleton_two_position_y * 72 + 36, image=skull)
        if self.hp_skeleton_three == 0:
            monsters.skeleton_image = canvas.create_image(monsters.skeleton_three_position_x * 72 + 36,
            monsters.skeleton_three_position_y * 72 + 36, image=skull)
        if self.hp_boss == 0:
            monsters.b = canvas.create_image(monsters.boss_x * 72 + 36,
            monsters.boss_y * 72 + 36, image=skull)
        if self.hp_skeleton_one == 0 and self.hp_skeleton_two == 0 and self.hp_skeleton_three == 0 and self.hp_boss == 0:
           fight.new_game()

    def new_game(self):
        models.draw_tiles()
        self.hp_hero = 30
        self.hp_skeleton_one = 3
        self.hp_skeleton_two = 4
        self.hp_skeleton_three = 5
        self.hp_boss = 10
        self.hero_level += 1
        hero.__init__()
        monsters.draw_skeleton_one()
        monsters.draw_skeleton_two()
        monsters.draw_skeleton_three()
        monsters.draw_boss()
        hero.draw_hero()

def on_key_press(e):
    wall_list = controller.open_map_file(game_map)
    if (e.keysym == "Up") and hero.y_position > 0 and wall_list[hero.y_position - 1][hero.x_position] != "1":
        hero.move_hero(0, - 72)
        hero.y_position -= 1
    elif (e.keysym == 'Down') and hero.y_position < 9 and wall_list[hero.y_position + 1][hero.x_position] != "1":
        hero.move_hero(0, 72)
        hero.y_position += 1
    elif (e.keysym == 'Left') and hero.x_position > 0 and wall_list[hero.y_position][hero.x_position - 1] != "1":
        hero.move_hero(-72, 0)
        hero.x_position -= 1
    elif (e.keysym == 'Right') and hero.x_position < 9 and wall_list[hero.y_position][hero.x_position + 1] != "1":
        hero.move_hero(72, 0)
        hero.x_position += 1
    fight.is_dead()
    fight.check_is_fight()
    stats.Hp()

controller = Controller()
models = Models()
models.draw_tiles()
hero = Hero()
monsters = Monsters()
monsters.draw_skeleton_one()
monsters.draw_skeleton_two()
monsters.draw_skeleton_three()
monsters.draw_boss()
fight = Fight()
stats = Stats()
hero.draw_hero()
stats.basic_information()
root.bind("<KeyPress>", on_key_press)

root.mainloop()