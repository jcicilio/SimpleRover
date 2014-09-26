import RPi.GPIO as GPIO
#import FakeRpi as GPIO


class MotorLocation:
    def __init__(self):
        pass

    Left = 0
    Right = 1


class MotorMovement:
    def __init__(self):
        pass

    Forward = 0
    Reverse = 1
    Stop = 2
    Clear = 3


def motorlocationname(location):
    if location == MotorLocation.Left:
        return "Left"
    if location == MotorLocation.Right:
        return "Right"


def motormovementname(movement):
    if movement == MotorMovement.Forward:
        return "Forward"
    if movement == MotorMovement.Reverse:
        return "Reverse"
    if movement == MotorMovement.Stop:
        return "Stop"
    if movement == MotorMovement.Clear:
        return "Clear"


class MotorPins:
    EnL = 4
    IAL = 17
    IBL = 18
    EnR = 21
    IAR = 22
    IBR = 23


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MotorPins.EnL, GPIO.OUT)
    GPIO.setup(MotorPins.IAL, GPIO.OUT)
    GPIO.setup(MotorPins.IBL, GPIO.OUT)
    GPIO.setup(MotorPins.EnR, GPIO.OUT)
    GPIO.setup(MotorPins.IAR, GPIO.OUT)
    GPIO.setup(MotorPins.IBR, GPIO.OUT)


def action(location, movement):
    setup()
    # Spec Sheet: https://www.bananarobotics.com/shop/How-to-use-the-L298N-Dual-H-Bridge-Motor-Driver
    print "MotorLocation ", motorlocationname(location), " MotorMovement", motormovementname(movement)

    # Choose Raspberry Pi pins
    if MotorLocation.Left == location:
        pinEN = MotorPins.EnL
        pinIA = MotorPins.IAL
        pinIB = MotorPins.IBL
    else:
        pinEN = MotorPins.EnR
        pinIA = MotorPins.IAR
        pinIB = MotorPins.IBR

    if MotorMovement.Forward == movement:
        GPIO.output(pinEN, GPIO.HIGH)
        GPIO.output(pinIA, GPIO.HIGH)
        GPIO.output(pinIB, GPIO.LOW)

    if MotorMovement.Reverse == movement:
        GPIO.output(pinEN, GPIO.HIGH)
        GPIO.output(pinIA, GPIO.LOW)
        GPIO.output(pinIB, GPIO.HIGH)

    if MotorMovement.Stop == movement:
        GPIO.output(pinEN, GPIO.LOW)
        GPIO.output(pinIA, GPIO.HIGH)
        GPIO.output(pinIB, GPIO.HIGH)

    if MotorMovement.Clear == movement:
        GPIO.output(pinEN, GPIO.LOW)
        GPIO.output(pinIA, GPIO.LOW)
        GPIO.output(pinIB, GPIO.LOW)


# Unit Testing
if __name__ == '__main__':
    action(MotorLocation.Left, MotorMovement.Forward)
    action(MotorLocation.Left, MotorMovement.Reverse)
    action(MotorLocation.Left, MotorMovement.Stop)
    action(MotorLocation.Left, MotorMovement.Clear)

    action(MotorLocation.Right, MotorMovement.Forward)
    action(MotorLocation.Right, MotorMovement.Reverse)
    action(MotorLocation.Right, MotorMovement.Stop)
    action(MotorLocation.Right, MotorMovement.Clear)
