import turtle

SCALE = 3

def setup_screen(world):
    s = turtle.Screen()
    s.title("Misja Lazika")
    s.bgcolor("black")
    ws = world.size * SCALE + 50
    s.setup(width=800, height=800)
    s.setworldcoordinates(-ws, -ws, ws, ws)
    return s

def get_pen(color, size):
    p = turtle.Turtle()
    p.speed(0)
    p.color(color)
    p.pensize(size)
    p.hideturtle()
    return p

def draw_borders(pen, world):
    limit = world.size * SCALE
    pen.penup()
    pen.goto(-limit, -limit)
    pen.pendown()
    for _ in range(4):
        pen.forward(limit * 2)
        pen.left(90)

def draw_items(world):
    p = get_pen("gray", 1)
    for rx, ry in world.rocks:
        p.penup()
        p.goto(rx * SCALE, ry * SCALE)
        p.dot(10, "gray")
    for sx, sy in world.solar_stations:
        p.penup()
        p.goto(sx * SCALE, sy * SCALE)
        p.dot(12, "yellow")
    for cx, cy in world.craters:
        p.penup()
        p.goto(cx * SCALE, cy * SCALE)
        p.dot(14, "brown")

def draw_mission(pojazd, world):
    screen = setup_screen(world)
    border_pen = get_pen("white", 2)
    path_pen = get_pen("cyan", 2)
    point_pen = get_pen("white", 1)

    draw_borders(border_pen, world)
    draw_items(world)

    # Cel
    point_pen.penup()
    point_pen.goto(world.goal_x * SCALE, world.goal_y * SCALE)
    point_pen.dot(15, "green")
    
    # Start
    if pojazd.path:
        sx, sy = pojazd.path[0]
        point_pen.goto(sx * SCALE, sy * SCALE)
        point_pen.dot(12, "blue")

    # Sciezka
    if len(pojazd.path) > 0:
        path_pen.penup()
        path_pen.goto(pojazd.path[0][0] * SCALE, pojazd.path[0][1] * SCALE)
        path_pen.pendown()
        for x, y in pojazd.path:
            path_pen.goto(x * SCALE, y * SCALE)

    # Koniec
    point_pen.goto(pojazd.x * SCALE, pojazd.y * SCALE)
    if pojazd.mission_success:
        point_pen.dot(16, "gold")
    else:
        point_pen.dot(16, "red")

    turtle.done()
