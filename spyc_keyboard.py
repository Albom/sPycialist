#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Keyboard emulation (part of sPycialist - Specialist PC Emulator)
# (C) Stanislav Yudin (CityAceE)
# http://zx-pk.ru

import pygame.constants as py_cs


keys = {
  # Key  [   C O L U M N    ] [  R O W  ]
    py_cs.K_F1: [0b1000, 0b00000000, 0b10000000],  # F - F1
    py_cs.K_F2: [0b0100, 0b00000000, 0b10000000],  # HELP - F2
    py_cs.K_F3: [0b0010, 0b00000000, 0b10000000],  # NEW - F3
    py_cs.K_F4: [0b0001, 0b00000000, 0b10000000],  # LOAD - F4
    py_cs.K_F5: [0b0000, 0b10000000, 0b10000000],  # SAVE - F5
    py_cs.K_F6: [0b0000, 0b01000000, 0b10000000],  # RUN - F6
    py_cs.K_F7: [0b0000, 0b00100000, 0b10000000],  # STOP - F7
    py_cs.K_F8: [0b0000, 0b00010000, 0b10000000],  # CONT - F8
    py_cs.K_F9: [0b0000, 0b00001000, 0b10000000],  # EDIT - F9
    py_cs.K_F10: [0b0000, 0b00000100, 0b10000000],  # СФ - F10
    py_cs.K_F11: [0b0000, 0b00000010, 0b10000000],  # ТФ - F11
    py_cs.K_F12: [0b0000, 0b00000001, 0b10000000],  # НФ - F12

    py_cs.K_EQUALS:  [0b1000, 0b00000000, 0b01000000],  # ; + - +
    py_cs.K_1:  [0b0100, 0b00000000, 0b01000000],  # 1 ! - 1
    py_cs.K_2:  [0b0010, 0b00000000, 0b01000000],  # 2 " - 2
    py_cs.K_3:  [0b0001, 0b00000000, 0b01000000],  # 3 # - 3
    py_cs.K_4:  [0b0000, 0b10000000, 0b01000000],  # 4 $ - 4
    py_cs.K_5:  [0b0000, 0b01000000, 0b01000000],  # 5 % - 5
    py_cs.K_6:  [0b0000, 0b00100000, 0b01000000],  # 6 & - 6
    py_cs.K_7:  [0b0000, 0b00010000, 0b01000000],  # 7 ' - 7
    py_cs.K_8:  [0b0000, 0b00001000, 0b01000000],  # 8 ( - 8
    py_cs.K_9:  [0b0000, 0b00000100, 0b01000000],  # 9 ) - 9
    py_cs.K_0:  [0b0000, 0b00000010, 0b01000000],  # 0 - 0
    py_cs.K_MINUS:  [0b0000, 0b00000001, 0b01000000],  # - = - -

    py_cs.K_q: [0b1000, 0b00000000, 0b00100000],  # Й J - Й
    py_cs.K_w: [0b0100, 0b00000000, 0b00100000],  # Ц C - Ц
    py_cs.K_e: [0b0010, 0b00000000, 0b00100000],  # У U - У
    py_cs.K_r: [0b0001, 0b00000000, 0b00100000],  # К K - К
    py_cs.K_t: [0b0000, 0b10000000, 0b00100000],  # Е E - Е
    py_cs.K_y: [0b0000, 0b01000000, 0b00100000],  # Н N - Н
    py_cs.K_u: [0b0000, 0b00100000, 0b00100000],  # Г G - Г
    py_cs.K_i: [0b0000, 0b00010000, 0b00100000],  # Ш [ - Ш
    py_cs.K_o: [0b0000, 0b00001000, 0b00100000],  # Щ ] - Щ
    py_cs.K_p: [0b0000, 0b00000100, 0b00100000],  # З Z - З
    py_cs.K_LEFTBRACKET:  [0b0000, 0b00000010, 0b00100000],  # Х H - H
    py_cs.K_RIGHTBRACKET:  [0b0000, 0b00000001, 0b00100000],  # : * - Ъ

    py_cs.K_a:  [0b1000, 0b00000000, 0b00010000],  # Ф F - Ф
    py_cs.K_s: [0b0100, 0b00000000, 0b00010000],  # Ы Y - Ы
    py_cs.K_d: [0b0010, 0b00000000, 0b00010000],  # В W - В
    py_cs.K_f: [0b0001, 0b00000000, 0b00010000],  # А A - А
    py_cs.K_g: [0b0000, 0b10000000, 0b00010000],  # П P - П
    py_cs.K_h: [0b0000, 0b01000000, 0b00010000],  # Р R - Р
    py_cs.K_j: [0b0000, 0b00100000, 0b00010000],  # О O - О
    py_cs.K_k: [0b0000, 0b00010000, 0b00010000],  # Л L - Л
    py_cs.K_l: [0b0000, 0b00001000, 0b00010000],  # Д D - Д
    py_cs.K_SEMICOLON:  [0b0000, 0b00000100, 0b00010000],  # Ж V - Ж
    py_cs.K_QUOTE:  [0b0000, 0b00000010, 0b00010000],  # Э \ - Э
    py_cs.K_BACKSLASH:  [0b0000, 0b00000001, 0b00010000],  # . > - \

    py_cs.K_z: [0b1000, 0b00000000, 0b00001000],  # Я Q - Я
    py_cs.K_x: [0b0100, 0b00000000, 0b00001000],  # Ч ^ - Ч
    py_cs.K_c:  [0b0010, 0b00000000, 0b00001000],  # С S - С
    py_cs.K_m: [0b0001, 0b00000000, 0b00001000],  # М M - М
    py_cs.K_b:  [0b0000, 0b10000000, 0b00001000],  # И I - И
    py_cs.K_n: [0b0000, 0b01000000, 0b00001000],  # Т T - Т
    py_cs.K_v: [0b0000, 0b00100000, 0b00001000],  # Ь X - Ь
    py_cs.K_COMMA:  [0b0000, 0b00010000, 0b00001000],  # Б B - Б
    py_cs.K_PERIOD:  [0b0000, 0b00001000, 0b00001000],  # Ю @ - Ю
    py_cs.K_SLASH:  [0b0000, 0b00000100, 0b00001000],  # , < - ?
    py_cs.K_RSHIFT:    [0b0000, 0b00000010, 0b00001000],  # / ? - Right Shift
    py_cs.K_BACKSPACE: [0b0000, 0b00000001, 0b00001000],  # ЗБ - Backspace

    py_cs.K_LCTRL:    [0b1000, 0b00000000, 0b00000100],  # НРФ - Left Ctrl
    py_cs.K_HOME:     [0b0100, 0b00000000, 0b00000100],  # HOME - Home
    py_cs.K_UP:       [0b0010, 0b00000000, 0b00000100],  # ВВЕРХ - Up
    py_cs.K_DOWN:     [0b0001, 0b00000000, 0b00000100],  # ВНИЗ - Down
    000:              [0b0000, 0b10000000, 0b00000100],  #
    000:              [0b0000, 0b01000000, 0b00000100],  #
    py_cs.K_SPACE:    [0b0000, 0b00100000, 0b00000100],  # ПРОБЕЛ - Space
    py_cs.K_LEFT:     [0b0000, 0b00010000, 0b00000100],  # ВЛЕВО - Left
    py_cs.K_RALT:     [0b0000, 0b00001000, 0b00000100],  # ПВ - Rigth Alt
    py_cs.K_RIGHT:    [0b0000, 0b00000100, 0b00000100],  # ВПРАВО - Right
    py_cs.K_PAGEDOWN: [0b0000, 0b00000010, 0b00000100],  # ПС - PageDown
    py_cs.K_RETURN:   [0b0000, 0b00000001, 0b00000100],  # ВК - Enter

    py_cs.K_LSHIFT: [0b0000, 0b00000000, 0b00000010]}  # НР - Left Shift

vv55a_mode = 0x82
kb_mem = bytearray([0x00, 0x00, 0x00])
kb_matrix = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 0]


def keydown(code):
    if code in keys:
        i = {2: 6, 4: 5, 8: 4, 16: 3, 32: 2, 64: 1, 128: 0}[keys[code][2]]
        kb_matrix[i][0] |= keys[code][0]
        kb_matrix[i][1] |= keys[code][1]
        kb_matrix[7] |= keys[code][2]


def keyup(code):
    if code in keys:
        i = {2: 6, 4: 5, 8: 4, 16: 3, 32: 2, 64: 1, 128: 0}[keys[code][2]]
        kb_matrix[i][0] &= 0xff - keys[code][0]
        kb_matrix[i][1] &= 0xff - keys[code][1]
        kb_matrix[7] &= 0xff - keys[code][2]


def get_port_91(mem, matrix):
    byte = 0
    mask = 128
    for i in range(7):
        if kb_mem[mem] & mask:
            byte |= kb_matrix[i][matrix]
        mask //= 2
    return 0xff - byte


def get_port_82(mem, matrix):
    byte = 0
    mask = 128
    for i in range(7):
        if kb_mem[mem] & kb_matrix[i][matrix]:
            byte += mask
        mask //= 2
    return byte


def read_kb_ports(addr):
    if vv55a_mode == 0x91:
        if not (addr % 4):
            return get_port_91(1, 1)
        elif addr % 4 == 1:
            return 0xff - kb_mem[1]
        elif addr % 4 == 2:
            return get_port_91(1, 0) % 0x10
    elif vv55a_mode == 0x82:
        if not (addr % 4):
            return 0xff - kb_mem[0]
        elif addr % 4 == 1:
            byte = get_port_82(0, 1)
            byte |= get_port_82(2, 0)
            return 0xff - byte - (kb_matrix[7] & 2)
        elif addr % 4 == 2:
            return 0xff - kb_mem[2]


def write_kb_ports(addr, byte):
    global vv55a_mode
    if addr % 4 != 3:
        kb_mem[(addr % 4)] = 0xff - byte
    elif byte == 0x91:
        vv55a_mode = byte
        kb_mem[1] = 0xff
    elif byte == 0x82:
        vv55a_mode = byte
        kb_mem[0] = 0xff
        kb_mem[2] = 0xff
