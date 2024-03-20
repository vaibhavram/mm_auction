import random
from owner import Owner
from game import Game

a = Owner("vaibhav.csv")
b = Owner("aggressive.csv")
c = Owner("aggrounderdog.csv")
d = Owner("close.csv")
e = Owner("reallyaggro.csv")
f = Owner("underdog.csv")

g = Game([a, b, c, d, e, f])
g.print_max_bids()
g.print_team_order()
g.run_game()