"""
As the owner of an online store, you need to fulfill orders everyday. To optimize the packing of each order, you decide to write an algorithm to match boxes and items based on their respective sizes.

You have access to the following two boxes:

- A medium box (identifier: M)

- A large box (identifier: L)

When possible, you should try to fit multiple items in the same box but boxes can only contain one type of product.

This is the list of items you sell along with associated boxes:

- Camera (identifier: Cam): one can fit in a medium box, and up to two can fit in a large box

- Gaming Console (identifier: Game): too big for a medium box, but up to two can fit in a large box

- max of 2 g consoles can fit in 1 box

- Bluetooth speaker (identifier: Blue): one can fit in a large box . max is 1 per large box

Your goal is to design a function that takes a list of items and returns the box & item matches (examples below).

Your solution should work for any number of each item greater than or equal to zero.

Input = [], Output = []

## Input/Output expectations

["Cam"] -> [M: ["Cam"]]

["Cam", "Game"] -> [M: ["Cam"], L: ["Game"]]

["Game", "Blue"] -> [L: ["Game"], L : ["Blue"]]

["Game", "Game", "Blue"] -> [L: ["Game", "Game"], L : ["Blue"]]

["Cam", "Cam", "Game", "Game"] -> [L: ["Cam", "Cam"], L: ["Game", "Game"]]

["Cam", "Cam", "Cam", "Game", "Game", "Game", "Cam", "Blue"] ->

[L: ["Cam", "Cam"], L: ["Cam", "Cam"], L: ["Game", "Game"], L: ["Game"], L: ["Blue"]]

["Cam", "Cam", "Cam", "Game", "Game", "Cam", "Cam", "Blue", "Blue"] -> [L: ["Cam", "Cam"] , L: ["Cam", "Cam"] , M: ["Cam"] , L: ["Game", "Game"] , L: ["Blue"] , L: ["Blue"]]
"""
from typing import List
from functools import partial

def count_item(item, item_name:str)-> int:
    if item == item_name:
        return True

    return False

def fit_item(items:List[str], item_name:str)->List[List[str]]:
    if item_name == 'Cam':
        if len(items)==1:
            return ["M:['Cam']"]
        else:
            large_box:int = int(len(items) / 2)
            medium_box:int = len(items) % 2

            return ["L:['Cam,Cam]"] * large_box + ["M:['Cam']"] * medium_box

    if item_name == 'Game':
        if len(items) == 1:
            return ["L:['Game']"]
        else:
            large_box_full:int = int(len(items) / 2)
            large_box_half:int = len(items) % 2

            return ["L:['Game','Game']"] * large_box_full + ["L:['Game']"] * large_box_half

    if item_name == 'Blue':
        large_box:int = len(items)

        return ["L:['Blue']"] * large_box

def fit_stuff(items, item_name:str):
    # count
    count_item_func = partial(count_item, item_name=item_name)
    items_filter = filter(count_item_func, items) 
    items_filtered = list(items_filter)

    # fit items
    fit_box = fit_item(items_filtered, item_name)

    return fit_box

if __name__ == "__main__":
    test_case = ["Cam", "Cam", "Cam", "Game", "Game", "Cam", "Cam", "Blue", "Blue"]
    count_camera_func = partial(count_item, item_name='Cam')
    count_camera_cnt = filter(count_camera_func, test_case)
    cameras = list(count_camera_cnt)

    assert len(cameras) == 5

    # assert fit_item(cameras,"Cam") == ["L:['Cam,Cam]", "M:['Cam']"]

    # assert fit_stuff(test_case, "Cam") == ["L:['Cam,Cam]", "M:['Cam']"] 

    # assert fit_stuff(test_case, "Game") == ["L:['Game','Game']"]

    # assert fit_stuff(test_case, "Blue") == ["L:['Blue']", "L:['Blue']"]

    boxes:List[str] = fit_stuff(test_case, "Cam") + fit_stuff(test_case, "Game") + fit_stuff(test_case, "Blue")
    print(boxes)
    assert boxes ==  ['L: ["Cam", "Cam"]' , 'L: ["Cam", "Cam"]' , 'M: ["Cam"]' , 'L: ["Game", "Game"]' , 'L: ["Blue"]' , 'L: ["Blue"]']