import random
class Owner:

    def __init__(self, filename):
        self.name = filename.split(".")[0].capitalize()
        self.budget = 50

        self.bids = {}
        f = open(filename, mode = "r", encoding='utf-8-sig')
        for line in f.readlines():
            bid = line.split(",")
            self.bids[bid[0]] = float(bid[1])

        self.teams = []

        f.close()

    def get_name(self):
        return(self.name)

    def get_budget(self):
        return(self.budget)

    def get_teams(self):
        return(self.bids.keys())

    def get_bid(self, team):
        return self.bids[team]

    def get_most_wanted_remaining_team(self, remaining_teams):
        winning_bid = 0
        # print(remaining_teams)
        for team in remaining_teams:
            if self.bids[team] > winning_bid:
                winning_bid = self.bids[team]
                winning_team = team
            elif self.bids[team] == winning_bid:
                if random.random() > 0.5:
                    winning_bid = self.bids[team]
                    winning_team = team
        return(winning_team)

    def allocate_team(self, team, cost, file):
        print(self.name + " gets " + team + f" for ${cost:.2f}")
        self.teams.append(team)
        file.write(team + "," + self.name + "," + str(cost) + "\n")

    def get_allocated_teams(self):
        return(self.teams)

    def bill_budget(self, amount):
        # print("budget: " + str(self.budget))
        # print("amount: " + str(amount))
        self.budget = self.budget - amount
        self.budget = round(self.budget, 2)
        assert self.budget >= 0