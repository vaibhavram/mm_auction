class Owner:

    def __init__(self, filename):
        self.name = filename.split(".")[0].capitalize()

        self.bids = {}
        f = open(filename, mode = "r", encoding='utf-8-sig')
        for line in f.readlines():
            bid = line.split(",")
            self.bids[bid[0]] = float(bid[1])

    def print_bids(self):
        print(self.bids)