
#Copyright 2020, feelSpace GmbH.

#Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
# CONTINUOUS VIBRATION USING ARROW KEYBOARD FOR HAND MOVEMENT
#! /usr/bin/env python
# encoding: utf-8
# continuous vibration using arrow

import keyboard
import pyautogui
import pybelt
#import win32api
import time

from connect import interactive_belt_connect, setup_logger

from pybelt.belt_controller import BeltController, BeltConnectionState, BeltControllerDelegate, BeltMode, \
    BeltVibrationPattern, BeltOrientationType, BeltVibrationTimerOption


class Delegate(BeltControllerDelegate):
    # Belt controller delegate
    pass


def main():
    setup_logger()

    # Interactive script to connect the belt
    belt_controller_delegate = Delegate()
    belt_controller = BeltController(belt_controller_delegate)
    interactive_belt_connect(belt_controller)
    if belt_controller.get_connection_state() != BeltConnectionState.CONNECTED:
        print("Connection failed.")
        return 0

    # Change belt mode to APP mode
    belt_controller.set_belt_mode(BeltMode.APP_MODE)

    while belt_controller.get_connection_state() == BeltConnectionState.CONNECTED:
        # print("enter")
        # print("Q to quit.")
        # print("s: Stop vibration.")
        # print("t: Start")
        # print("->: Right.")
        # print("<-: Left.")
        # print("Arrow up: Up.")
        # print("Arrow down: Down.")
        # print("enter")
        # print("Q to quit.")
        # print("0: Stop vibration.")

        while True:
            try:
                if keyboard.is_pressed('s'):
                    print("stop")
                    belt_controller.stop_vibration()
                    time.sleep(0.5)
                    break
                elif keyboard.is_pressed('right'):
                    belt_controller.vibrate_at_angle(120, channel_index=0)
                    print("right")
                    time.sleep(0.5)
                    break
                elif keyboard.is_pressed('left'):
                    belt_controller.vibrate_at_angle(45, channel_index=0)
                    print("left")
                    time.sleep(0.5)
                    break
                elif keyboard.is_pressed('down'):
                    belt_controller.vibrate_at_angle(60, channel_index=0)
                    print("left")
                    break
                elif keyboard.is_pressed('up'):
                    belt_controller.vibrate_at_angle(90, channel_index=0)
                    print("up")
                    time.sleep(0.5)
                    break
                elif keyboard.is_pressed('f'):
                    belt_controller.send_pulse_command(
                        channel_index=0,
                        orientation_type=BeltOrientationType.ANGLE,
                        orientation=90,
                        intensity=None,
                        on_duration_ms=150,
                        pulse_period=500,
                        pulse_iterations=9,
                        series_period=5000,
                        series_iterations=1,
                        timer_option=BeltVibrationTimerOption.RESET_TIMER,
                        exclusive_channel=False,
                        clear_other_channels=False
                    )
                    break
                else:
                    print("enter.")
                    break
            except ValueError:
                if keyboard.is_pressed('p'):
                    belt_controller.disconnect_belt()
                else:
                    #print("enter.")
                    break

    return 0


if __name__ == "__main__":
    main()