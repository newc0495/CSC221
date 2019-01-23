# -*- coding: utf-8 -*-
"""
CSC 221
M1LAB
Christian New
01/23/19
"""

def main():
    """
    Bottles of beer song
    """
    # 1 use a var
    bottles = 99
    while bottles > 0:
        print(bottles, "bottles of beer on the wall")
        print(bottles, "bottles of beer")
        print("take one down, pass it around")
        bottles = bottles - 1
        print(bottles, "bottles of beer on the wall")
        
    # 2 use a for loop
    # range (start, stop, step)
#    for beer in range(99,-1,-1):
#        print(beer, "beers")
    
#    bottles = 99
#    wall = range(bottles)
#    for beer in wall:
#        print(99 - beer, "bottles of beer on the wall")
        
if __name__ == "__main__":
    main()