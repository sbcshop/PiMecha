#! /usr/bin/python3

'''
This file contains Joystick example code for controlling PiMecha
Developed by - SB Components
http://sb-components.co.uk
'''

import os
import re
import pprint
import pygame
import pimecha

class Joystick_Controller(object):
    """ Joystick controller class """

    controller = None
    button_data = None
    command_data = []

    def init(self):
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

        # Write your code path
        file = open('/home/pi/PiMecha/Example Codes/code 1.txt', 'r')

        for line in file:
            self.command_data.append(line.strip())

    def listen(self):
        """Listen for events to happen"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    print(str(event.button) + '- Key Pressed')

                    raw_Data = self.command_data[event.button]
                    raw_Data = raw_Data.split('  ')
                    delay = raw_Data[-1].split(':')
                    delay = int(delay[1])/1000

                    for value in range(0, 17):
                        cmd_Data = re.findall('\d+', raw_Data[value])
                        robot.servoWrite(int(cmd_Data[0]), int(cmd_Data[1]), int(cmd_Data[2]))

                if event.type == pygame.JOYHATMOTION:
                    # You can program these keys as per your need
                    #print(event.value)
                    print('Keys not configured..!')


if __name__ == "__main__":
    robot = pimecha.PiMecha()

    # write your serial comm
    robot.connect("/dev/ttyS0")
    
    joystick = Joystick_Controller()
    joystick.init()
    joystick.listen()
