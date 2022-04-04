from constants import *

def pos_to_coord(pos, left, up, box_x, box_y, columns, rows):
    if pos < 0: return None
    i = pos % columns
    j = pos // columns
    x = left + i * box_x
    y = up + j * box_y
    return (x, y)

def int2(number, mode):
    modes = ('dec', 'hex', 'bin', 'octo', 'ascii')
    if mode not in modes:
        print(mode + ' is not in modes(' + str(modes) + ')')
        return
    if mode == 'ascii':
        return chr(number)
    if mode == 'hex':
        val = str(hex(number))[2:].upper()
        if len(val) == 1:
            val = '0' + val
        return val

def count_depth(string, character_to_check=' ') -> int:
    depth = 0
    size_to_check = len(character_to_check)
    for i in range(0, len(string), size_to_check):
        section_to_check = string[i:i+size_to_check]
        if section_to_check == character_to_check:
            depth += 1
        else:
            break
    if depth == 0:
        return (0, string)
    return (depth, string[depth * size_to_check:])