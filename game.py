import random
class Game:

    def __init__(self, players):
        self.players = players
        self.num_players = len(players)
        self.max_bids = {}
        for team in players[0].get_teams():
            self.max_bids[team] = players[0].get_bid(team)
            for player in players[1:]:
                if player.get_bid(team) > self.max_bids[team]:
                    self.max_bids[team] = player.get_bid(team)

        self.team_order = {k: v for k, v in sorted(self.max_bids.items(), key=lambda item: item[1], reverse = True)}.keys()

    def print_max_bids(self):
        print(self.max_bids)

    def print_team_order(self):
        print(self.team_order)

    # # TODO make sure this gets random person when two players have same budget
    # def get_richest_player(self):
    #     budgets = [player.get_budget() for player in self.players]
    #     max_budget = max(budgets)
    #     max_budget_index = budgets.index(max_budget)
    #     return(self.players[max_budget_index], sorted(budgets)[-2] + 0.01)

    def print_budgets(self):
        s = "| "
        for player in self.players:
            s += player.get_name()
            s += ": "
            s += f": ${player.get_budget():.2f}"
            s += " | "
        print(s)

    def run_game(self):
        # go through all teams in order of descending max bid
        for team in self.team_order:
            bids = [player.get_bid(team) for player in self.players]
            adj_bids = [bids[i] if bids[i] <= self.players[i].get_budget() else self.players[i].get_budget() for i in range(self.num_players)]
            cost = sorted(adj_bids)[-2] + 0.01

            # initialize calculation for owner who wins this team
            winning_bid = 0
            # winning_index = -1

            # iterate through every player and assign team to winning player
            for i in range(self.num_players):
                # print("evaluating player " + str(i))
                # print("winning_index: " + str(winning_index))

                print(self.players[i].get_name() + f" Bid: ${bids[i]:.2f} (${adj_bids[i]:.2f})")

                # if the player cannot afford the cost, they cannot get the team
                # if self.players[i].get_budget() < cost:
                #     continue
                
                # if player's bid is the running max, assign the team to them
                if adj_bids[i] > winning_bid:
                    winning_bid = adj_bids[i]
                    winning_index = i

                # else if player's bid is equal to current winning bid, give 
                # them the team if they have higher remaining budget
                # or if they win a coin toss
                elif adj_bids[i] == winning_bid:
                    if self.players[i].get_budget() > self.players[winning_index].get_budget():
                        winning_bid = adj_bids[i]
                        winning_index = i
                    elif self.players[i].get_budget() == self.players[winning_index].get_budget():
                        if random.random() > 0.5:
                            winning_bid = adj_bids[i]
                            winning_index = i

            # if winning_index == -1:
            #     winning_player, cost = self.get_richest_player()
            # else:

            winning_player = self.players[winning_index]

            winning_player.allocate_team(team)
            winning_player.bill_budget(cost)

            print(winning_player.get_name() + " gets " + team + f" for ${cost:.2f}")
            self.print_budgets()
            print("---------------")















