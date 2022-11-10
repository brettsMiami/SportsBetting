from scipy.stats import poisson

class Bet(object):

    def __init__(self, stat,average,odds,amount,over_or_under):
        self.stat = float(stat)
        self.average = float(average)
        self.odds = int(odds)
        self.amount = float(amount)
        self.over_or_under = over_or_under

    def get_book_prob(self,odds):
        odds = 100/(self.odds + 100)
        return odds

    # Prob of greater than or equal
    def get_goe_prob(self,stat,average):
        real = 1 - poisson.cdf(k = self.stat, mu = self.average)
        return real
    # Prob of less than or equal
    def get_loe_prob(self,stat,average):
        real = poisson.cdf(k = self.stat, mu = self.average)
        win = real
        return win
    def amount_won(self, amount,odds):
        decimal = float((odds/100) + 1)
        won = amount * decimal
        profit = amount * (decimal - 1)
        integer = int(profit)
        return integer

bet = Bet(stat= input('Whats the stat'),average= input('Whats the average'),odds=input('What are the odds'),amount=input('Whats the amount'), over_or_under= input("Over or Under"))
if bet.over_or_under == "over":
    really = bet.get_goe_prob(stat= bet.stat,average= bet.average)
else:
    really = bet.get_loe_prob(stat= bet.stat,average= bet.average)
book = bet.get_book_prob(odds= bet.odds)
won1 = bet.amount_won(bet.amount, odds= bet.odds)
ev = (won1 * really) + (1-really) *(-bet.amount)
print("Expected Value is %f $ " % ev)
print("Probability of winning",really * 100)






