import motor


class MotorsAction:
    def __init__(self):
        pass

    Left = 0
    Right = 1
    Reverse = 2
    Forward = 3
    RotateRight = 4
    RotateLeft = 5
    Stop = 6
    Clear = 7


def motoractionname(action):
    if (action == MotorsAction.Left):
        return "Left"
    if (action == MotorsAction.Right):
        return "Right"
    if (action == MotorsAction.Reverse):
        return "Reverse"
    if (action == MotorsAction.Forward):
        return "Forward"
    if (action == MotorsAction.RotateRight):
        return "RotateRight"
    if (action == MotorsAction.RotateLeft):
        return "RotateLeft"
    if (action == MotorsAction.Stop):
        return "Stop"
    if (action == MotorsAction.Clear):
        return "Clear"


def movement(action):
    print "MotorAction ",motoractionname(action)
    if action == MotorsAction.Left:
        moveleft()
    if action == MotorsAction.Right:
        moveright()
    if action == MotorsAction.Reverse:
        movereverse()
    if action == MotorsAction.Forward:
        moveforward()
    if action == MotorsAction.RotateRight:
        moverotateright()
    if action == MotorsAction.RotateLeft:
        moverotateleft()
    if action == MotorsAction.Stop:
        movestop()
    if action == MotorsAction.Clear:
        moveclear()


def moveleft():
    motor.action(motor.MotorLocation.Left, motor.MotorMovement.Stop)
    motor.action(motor.MotorLocation.Right, motor.MotorMovement.Forward)


def moverotateleft():
    motor.action(motor.MotorLocation.Left, motor.MotorMovement.Reverse)
    motor.action(motor.MotorLocation.Right, motor.MotorMovement.Forward)


def moveright():
    motor.action(motor.MotorLocation.Left, motor.MotorMovement.Forward)
    motor.action(motor.MotorLocation.Right, motor.MotorMovement.Stop)


def moverotateright():
    motor.action(motor.MotorLocation.Left, motor.MotorMovement.Forward)
    motor.action(motor.MotorLocation.Right, motor.MotorMovement.Reverse)


def movereverse():
    motor.action(motor.MotorLocation.Left, motor.MotorMovement.Reverse)
    motor.action(motor.MotorLocation.Right, motor.MotorMovement.Reverse)


def moveforward():
    motor.action(motor.MotorLocation.Left, motor.MotorMovement.Forward)
    motor.action(motor.MotorLocation.Right, motor.MotorMovement.Forward)


def movestop():
    motor.action(motor.MotorLocation.Left, motor.MotorMovement.Stop)
    motor.action(motor.MotorLocation.Right, motor.MotorMovement.Stop)


def moveclear():
    motor.action(motor.MotorLocation.Left, motor.MotorMovement.Clear)
    motor.action(motor.MotorLocation.Right, motor.MotorMovement.Clear)


if __name__ == '__main__':
    movement(MotorsAction.Left)
    movement(MotorsAction.Right)
    movement(MotorsAction.Reverse)
    movement(MotorsAction.Forward)
    movement(MotorsAction.RotateRight)
    movement(MotorsAction.RotateLeft)
    movement(MotorsAction.Stop)
    movement(MotorsAction.Clear)