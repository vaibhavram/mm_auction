import random
from owner import Owner
from game import Game

a = Owner("vaibhav.csv")
b = Owner("lanard.csv")
c = Owner("rich.csv")
d = Owner("Rahul.csv")
e = Owner("key.csv")
f = Owner("akash.csv")

g = Game([a, b, c, d, e, f])
g.print_max_bids()
g.print_team_order()
g.run_game()