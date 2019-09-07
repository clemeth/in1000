from ezgraphics import GraphicsWindow

win = GraphicsWindow()

canvas = win.canvas()

# ansikt
canvas.setColor("yellow")
canvas.drawOval(50, 50, 100, 100)

# venstre øye
canvas.setColor("blue")
canvas.drawOval(65, 70, 10, 15)

# høyre øye
canvas.drawOval(115, 70, 10, 15)

# glad munn
canvas.setColor("yellow")
canvas.drawArc(65, 95, 70, 0, 180)

canvas.setColor("red")
canvas.drawArc(65, 65, 70, 180, 180)

## trist munn
#canvas.setColor("yellow")
#canvas.drawArc(65, 65, 70, 180, 180)
#
#canvas.setColor("red")
#canvas.drawArc(65, 95, 70, 0, 180)

# vent
win.wait()
