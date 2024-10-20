import time
import turtle


def draw_rectangle(height, width, color):
    turtle.begin_fill()
    turtle.color(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_barbell_2(size, color):
    turtle.penup()
    turtle.sety(-size)
    turtle.pendown()
    draw_rectangle(size * 2, 10, color)


def draw_barbell(weight, weights_list):
    turtle.bgcolor("white")
    turtle.speed(3)
    turtle.color("black")
    turtle.penup()
    turtle.goto(-250, 0)
    turtle.pendown()
    turtle.goto(260, 0)
    turtle.penup()
    # weight - the weight of the barbell to be gained
    # total_weight - weight on the barbell
    # weight_value - current weight of barbell plate from the list
    # value - current value of the list
    total_weight = 0
    offset = 0
    counter = 0
    first_time = 1
    for weight_value, color, amount, size in weights_list:
        first_time += 1
        for i in range(amount):
            if total_weight + weight_value * 2 <= weight:
                weight_value, color, amount, size = weights_list[counter][0], weights_list[counter][1], \
                                                    weights_list[counter][
                                                        2], weights_list[counter][3]
                turtle.penup()
                turtle.goto(-210 - (offset * 2), 0)
                draw_barbell_2(size, color)
                turtle.penup()
                turtle.goto(210 + (offset * 2), 0)
                draw_barbell_2(size, color)
                total_weight += weight_value * 2
                offset += 7
                amount -= 1
            else:
                continue
        if first_time > 1:
            counter += 1

    turtle.hideturtle()
    turtle.done()


def main():
    weight = turtle.numinput('', "Enter the weight of the barbell: ")
    if weight > 545 or weight < 20:
        pen = turtle.getpen()
        pen.write("It's impossible to assemble a barbell like that")
        time.sleep(2)
        pen.clear()
        main()
    else:
        weights_list = [
            (50, "red", 6, 50),
            (25, "green", 4, 50),
            (20, "blue", 4, 40),
            (10, "#E6E600", 4, 35),  # yellow
            (5, "black", 4, 30),
            (1, "black", 4, 25),
            (0.5, "black", 2, 20),
        ]

        draw_barbell(weight, weights_list)


if __name__ == "__main__":
    main()
