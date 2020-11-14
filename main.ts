let hand = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    game.addScore(1)
    basic.pause(100)
    basic.showString("wins: ")
    basic.showNumber(game.score())
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    hand = randint(0, 3)
    if (hand == 0) {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
    } else if (hand == 1) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    } else {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
    }
    
})
