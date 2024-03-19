import random
from owner import Owner
from game import Game

a = Owner("test1.csv")
b = Owner("test2.csv")
c = Owner("test3.csv")
d = Owner("test4.csv")

g = Game([a, b, c, d])
g.print_max_bids()
g.print_team_order()
g.run_game()