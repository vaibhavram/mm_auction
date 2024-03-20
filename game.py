import random
import time
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

        self.team_order = list({k: v for k, v in sorted(self.max_bids.items(), key=lambda item: item[1], reverse = True)}.keys())

    def print_max_bids(self):
        print(self.max_bids)

    def print_team_order(self):
        print(self.team_order)

    def print_budgets(self):
        s = "| "
        for player in self.players:
            s += player.get_name()
            s += ": "
            s += f": ${player.get_budget():.2f}"
            s += " | "
        print(s)

    def run_game(self):
        # open results file to write team allocations to
        results = open("results.csv", "w")

        num_teams = len(self.team_order)

        # go through all teams in order of descending max bid
        # until all but one person have budget
        t = 0
        exhausted = False
        while not exhausted:
            team = self.team_order[t]
            print(str(t + 1) + " of " + str(num_teams) + ": " + team.upper())
            bids = [player.get_bid(team) for player in self.players]
            # effective bid for each player is their bid if it is below remaining budget,
            # else it is their budget
            adj_bids = [bids[k] if bids[k] <= self.players[k].get_budget() else self.players[k].get_budget() for k in range(self.num_players)]
            # cost = sorted(adj_bids)[-2] + 0.01
            cost = sorted(adj_bids)[-2]

            # initialize calculation for owner who wins this team
            winning_bid = 0
            # winning_index = -1

            # iterate through every player and assign team to winning player
            for i in range(self.num_players):

                print(self.players[i].get_name() + f": ${bids[i]:.2f} (${adj_bids[i]:.2f})")
                
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

            winning_player = self.players[winning_index]

            winning_player.allocate_team(team, cost, results)
            winning_player.bill_budget(cost)

            self.print_budgets()
            print("---------------")

            # time.sleep(3)

            # increment to next team
            t += 1

            # check if all but one's budget has been exhausted
            exhausted_budget_counter = 0
            for player in self.players:
                if player.get_budget() == 0:
                    exhausted_budget_counter += 1
            if exhausted_budget_counter == self.num_players - 1:
                exhausted = True

        time.sleep(5)
        print("ENTERING DRAFT")
        # begin draft for remaining teams
        remaining_teams = self.team_order[t:num_teams]
        random.shuffle(self.players)
        # print("t: " + str(t))
        while t < num_teams:
            for player in self.players:
                if len(remaining_teams) > 0:
                    team = player.get_most_wanted_remaining_team(remaining_teams)
                    player.allocate_team(team, 0, results)
                    remaining_teams.remove(team)
                    t += 1

        for player in self.players:
            print(player.get_name())
            print(player.get_allocated_teams())

        results.close()















