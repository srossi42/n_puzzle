import os
import re
import glob
import time
import random


def chose_algo():
    algo_choice = 0
    available_answers = [1, 2, 3]
    while algo_choice not in available_answers:
        os.system("clear")
        print("Which algorithm do you want to use?")
        print("     1- Astar")
        print("     2- Greedy")
        print("     3- Uniform")
        algo_choice = input("Answer : ")
        if not algo_choice.isdigit() or int(algo_choice) not in available_answers:
            print("Wrong answer, please try again")
            time.sleep(2)
        else:
            algo_choice = int(algo_choice)
    return algo_choice


def chose_heuristic():
    heuristic_choice = 0
    available_answers = [1, 2, 3, 4]
    while heuristic_choice not in available_answers:
        os.system("clear")
        print("Which heuristic function do you want to use?")
        print("     1- Manhattan distance")
        print("     2- Euclidian distance")
        print("     3- Misplaces tiles")
        print("     4- Chebyshev")
        heuristic_choice = input("Answer : ")
        if not heuristic_choice.isdigit() or int(heuristic_choice) not in available_answers:
            print("Wrong answer, please try again")
            time.sleep(2)
        else:
            heuristic_choice = int(heuristic_choice)
    return heuristic_choice


def chose_weight():
    os.system("clear")
    add_weight = 0
    available_answers = [1, 2]
    while add_weight not in available_answers:
        os.system("clear")
        print("Would you like to add some weight to your heuristic?")
        print("     1- Yes")
        print("     2- No")
        add_weight = input("Answer : ")
        if not add_weight.isdigit() or int(add_weight) not in available_answers:
            print("Wrong answer, please try again")
            time.sleep(2)
        else:
            add_weight = int(add_weight)
    os.system("clear")
    weight = (None, 1)[add_weight == 2]
    if weight is None:
        while weight is None or not weight.isdigit():
            os.system("clear")
            weight = input("Please enter weight:")
        os.system("clear")
    return int(weight)


def chose_difficulty(size):
    difficulty = 0
    available_answers = [1, 2, 3, 4]
    while difficulty not in available_answers:
        os.system("clear")
        print("Chose difficulty of the puzzle (" + str(size) + "*" + str(size) + "): ")
        print("     1- Easy")
        print("     2- Normal")
        print("     3- Hard")
        print("     4- Extreme")
        difficulty = input("Answer: ")
        if not difficulty.isdigit() or int(difficulty) not in available_answers:
            print("Wrong answer, please try again")
            time.sleep(2)
        else:
            difficulty = int(difficulty)
    if difficulty == 1:
        difficulty = random.randint(10, 49)
    elif difficulty == 2:
        difficulty = random.randint(50, 149)
    elif difficulty == 3:
        difficulty = random.randint(150, 499)
    elif difficulty == 4:
        difficulty = random.randint(500, 2000)
    return difficulty


def chose_size():
    size = None
    while size is None:
        os.system("clear")
        print("You are going to generate a puzzle.")
        size = input("Please chose your puzzle size (> 1): ")
        if not size.isdigit() or int(size) <= 1:
            print("Wrong answer, please try again")
            size = None
            time.sleep(2)
        else:
            size = int(size)
    return size


def chose_display():
    os.system("clear")
    available_answers = [1, 2]
    visualize = 0
    while visualize not in available_answers:
        os.system("clear")
        print("Would you like to visualize the path to solution?")
        print("     1- Yes")
        print("     2- No")
        visualize = input("Answer : ")
        if not visualize.isdigit() or int(visualize) not in available_answers:
            print("Wrong answer, please try again")
            time.sleep(2)
        else:
            visualize = int(visualize)
    os.system("clear")
    display_mode = (0, None)[visualize == 1]
    available_answers = [1, 2, 3]
    if display_mode is None:
        while display_mode is None or not str(display_mode).isdigit():
            os.system("clear")
            print("Which visualize mode would you like to use?")
            print("     1- Default")
            print("     2- Puzzle (image)")
            print("     3- Special (image)")
            display_mode = input("Answer : ")
            if not display_mode.isdigit() or int(display_mode) not in available_answers:
                print("Wrong answer, please try again")
                display_mode = None
                time.sleep(2)
            else:
                display_mode = int(display_mode)
        os.system("clear")
    return display_mode


def chose_img_path():
    img_choice = 0
    images_path = "./images/"
    images_list = glob.glob(images_path + "*.jpg")
    range_max = len(images_list) + 1
    regex = re.compile("./images/(.*).jpg")
    while img_choice not in range(1, range_max):
        os.system("clear")
        print("Which image do you want to use?")
        opt = 1
        for img in images_list:
            img_name = regex.findall(img)[0]
            print("     " + str(opt) + "- " + img_name.title())
            opt += 1
        img_choice = input("Answer : ")
        if not img_choice.isdigit() or int(img_choice) not in range(1, range_max):
            print("Wrong answer, please try again")
            time.sleep(2)
        else:
            img_choice = int(img_choice)
    return images_list[img_choice - 1]