let lamp = 0
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
    	
    } else if (input.buttonIsPressed(Button.B)) {
    	
    } else {
        basic.clearScreen()
    }
    basic.pause(200)
    if (lamp != 0) {
        pins.digitalWritePin(DigitalPin.P12, 1)
        pins.digitalWritePin(DigitalPin.P8, 0)
        lamp = 0
    } else {
        pins.digitalWritePin(DigitalPin.P12, 0)
        pins.digitalWritePin(DigitalPin.P8, 1)
        lamp = 1
    }
})
