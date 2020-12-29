#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sPycialist - Specialist PC Emulator
# (C) Stanislav Yudin (CityAceE)
# http://zx-pk.ru
#
# ver.0.5, 20th January 2019

import pygame
import pygame.surfarray
import numpy as np

import i8080 as cpu
import spyc_loader
import spyc_keyboard

GAME = 'zoo.rks'
ROM = 'system.rom'
SHOW_FPS = True
CPU_CLOCK = 2  # In MHz. Default Intel 8080 frequency is 2 MHz

spyc_loader.rom(ROM, 0xc000)
cpu.sp = 0x7FFF
cpu.pc = spyc_loader.game(GAME)

debug = False
running = True
int_ticks = int(CPU_CLOCK * 1000000 / 50)
screen_w = 384
screen_h = 256
screen = pygame.display.set_mode((screen_w, screen_h), flags=pygame.RESIZABLE, depth=8)
caption = "sPycialist"
pygame.display.set_caption(caption)


def blitsurface():
    mem = np.reshape(cpu.memory[0x9000:0xc000], (256, 48), 'F')
    bits = np.unpackbits(mem) * 255
    bits = np.reshape(bits, (256, 384)).T
    srf = pygame.surfarray.make_surface(bits)
    screen.blit(srf, (screen_w/2 - 384/2, screen_h/2 - 256/2))

try:
    clock = pygame.time.Clock()
    while running:

        # START OF MAIN LOOP

        # # FOR DEBUGGING
        # if (cpu.pc == 0xc1ff):  # and (cpu.reg_h == 0x3d) and (cpu.reg_l == 0xf8):  # Trap conditions
        #     debug = True
        #     # print('PC:', hex(cpu.pc))
        #     pass
        # if debug:
        #     # blitsurface()
        #     # pygame.display.flip()
        #     cpu.display_regs()  # Set breakpoint here

        cpu.core()
        if cpu.ticks > int_ticks:
            cpu.ticks = 0
            blitsurface()
            pygame.display.flip()
            clock.tick(52)

            # END OF MAIN LOOP

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    spyc_keyboard.keydown(event.key)
                elif event.type == pygame.KEYUP:
                    spyc_keyboard.keyup(event.key)
                elif event.type == pygame.VIDEORESIZE:
                    screen_w, screen_h = event.w, event.h

            if SHOW_FPS:
                fps = clock.get_fps()
                with_fps = "{} - {:.2f} FPS".format(caption, fps)
                pygame.display.set_caption(with_fps)

    pygame.quit()
except SystemExit:
    pygame.quit()
