class Guest:
    def __init__(self, input_name, input_cash):
        self.name = input_name
        self.cash = input_cash

    def can_afford(self, entry_fee):
        if self.cash >= entry_fee:
            return True
        else: 
            return False

    def remove_money(self, entry_fee):
        self.cash -= entry_fee
