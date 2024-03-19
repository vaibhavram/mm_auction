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

    def get_name(self):
        return(self.name)

    def get_budget(self):
        return(self.budget)

    def get_teams(self):
        return(self.bids.keys())

    def get_bid(self, team):
        return self.bids[team]

    def allocate_team(self, team):
        self.teams.append(team)

    def bill_budget(self, amount):
        self.budget = self.budget - amount
        assert self.budget >= 0