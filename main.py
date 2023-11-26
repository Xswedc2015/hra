def on_button_pressed_a():
    global X, Y
    led.unplot(X, Y)
    if smer == 0:
        X += -1
    else:
        Y += -1
    led.plot(X, Y)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_touched():
    global smer
    if smer == 0:
        smer = 1
    else:
        smer = 0
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_button_pressed_b():
    global X, Y
    if smer == 0:
        X += 1
    else:
        Y += 1
    led.plot(X, Y)
    led.unplot(X, Y)
input.on_button_pressed(Button.B, on_button_pressed_b)

smer = 0
Y = 0
X = 0
jas = 500
X = 2
Y = 2
smer = 0
XX = randint(0, 4)
YY = randint(0, 4)
led.plot(X, Y)
led.plot_brightness(XX, YY + 0, jas)

def on_forever():
    global X, Y, XX, YY, smer
    if X > 4:
        led.unplot(X, Y)
        X = 0
        led.plot(X, Y)
    if X < 0:
        led.unplot(X, Y)
        X = 4
        led.plot(X, Y)
    if Y > 4:
        led.unplot(X, Y)
        Y = 0
        led.plot(X, Y)
    if Y < 0:
        led.unplot(X, Y)
        Y = 4
        led.plot(X, Y)
    if XX == X and YY == Y:
        led.unplot(XX, YY)
        XX = randint(0, 4)
        YY = randint(0, 4)
        led.plot_brightness(XX, YY + 0, jas)
        music.play(music.create_sound_expression(WaveShape.SINE,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
        X = randint(0, 4)
        Y = randint(0, 4)
        smer = 0
        led.plot(X, Y)
basic.forever(on_forever)
