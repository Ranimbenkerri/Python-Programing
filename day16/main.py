from turtle import Turtle, Screen
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable
x = PrettyTable()
x.add_column("prof",["Khalfone","Kharbachi","Samiha Ait taleb"])
x.add_column("module",["analyse","algebre","Archi"])
print(x)