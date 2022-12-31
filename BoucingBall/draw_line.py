"""
File: draw_line.py
Name:Yun Yen Tsai
-------------------------
TODO:
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.

"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow(800,800)
click = 0
start_point = GOval(10,10)

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_dot)



def draw_dot(mouse):
    global click, start_poin
    if click % 2 == 0:
        window.add(start_point,mouse.x-5,mouse.y-5)
        click += 1
    else:
        click += 1
        #draw line in between and remove dots
        start_point_location = window.get_object_at(start_point.x+5,start_point.y+5)
        window.remove(start_point_location)
        line = GLine(start_point.x+5,start_point.y+5,mouse.x+5,mouse.y+5)
        window.add(line)


if __name__ == "__main__":
    main()


