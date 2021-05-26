pay = input('Enter your pay:')
dependants = input('How many people do you need to insure?')


def calc_taxes(num):
    return pay * .07


def calc_insurance(dependants):
    return dependants * 30


def calc_401k(num):
    return pay * .05


def calc_net(pay, dependants):
    taxes = calc_taxes(pay)
    insurance = calc_insurance(dependants)
    retirement = calc_401k(pay)
    return pay - taxes - insurance - retirement


print(calc_net(pay, dependants))
