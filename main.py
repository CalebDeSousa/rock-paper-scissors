hand = 0

def on_button_pressed_a():
    game.add_score(1)
    basic.pause(100)
    basic.show_string("wins: ")
    basic.show_number(game.score())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global hand
    hand = randint(0, 3)
    if hand == 0:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
    elif hand==1:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    else:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
input.on_gesture(Gesture.SHAKE,on_gesture_shake)