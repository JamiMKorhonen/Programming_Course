import math
import svgwrite

dwg = svgwrite.Drawing()


def draw_hexagon():
    print("Insert hexagon details:")
    cx = float(input("Middle point X: "))
    cy = float(input("Middle point Y: "))
    a = float(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    R = a / math.cos(math.radians(30))

    points = []
    start_angle = -30
    for i in range(6):
        angle_deg = start_angle - (i * 60)
        angle_rad = math.radians(angle_deg)
        x = cx + R * math.cos(angle_rad)
        y = cy + R * math.sin(angle_rad)
        points.append((round(x), round(y)))

    hexagon = dwg.polygon(points=points, fill=fill, stroke=stroke)
    dwg.add(hexagon)


def save_svg():
    filename = input("Insert filename: ")
    print(f"Saving file to \"{filename}\"")
    confirm = input("Proceed (y/n)?: ")
    if confirm.lower() == "y":
        dwg.saveas(filename)
        print("Vector saved successfully!\n")


def draw_square(drawing):
    pass


def draw_circle(drawing):
    pass