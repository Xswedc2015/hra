input.onButtonPressed(Button.A, function () {
    led.unplot(X, Y)
    if (smer == 0) {
        X += -1
    } else {
        Y += -1
    }
    led.plot(X, Y)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    if (smer == 0) {
        smer = 1
    } else {
        smer = 0
    }
})
input.onButtonPressed(Button.B, function () {
    if (smer == 0) {
        X += 1
    } else {
        Y += 1
    }
    led.plot(X, Y)
    led.unplot(X, Y)
})
let smer = 0
let Y = 0
let X = 0
let jas = 500
X = 2
Y = 2
smer = 0
let XX = randint(0, 4)
let YY = randint(0, 4)
led.plot(X, Y)
led.plotBrightness(XX, YY + 0, jas)
basic.forever(function () {
    if (X > 4) {
        led.unplot(X, Y)
        X = 0
        led.plot(X, Y)
    }
    if (X < 0) {
        led.unplot(X, Y)
        X = 4
        led.plot(X, Y)
    }
    if (Y > 4) {
        led.unplot(X, Y)
        Y = 0
        led.plot(X, Y)
    }
    if (Y < 0) {
        led.unplot(X, Y)
        Y = 4
        led.plot(X, Y)
    }
    if (XX == X && YY == Y) {
        basic.clearScreen()
        XX = randint(0, 4)
        YY = randint(0, 4)
        led.plotBrightness(XX, YY + 0, jas)
        music.play(music.createSoundExpression(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        X = randint(0, 4)
        Y = randint(0, 4)
        smer = 0
        led.plot(X, Y)
    }
})
