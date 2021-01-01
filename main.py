def on_logo_pressed():
    music.play_melody("E B C5 A B G A F ", 150)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_leds("""
            . # . # .
            . . . . .
            . . # . .
            # . . . #
            . # # # .
            """)
    elif input.button_is_pressed(Button.B):
        basic.show_icon(IconNames.HEART)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
basic.forever(on_forever)
