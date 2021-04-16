from sense_emu import SenseHat
from Controls_Level_1 import Controls_Level_1
from animation_lose_level_1 import animation_lose_level_1
from animation_win_level_1 import animation_win_level_1
from ENTERING_MAIN_MENU import ENTERING_MAIN_MENU
from afisare_imagine_de_sfarsit_de_nivel_1 import afisare_imagine_de_sfarsit_de_nivel_1
from afisare_imagine_de_sfarsit_de_nivel_2 import afisare_imagine_de_sfarsit_de_nivel_2
from time import sleep

sense = SenseHat()

#CULORI pentru SenseHat (COLOURS for the SenseHat):
black = [0, 0, 0]
cyan = [0, 255, 255]
blue = [0, 0, 255]
darker_blue = [0, 102, 204]
red = [248, 0, 0]
gold = [248, 212, 0]
green = [0, 255, 0]
white = [255, 255, 255]
purple = [128, 0, 128]
orange = [255, 140, 0]
brown = [136, 68, 16]
coral = [255, 160, 122]
toxicgreen = [97, 222, 42]
darkgreen = [0, 100, 0]
pink = [255, 113, 181]
yellow = [255, 255, 0]
darkbrown = [101, 67, 33]
magenta = [255, 0, 255]
brown2 = [210, 105, 30]
water = [24, 160, 232]
dimgrey = [104, 104, 104]

#FUNCTIE PENTRU NIVELUL 1 (LEVEL 1 FUNCTION)

def Level1():
    Controls_Level_1()
    image_level1 = [
        black, black, black, black, dimgrey, black, red, purple,
        black, pink, gold, black, dimgrey, black, red, red,
        black, black, black, black, dimgrey, black, black, black,
        dimgrey, dimgrey, dimgrey, black, black, dimgrey, water, water,
        black, gold, water, black, black, black, black, black,
        black, black, water, black, black, water, water, water,
        black, gold, water, black, black, water, brown, black,
        dimgrey, black, water, black, black, water, black, black,
    ]
    sense.set_pixels(image_level1)
    vector_y = 1
    vector_x = 1
    has_wooden_bucket_fire = False
    has_wooden_bucket_water = 0
    has_wooden_bucket = False
    has_flag = False
    while has_flag == False:
        pixels1 = sense.get_pixels()
        event4 = sense.stick.wait_for_event(emptybuffer = True)
        if event4.action == "pressed" and event4.direction == "up" and vector_x > 0 and pixels1[8 * (vector_x - 1) + vector_y] != dimgrey:
            if pixels1[8 * (vector_x - 1) + vector_y] == gold and vector_x - 2 >= 0 and pixels1[8 * (vector_x - 2) + vector_y] != dimgrey:
                if pixels1[8 * (vector_x - 2) + vector_y] == water:
                    sense.set_pixel(vector_y, vector_x - 2, black)
                    sense.set_pixel(vector_y, vector_x - 1, black)
                elif pixels1[8 * (vector_x - 2) + vector_y] == red:
                    sense.set_pixel(vector_y, vector_x - 1, black)
                elif pixels1[8 * (vector_x - 2) + vector_y] == gold:
                    continue
                else:
                    sense.set_pixel(vector_y, vector_x - 1, black)
                    sense.set_pixel(vector_y, vector_x - 2, gold)
            elif pixels1[8 * (vector_x - 1) + vector_y] == gold and (vector_x - 2 < 0 or pixels1[8 * (vector_x - 2) + vector_y] == dimgrey):
                continue
            elif pixels1[8 * (vector_x - 1) + vector_y] == water:
                if has_wooden_bucket_water == 0 and has_wooden_bucket == True:
                    has_wooden_bucket_water = 1
                    sense.set_pixel(vector_y, vector_x - 1, black)
                else:
                    animation_lose_level_1()
                    break
            elif pixels1[8 * (vector_x - 1) + vector_y] == brown:
                has_wooden_bucket = True
                sense.set_pixel(vector_y, vector_x, black)
                vector_x = vector_x - 1
                sense.set_pixel(vector_y, vector_x, pink)
            elif pixels1[8 * (vector_x - 1) + vector_y] == red:
                if has_wooden_bucket_water == 1 and has_wooden_bucket == True and has_wooden_bucket_fire == False:
                    sense.set_pixel(vector_y, vector_x - 1, black)
                    has_wooden_bucket_fire = True
                    has_wooden_bucket_water = 0
                else:
                    animation_lose_level_1()
                    break
            elif pixels1[8 * (vector_x - 1) + vector_y] == purple:
                animation_win_level_1()
                sleep(2)
                has_flag = True
            else:
                sense.set_pixel(vector_y, vector_x, black)
                vector_x = vector_x - 1
                sense.set_pixel(vector_y, vector_x, pink)
        elif event4.action == "pressed" and event4.direction == "down" and vector_x < 7 and pixels1[8 * (vector_x + 1) + vector_y] != dimgrey:
            if pixels1[8 * (vector_x + 1) + vector_y] == gold and vector_x + 2 <= 7 and pixels1[8 * (vector_x + 2) + vector_y] != dimgrey:
                if pixels1[8 * (vector_x + 2) + vector_y] == water:
                    sense.set_pixel(vector_y, vector_x + 2, black)
                    sense.set_pixel(vector_y, vector_x + 1, black)
                elif pixels1[8 * (vector_x + 2) + vector_y] == red:
                    sense.set_pixel(vector_y, vector_x + 1, black)
                elif pixels1[8 * (vector_x + 2) + vector_y] == gold:
                    continue
                else:
                    sense.set_pixel(vector_y, vector_x + 1, black)
                    sense.set_pixel(vector_y, vector_x + 2, gold)
            elif pixels1[8 * (vector_x + 1) + vector_y] == gold and (vector_x + 2 > 7 or pixels1[8 * (vector_x + 2) + vector_y] == dimgrey):
                continue
            elif pixels1[8 * (vector_x + 1) + vector_y] == water:
                if has_wooden_bucket_water == 0 and has_wooden_bucket == True:
                    has_wooden_bucket_water = 1
                    sense.set_pixel(vector_y, vector_x + 1, black)
                else:
                    animation_lose_level_1()
                    break
            elif pixels1[8 * (vector_x + 1) + vector_y] == brown:
                has_wooden_bucket = True
                sense.set_pixel(vector_y, vector_x, black)
                vector_x = vector_x + 1
                sense.set_pixel(vector_y, vector_x, pink)
            elif pixels1[8 * (vector_x + 1) + vector_y] == red:
                if has_wooden_bucket_water == 1 and has_wooden_bucket == True and has_wooden_bucket_fire == False:
                    sense.set_pixel(vector_y, vector_x + 1, black)
                    has_wooden_bucket_fire = True
                    has_wooden_bucket_water = 0
                else:
                    animation_lose_level_1()
                    break
            elif pixels1[8 * (vector_x + 1) + vector_y] == purple:
                animation_win_level_1()
                sleep(2)
                has_flag = True
            else:
                sense.set_pixel(vector_y, vector_x, black)
                vector_x = vector_x + 1
                sense.set_pixel(vector_y, vector_x, pink)
        elif event4.action == "pressed" and event4.direction == "left" and vector_y > 0 and pixels1[8 * vector_x + vector_y - 1] != dimgrey:
            if pixels1[8 * vector_x + vector_y - 1] == gold and vector_y - 2 >= 0 and pixels1[8 * vector_x + vector_y - 2] != dimgrey:
                if pixels1[8 * vector_x + vector_y - 2] == water:
                    sense.set_pixel(vector_y - 1, vector_x, black)
                    sense.set_pixel(vector_y - 2, vector_x, black)
                elif pixels1[8 * vector_x + vector_y - 2] == red:
                    sense.set_pixel(vector_y - 1, vector_x, black)
                elif pixels1[8 * vector_x + vector_y - 2] == gold:
                    continue
                else:
                    sense.set_pixel(vector_y - 1, vector_x, black)
                    sense.set_pixel(vector_y - 2, vector_x, gold)
            elif pixels1[8 * vector_x + vector_y - 1] == gold and (vector_y - 2 < 0 or pixels1[8 * vector_x + vector_y - 2] == dimgrey):
                continue
            elif pixels1[8 * vector_x + vector_y - 1] == water:
                if has_wooden_bucket_water == 0 and has_wooden_bucket == True:
                    has_wooden_bucket_water = 1
                    sense.set_pixel(vector_y - 1, vector_x, black)
                else:
                    animation_lose_level_1()
                    break
            elif pixels1[8 * vector_x + vector_y - 1] == brown:
                has_wooden_bucket = True
                sense.set_pixel(vector_y, vector_x, black)
                vector_y = vector_y - 1
                sense.set_pixel(vector_y, vector_x, pink)
            elif pixels1[8 * vector_x + vector_y - 1] == red:
                if has_wooden_bucket_water == 1 and has_wooden_bucket == True and has_wooden_bucket_fire == False:
                    sense.set_pixel(vector_y - 1, vector_x, black)
                    has_wooden_bucket_fire = True
                    has_wooden_bucket_water = 0
                else:
                    animation_lose_level_1()
                    break
            elif pixels1[8 * vector_x + vector_y - 1] == purple:
                animation_win_level_1()
                sleep(2)
                has_flag = True
            else:
                sense.set_pixel(vector_y, vector_x, black)
                vector_y = vector_y - 1
                sense.set_pixel(vector_y, vector_x, pink)
        elif event4.action == "pressed" and event4.direction == "right" and vector_y < 7 and pixels1[8 * vector_x + vector_y + 1] != dimgrey:
            if pixels1[8 * vector_x + vector_y + 1] == gold and vector_y + 2 <= 7 and pixels1[8 * vector_x + vector_y + 2] != dimgrey:
                if pixels1[8 * vector_x + vector_y + 2] == water:
                    sense.set_pixel(vector_y + 1, vector_x, black)
                    sense.set_pixel(vector_y + 2, vector_x, black)
                elif pixels1[8 * vector_x + vector_y + 2] == red:
                    sense.set_pixel(vector_y + 1, vector_x, black)
                elif pixels1[8 * vector_x + vector_y + 2] == gold:
                    continue
                else:
                    sense.set_pixel(vector_y + 1, vector_x, black)
                    sense.set_pixel(vector_y + 2, vector_x, gold)
            elif pixels1[8 * vector_x + vector_y + 1] == gold and (vector_x + 2 > 7 or pixels1[8 * vector_x + vector_y + 2] == dimgrey):
                continue
            elif pixels1[8 * vector_x + vector_y + 1] == water:
                if has_wooden_bucket_water == 0 and has_wooden_bucket == True:
                    has_wooden_bucket_water = 1
                    sense.set_pixel(vector_y + 1, vector_x, black)
                else:
                    animation_lose_level_1()
                    break
            elif pixels1[8 * vector_x + vector_y + 1] == brown:
                has_wooden_bucket = True
                sense.set_pixel(vector_y, vector_x, black)
                vector_y = vector_y + 1
                sense.set_pixel(vector_y, vector_x, pink)
            elif pixels1[8 * vector_x + vector_y + 1] == red:
                if has_wooden_bucket_water == 1 and has_wooden_bucket == True and has_wooden_bucket_fire == False:
                    sense.set_pixel(vector_y + 1, vector_x, black)
                    has_wooden_bucket_fire = True
                    has_wooden_bucket_water = 0
                else:
                    animation_lose_level_1()
                    break
            elif pixels1[8 * vector_x + vector_y + 1] == purple:
                animation_win_level_1()
                sleep(2)
                has_flag = True
            else:
                sense.set_pixel(vector_y, vector_x, black)
                vector_y = vector_y + 1
                sense.set_pixel(vector_y, vector_x, pink)
    afisare_imagine_de_sfarsit_de_nivel_1()
    afisare_imagine_de_sfarsit_de_nivel_2()
    ENTERING_MAIN_MENU()

#Level1()