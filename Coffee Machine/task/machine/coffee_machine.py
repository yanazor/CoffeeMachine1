class CoffeeMachine:
    power = 'off'

    def __init__(self, money, beans, milk, water, cups):
        self.money = money
        self.beans = beans
        self.milk = milk
        self.water = water
        self.cups = cups

    def buy(self):
        coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        if coffee == '1':
            if (self.water >= 250) & (self.beans >= 16) & (self.cups >= 1):
                self.money += 4
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                print('I have enough resources, making you a coffee!')
            elif self.water < 250:
                print('Sorry, not enough water!')
            elif self.beans < 16:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
        elif coffee == '2':
            if (self.water >= 350) & (self.beans >= 20) & (self.milk >= 75) & (self.cups >= 1):
                self.money += 7
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                print('I have enough resources, making you a coffee!')
            elif self.water < 350:
                print('Sorry, not enough water!')
            elif self.beans < 20:
                print('Sorry, not enough coffee beans!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
        elif coffee == '3':
            if (self.water >= 200) & (self.beans >= 12) & (self.milk >= 100) & (self.cups >= 1):
                self.money += 6
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                print('I have enough resources, making you a coffee!')
            elif self.water < 200:
                print('Sorry, not enough water!')
            elif self.beans < 12:
                print('Sorry, not enough coffee beans!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
        elif coffee == 'back':
            pass

    def fill(self):
        self.water += int(input('Write how many ml of water you want to add:'))
        self.milk += int(input('Write how many ml of milk you want to add:'))
        self.beans += int(input('Write how many grams of coffee beans you want to add:'))
        self.cups += int(input('Write how many disposable coffee cups you want to add:'))

    def take(self):
        print('I gave you ${}\n'.format(self.money))
        self.money = 0

    def remaining(self):
        print('The coffee machine has:\n{0}{1}{2}{3}{4}'.format('{} of water\n'.format(self.water),
                                                                '{} of milk\n'.format(self.milk),
                                                                '{} of coffee beans\n'.format(self.beans),
                                                                '{} of disposable cups\n'.format(self.cups),
                                                                '{} of money\n'.format(self.money)))

    def machine_working(self):
        power = 'on'
        while power != 'off':
            action = input('Write action (buy, fill, take, remaining, exit):')
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.remaining()
            elif action == 'exit':
                power = 'off'


cof = CoffeeMachine(550, 120, 540, 400, 9)
cof.machine_working()
