"""
File: bouncing_ball.py
Name:Tina Tsai
-------------------------
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 8
DELAY = 30
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True

mouse_click = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global mouse_click
    run = 1
    vy = 0
    window.add(ball, START_X, START_Y)
    onmouseclicked(bouncing)
    # if mouse click not equal to current run don't drop the ball
    while True:
        if mouse_click:
            if run <= 3:
                #check if jump out of window
                while ball.x + SIZE < window.width:
                    while ball.y < window.height:
                        ball.move(VX, vy)
                        vy += GRAVITY
                        pause(DELAY)
                    #bounce up slower and lower
                    vy = -vy * REDUCE
                    while vy < 0:
                        ball.move(VX, vy)
                        vy += GRAVITY
                        pause(DELAY)
                run += 1
                window.remove(ball)
                window.add(ball, START_X, START_Y)
                mouse_click = False
        else:
            pause(DELAY)


def bouncing(mouse):
    global mouse_click
    mouse_click = True


if __name__ == "__main__":
    main()
