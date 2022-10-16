from time import sleep
import sys

day = 0
season = ''
companies = []

ICE_CREAM_COST = 1

def commafy(number):
    if number == type(float):
        return "{:,.2f}".format(number)
    else:
        return "{:,}".format(number)

def number_of_companies(company_subclass_to_look_for):
    number = 0
    for i in companies:
        if isinstance(i, company_subclass_to_look_for):
            number += 1

    return number

def isfloat(string):
    try:
        # if it's an intager eg. '0', str(float('0')) will be '0.0' which is not the same
        # if it's a string eg. 'hello', a value error will be raised
        # if it's a float eg. '1.5', it will turn into 1.5 then '1.5' again, staying the same
        if str(float(string)) == string:
            return True
        else:
            return False
    except ValueError:
        return False

def isint(string):
    try:
        int(string)
        if '.' not in string:
            return True
        else:
            return False
    except ValueError:
        return False

def isstr(string):
    if not isint(string) and not isfloat(string):
        return True
    return False

def buy_upgrade(company_subclass, upgrade_list, asset_being_upgraded, error_msg, upgraded_var_index_in_upgrade_list):
    price = upgrade_list[upgraded_var_index_in_upgrade_list][2]
    if Company.total_money >= price:
        Company.total_money = round(Company.total_money - price, 2)
        print(f'Successfully bought {upgrade_list[upgraded_var_index_in_upgrade_list][0]}')
        return upgrade_list[upgraded_var_index_in_upgrade_list]
    else:
        print(f'You need £{commafy(price - Company.total_money)} more ' + error_msg)
        return asset_being_upgraded

class Company:
    total_money = 7500 + 7500 + 7500 + 4000
    pointer = None
    
    def __init__(self, name):
        self.name = name
        self.pounds_per_day = 0
        self.valuation = 0
        self.total_money_made = 0


class Ice_cream_stand(Company):
    '''Where a list of the functions shared by all subclasses should be'''
    '''calculate valuation, start screen (top), stat screen (bottom), configure?'''
    
    beaches = [
        ['Polnare Beach', 20, 0],
        ['Duporth Cove', 40, 500],
        ['Porthgwidden Beach', 58, 1500],
        ['Crimdon Cove', 74, 3000],
        ['Bardsea Beach', 88, 5000],
        ['Blackpool Beach', 100, 7500]]
    
    machines = [
        ['CJ Cheapskate', 20, 0],
        ['Kernow Dehen', 45, 2500],
        ['CJ Cheapskate Max', 75, 4500],
        ['Kernow Ren', 110, 6000],
        ['AL Autonomous I', 150, 7000],
        ['AL Autonomous II', 195, 7500]]

    flavours = [
        ['1 flavour', 1, 0],
        ['2 flavours', 1.2, 1500],
        ['4 flavours', 1.4, 3000],
        ['6 flavours', 1.6, 4500],
        ['8 flavours', 1.8, 6000],
        ['10 flavours', 2, 7500]]

    def __init__(self, name):
        super().__init__(name)
        self.beach = Ice_cream_stand.beaches[0]
        self.machine = Ice_cream_stand.machines[0]
        self.flavour = Ice_cream_stand.flavours[0]
        self.price = 0
        self.max_made = self.machine[1]
        self.customers = 0
        self.amount_made = self.machine[1]
        self.employee = False
        self.MIPMs = []
        self.total_ice_creams_sold = 0

    def start_screen(self, new_day):
        Company.pointer = self
        
        if new_day == True:
            show_day()
        else:
            print()
        
        print(f'{self.name} ice cream stand')
        print(f'Total money: £{commafy(round(Company.total_money, 2))}')
        print(f'Profits: £{commafy(round(self.pounds_per_day, 2))}')
        
        valid = False
        while not valid:
            command = input('Enter command: ')
            
            if 'help' in command:
                if command == 'help':
                    print()
                    print('configure')
                    print('upgrade')
                    print('stats')
                    print('back (to company options)')
                    print('employee')
                    #print('Mains Integrated Control System (MICS)') # | Backdoor Bill Control | Integrated Pricing System | Mains Integrated Listing Feature | ControlConditionConsistent Unwanted Costs Keeper | Mains Integreated Limiting System | Mains Integrated Control Mechanism
                    print('Mains Integrated Pricing Mechanism (MIPM)')
                    print('help [command] (for more detailed information)')
                    print('quit')
                    print()
                    
                elif 'configure' in command:
                    print("\n\nThese let you modify the inner workings of your company. Options are:")
                    print("\nPrice per ice cream. The higher your price is, the less people will buy it. If you don't have many customers, be careful for local maxima")
                    print("Number of ice creams made. If you're producing more than you're selling, limit the number produced to minimise costs")
                    print("MIPM. Use this to change the price of your ice creams when it gets to a certain day of the year")
                    self.start_screen(new_day=False)

                elif 'upgrade' in command:
                    print("\nThese are one-off things you can buy to grow your company. Options are:")
                    print("\nBeach. This is the base for calculating how many customers you have, all other numbers revolve around this as each level has the biggest difference")
                    print("Machine. This is the sole predictor for the maximum number of ice creams produced. You can limit this number but can't grow it without this upgrade")
                    print("Flavour. More flavours give you more customers on the beach. At its peak, you can double your maximum customers, vital with the smaller beach upgrades in the late game")
                    self.start_screen(new_day=False)

                elif 'stats' in command:
                    print("\nThis shows you a list of useful information about your company on a given day or all time. Very useful when configuring")
                    self.start_screen(new_day=False)

                elif 'back' in command:
                    print("\nThis shows you a list of all your companies and where you can access general information. This also has a stats screen where you can look at your companies as a whole")
                    self.start_screen(new_day=False)

                elif 'employee' in command:
                    print("\nEmployees let your businsses make money when you aren't there. They cost £70 per day and you can only have one per company but they let you grow and expand")
                    self.start_screen(new_day=False)

                elif 'quit' in command:
                    print("\nExits the game entirely. It's impossible to save the game yet")
                    self.start_screen(new_day=False)

            elif command == 'configure':
                self.configure_screen()

            elif command == 'upgrade':
                self.upgrade_screen()

            elif command == 'stats':
                self.stat_screen()

            elif command == 'back':
                #start_screen()
                raise SystemExit

            elif command == 'employee':
                self.employee_screen()

            elif command == 'quit':
                sys.exit()

            elif command == '':
                self.start_screen(new_day=True)

            else:
                print('That was not a valid command. Use "help" for a list of commands\n')


    def season_effect(self):
        if season == 'Summer':
            return 1
        elif season == 'Autumn':
            return 0.5
        elif season == 'Winter':
            return 0.25
        elif season == 'Spring':
            return 0.5

    def calculate_valuation(self):
        # change name to company_valuation
        # calculate each of the 3 ways to valuate that can apply to the company - asset based, ratio based (P/E ratio, relative valuation), discounted cash flow (DCF, intrinsic)
        # find the mean average
        # badda bing badda boom
        # scratch that, I'm using entry cost from the website https://www.simplybusiness.co.uk/knowledge/articles/2021/08/how-to-value-a-business/

        value = self.beach[2] + self.machine[2] + self.flavour[2]
        value += self.amount_made * ICE_CREAM_COST
        
        mipm_worth = 0
        for i in range(len(self.MIPMs)):
            mipm_worth += 4000 * 1.4 ** i

        value += mipm_worth

        self.valuation = value


    def calculate_amount_made(self):
        self.amount_made = min(self.max_made, self.machine[1])

    def calculate_customers(self):
        customers = self.beach[1] * self.flavour[1] * self.season_effect()
        # the equation of the line linking price with customers
        customer_multiplier = self.price / -4 + 1.2
        if customer_multiplier > 1:
            customer_multiplier = 1
        elif customer_multiplier < 0:
            customer_multiplier = 0
            
        customers = round(customers * customer_multiplier)

        self.customers = customers

    def upgrade_beach(self):
        print() # to improve the GUI
        for i in range(len(Ice_cream_stand.beaches)):
            print(f'{i+1}) Move to {Ice_cream_stand.beaches[i][0]}; {Ice_cream_stand.beaches[i][1]} customers; £{commafy(Ice_cream_stand.beaches[i][2])}')
        print('7) BACK')
        print('8) CANCEL')

        valid = False
        while not valid:
            choice = input('Type number: ')
            
            if choice == '1':
                self.beach = buy_upgrade(Ice_cream_stand, Ice_cream_stand.beaches, self.beach, 'to go there', 0)
                valid = True

            elif choice == '2':
                self.beach = buy_upgrade(Ice_cream_stand, Ice_cream_stand.beaches, self.beach, 'to go there', 1)
                valid = True
            
            elif choice == '3': 
                self.beach = buy_upgrade(Ice_cream_stand, Ice_cream_stand.beaches, self.beach, 'to go there', 2)
                valid = True                                                                                          

            elif choice == '4':
                self.beach = buy_upgrade(Ice_cream_stand, Ice_cream_stand.beaches, self.beach, 'to go there', 3)
                valid = True

            elif choice == '5':
                self.beach = buy_upgrade(Ice_cream_stand, Ice_cream_stand.beaches, self.beach, 'to go there', 4)
                valid = True

            elif choice == '6':
                self.beach = buy_upgrade(Ice_cream_stand, Ice_cream_stand.beaches, self.beach, 'to go there', 5)
                valid = True

            elif choice == '7':
                self.upgrade_screen()

            elif choice == '8':
                self.start_screen(new_day=False)

            elif choice == '':
                self.start_screen(new_day=True)

            else:
                print('That was not a valid number')

        # here to avoid repeating multiple times after the upgrade. Can't go in the function as it has to return self.beach
        self.start_screen(new_day=False)

    def upgrade_machine(self):
        print()
        for i in range(len(Ice_cream_stand.machines)):
            print(f'{i+1}) Buy {Ice_cream_stand.machines[i][0]}; {Ice_cream_stand.machines[i][1]} ice creams per day; £{commafy(Ice_cream_stand.machines[i][2])}')
        print('7) BACK')
        print('8) CANCEL')
        
        valid = False
        while not valid:
            choice = input('Type number: ')
            
            if choice == '1':
                self.machine = buy_upgrade(Ice_cream_stand, Ice_cream_stand.machines, self.machine, 'to buy that', 0)
                valid = True                                                                                                

            elif choice == '2':
                self.machine = buy_upgrade(Ice_cream_stand, Ice_cream_stand.machines, self.machine, 'to buy that', 1)
                valid = True                                                                                                

            elif choice == '3':
                self.machine = buy_upgrade(Ice_cream_stand, Ice_cream_stand.machines, self.machine, 'to buy that', 2)
                valid = True                                                                                                

            elif choice == '4':
                self.machine = buy_upgrade(Ice_cream_stand, Ice_cream_stand.machines, self.machine, 'to buy that', 3)
                valid = True                                                                                                

            elif choice == '5':
                self.machine = buy_upgrade(Ice_cream_stand, Ice_cream_stand.machines, self.machine, 'to buy that', 4)
                valid = True                                                                                                

            elif choice == '6':
                self.machine = buy_upgrade(Ice_cream_stand, Ice_cream_stand.machines, self.machine, 'to buy that', 5)
                valid = True                                                                                                

            elif choice == '7':
                self.upgrade_screen()

            elif choice == '8':
                self.start_screen(new_day=False)

            elif choice == '':
                self.start_screen(new_day=True)

            else:
                print('That was not a valid number')

        # here to avoid repeating multiple times after the upgrade. Can't go in the function as it has to return self.beach
        self.max_made = self.machine[1]
        self.start_screen(new_day=False)

    def upgrade_flavours(self):
        print()
        for i in range(len(Ice_cream_stand.flavours)):
            print(f'{i+1}) Have {Ice_cream_stand.flavours[i][0]}; {int(Ice_cream_stand.flavours[i][1] * 100 - 100)}% more customers per day; £{commafy(Ice_cream_stand.flavours[i][2])}')
        print('7) BACK')
        print('8) CANCEL')

        valid = False
        while not valid:
            choice = input('Type number: ')

            if choice == '1':
                self.flavour = buy_upgrade(Ice_cream_stand, Ice_cream_stand.flavours, self.flavours, 'to buy that', 0)
                valid = True                                                                                                

            elif choice == '2':
                self.flavour = buy_upgrade(Ice_cream_stand, Ice_cream_stand.flavours, self.flavours, 'to buy that', 1)
                valid = True                                                                                                

            elif choice == '3':
                self.flavour = buy_upgrade(Ice_cream_stand, Ice_cream_stand.flavours, self.flavours, 'to buy that', 2)
                valid = True                                                                                                

            elif choice == '4':
                self.flavour = buy_upgrade(Ice_cream_stand, Ice_cream_stand.flavours, self.flavours, 'to buy that', 3)
                valid = True                                                                                                

            elif choice == '5':
                self.flavour = buy_upgrade(Ice_cream_stand, Ice_cream_stand.flavours, self.flavours, 'to buy that', 4)
                valid = True                                                                                                

            elif choice == '6':
                self.flavour = buy_upgrade(Ice_cream_stand, Ice_cream_stand.flavours, self.flavours, 'to buy that', 5)
                valid = True                                                                                                

            elif choice == '7':
                self.upgrade_screen()

            elif choice == '8':
                self.start_screen(new_day=False)

            elif choice == '':
                self.start_screen(new_day=True)

            else:
                print('That was not a valid number')

        # here to avoid repeating multiple times after the upgrade. Can't go in the function as it has to return self.beach
        self.start_screen(new_day=False)

    def employee_screen(self):
        if self.employee == False:
            print('\nYou do not have an employee. Hire one for £70 per day?')
            valid = False
            while not valid:
                choice = input('(y/n) - ')
                if choice == 'y':
                    print('Successfully hired an employee')
                    self.employee = True
                    self.start_screen(new_day=True)
                elif choice == 'n':
                    self.start_screen(new_day=False)
                else:
                    print('That was not a valid option')
        else:
            print('\nYour employee is costing £70 per day. Fire them?')
            valid = False
            while not valid:
                choice = input('(y/n) - ')
                if choice == 'y':
                    print('Successfully fired your employee')
                    self.employee = False
                    self.start_screen(new_day=True)
                elif choice == 'n':
                    self.start_screen(new_day=False)
                else:
                    print('That was not a valid option')

    def upgrade_screen(self):
        print(f'\nWhat do you want to upgrade:\n1) Beach\n2) Ice cream machine\n3) Selection of ice cream flavours\n4) BACK')

        valid = False
        while not valid:
            choice = input('Type number: ')
            
            if choice == '1':
                self.upgrade_beach()

            elif choice == '2':
                self.upgrade_machine()

            elif choice == '3':
                self.upgrade_flavours()

            elif choice == '4':
                self.start_screen(new_day=False)

            elif choice == '':
                self.start_screen(new_day=True)
                
            else:
                print('That was not a valid input')

    def change_price_screen(self):
        print(f'Old price: £{self.price}')
        valid = False
        while not valid:
            try:
                self.price = round(float(input('New price: £')), 2)
                # checks if the number has more than 3 dp. eg. 3.999
                # I'm so stupid its obviously not working because it rounds before the check ToT
                if int(f'{self.price:e}'.split('e')[-1]) >= 3:
                    raise ValueError
                else:
                    self.start_screen(new_day=True)
            except ValueError:
                print('That was not a valid number')

    def change_number_ice_creams_made_screen(self):
        print('(leave blank to remove limit)')
        if self.max_made == self.machine[1]:
            print('Old number: No limit')
        else:
            print('Old number:', self.max_made)
        valid = False
        while not valid:
            try:
                new = input('New number: ')
                new = float(new)
                if str(new)[-2:] == '.0':
                    self.max_made = int(new)
                    self.start_screen(new_day=True)
                else:
                    raise ValueError
            except ValueError:
                if new == '':
                    self.max_made = self.machine[1]
                    self.start_screen(new_day=True)
                else:
                    print('that was not a valid number')

    def configure_screen(self):
        print('\n1) price per ice cream\n2) number of ice creams made\n3) Mains Integrated Pricing Mechanism\n4) BACK')

        valid = False
        while not valid:
            choice = input('Type number: ')

            if choice == '1':
                self.change_price_screen()

            elif choice == '2':
                self.change_number_ice_creams_made_screen()

            elif choice == '3':
                self.MIPM_screen()

            elif choice == '4':
                self.start_screen(new_day=False)

            elif choice == '':
                self.start_screen(new_day=True)

    def MIPM_screen(self):
        def whats_changing():
            print('\nWhat would you like it to change?')
            print('1) price of ice creams')
            print('2) ice cream limit')
            choice = input('Type number: ')

            if choice == '1':
                return 'price'
            elif choice == '2':
                return 'limit'
            
        def when_changing():    
            print('\nWhen do you want it to be changed?')
            print('1) a certain day of the year') # day
            print('2) when the price is lower than a certain amount') # plower
            print('3) when the price is a certain amount') # pis
            print('4) when the price is higher than a certain amount') # phigher
            print('5) when a season starts') # season
            print('6) when the beach is upgraded') # beach
            print('7) when the machine is upgraded') # machine
            print('8) when the flavour is upgraded') # flavour
            print('9) when the money is higher than a certain amount') # mhigher
            print('10) when the money is lower than a certain amount') # mlower
            choice = input('Type number: ')

            if choice == '1':
                ret = ['day is']
                choice = int(input('Which day: '))
                ret.append(choice)
                return ret

            elif choice == '2':
                ret = ['price is lower than']
                choice = input('Enter price: £')
                ret.append(choice)
                return ret

            elif choice == '3':
                ret = ['price is']
                choice = input('Enter price: £')
                ret.append(choice)
                return ret

            elif choice == '4':
                ret = ['price is higher than']
                choice = input('Enter price: £')
                ret.append(choice)
                return ret

            elif choice == '5':
                ret = ['season is']
                print('\nWhich season:')
                print('1) Summer')
                print('2) Autumn')
                print('3) Winter')
                print('4) Spring')
                choice = input('Type number: ')
                if choice == '1':
                    ret.append('summer')
                elif choice == '2':
                    ret.append('autumn')
                elif choice == '3':
                    ret.append('winter')
                elif choice == '4':
                    ret.append('spring')
                    
                return ret

            elif choice == '6':
                ret = ['beach is']
                
            elif choice == '7':
                ret = ['machine is']
                
            elif choice == '8':
                ret = ['flavour is']

            if choice == '6' or choice == '7' or choice == '8':
                print(f'\nWhen what happens to the {add_mipm[-1]}?')
                print("1) it's higher than a certain level")
                print("2) it's lower than a certian level")
                choice = input('Type number: ')

                if choice == '1':
                    choice = 'higher'

                elif choice == '2':
                    choice = 'lower'

                level = input('Enter level: ')
                ret.append(choice + ' than ' + level.replace(' ', ''))

                return ret

            elif choice == '9':
                ret = ['money is higher than']
                choice = input('\nWhen money is higher than what: ')
                ret.append(choice)
                return ret

            elif choice == '10':
                ret = ['money is lower than']
                choice = input('\nWhen money is lower than what: ')
                ret.append(choice)
                return ret

        def changing_to_what(price_or_limit):
            print(f'\nWhat do you want the {price_or_limit} to be changed to?')
            if price_or_limit == 'price':
                end = '£'
                intager = False
            else:
                end = ''
                intager = True
                
            choice = float(input(f'Enter number: {end}'))
            if intager:
                choice = round(choice)
            else:
                choice = round(choice, 2)
                
            ret = choice
            return ret

        # the actual MIPM_screen function starts here
        print()
        n = 0
        for i in range(len(self.MIPMs)):
            n += 1
            mipm = self.MIPMs[i]
            # if we changed price, we want a pound sign. If we changed season, we don't want it to say level. This ficilitates that
            if mipm[0] == 'price':
                prefix = '£'
            else:
                prefix = ''
            if 'beach' in mipm[1] or 'machine' in mipm[1] or 'flavour' in mipm[1]:
                level = 'level '
            elif 'money' in mipm[1]:
                level = '£'
            else:
                level = ''
                
            print(f'{n}) Make the {mipm[0]} {prefix}{mipm[3]} when the {mipm[1]} {level}{mipm[2]}')
            
        mipm_price = round(4000 * 1.4 ** n, 2)
        print(f'{n+1}) buy new MIPM for £{commafy(mipm_price)}')
        print(f'{n+2}) BACK')
        print(f'{n+3}) CANCEL')
        number = int(input('Type number: '))

        if 1 <= number <= len(self.MIPMs):
            print('\nWhat do you want to change?')
            print('1) what\'t being changed')
            print('2) when it\'s changed')
            print('3) what it\'s changed to')
            print('4) CANCEL')
            choice = input('Type number: ')

            if choice == '1':
                new = whats_changing()
                self.MIPMs[number-1][0] = new

                new = changing_to_what(self.MIPMs[number-1][0])
                self.MIPMs[number-1][3] = new

            elif choice == '2':
                new1, new2 = when_changing()
                print('news', new1, new2)
                self.MIPMs[number-1][1] = new1
                self.MIPMs[number-1][2] = new2

            elif choice == '3':
                new = changing_to_what(self.MIPMs[number-1][0])
                self.MIPMs[number-1][3] = new

            elif choice == '4':
                self.start_screen(new_day=undefined)

            print('MIPM changed')
            print(self.MIPMs[number-1])

        elif number == len(self.MIPMs) + 1:
            add_mipm = []
            
            price_or_limit = whats_changing()
            add_mipm.append(price_or_limit)

            when1, when2 = when_changing()
            add_mipm.append(when1)
            add_mipm.append(when2)

            what = changing_to_what(price_or_limit)
            add_mipm.append(what)

            print('Added MIPM')
            print(add_mipm)
            self.MIPMs.append(add_mipm)

        self.start_screen(new_day=True)

    def activate_MIPMs(self):
        for mipm in self.MIPMs:
            if mipm[1] == 'day is' and day % 365 == mipm[2]:
                change = True

            elif mipm[1] == 'price is lower than' and self.price <= mipm[2]:
                change = True

            elif mipm[1] == 'price is' and self.price == mipm[2]:
                change = True

            elif mipm[1] == 'price is higher than' and self.price >= mipm[2]:
                change = True

            elif mipm[1] == 'season is' and mipm[2].capitalize() == season:
                change = True

            elif mipm[1] == 'beach is' and 

            if change = True:
                if mipm[0] == 'price':
                    self.price = mipm[3]
                elif mipm[0] == 'limit':
                    self.max_made = mipm[3]
                
    def stat_screen(self):
        print(f'\nValuation: £{commafy(self.valuation)}')
        print('\nASSETS:')
        self.calculate_valuation()
        if self.employee:
            print('Employee: Yes')
        else:
            print('Employee: No')
        print('Number of MIPMs:', len(self.MIPMs))
        print('Beach:', self.beach[0])
        print('Machine:', self.machine[0])
        print('Flavours:', self.flavour[0])
        print('\nTODAY:')
        print('Maximum customers at beach:', int(self.beach[1] * self.flavour[1] * self.season_effect()))
        self.calculate_customers()
        print('Number of customers:', self.customers)
        self.calculate_amount_made()
        print('Number of ice creams made:', self.amount_made)
        print(f'Cost per ice cream: £{ICE_CREAM_COST}')
        if self.amount_made - self.customers >= 0:
            print('Unsold ice creams:', self.amount_made - self.customers)
        else:
            print('Unsold ice creams: 0')
        print(f'Price: £{self.price}')
        print('Season:', season)
        print('\nALL TIME:')
        print(f'Total money made: £{commafy(self.total_money_made)}')
        print('Total ice creams sold:', commafy(self.total_ice_creams_sold))
        print()

        self.start_screen(new_day=False)


def buy_company_screen():
    print('\nStart companies:')
    n = number_of_companies(Ice_cream_stand)
    if n == 0:
        price = 0
    else:
        third = 1 / 3
        price = round(1000 * (1+third) ** (n-1), 2)
    print(f'1) ice cream stand - £{commafy(price)}')
    print('2) CANCEL')

    valid = False
    while not valid:
        choice = input('Type number: ')
        
        if choice == '1':
            if Company.total_money >= price:
                name = input('Enter the name of your company: ')
                companies.append(Ice_cream_stand(name))
                print('Successfully bought', name, 'ice cream stand')
                # go to its start screen instead of company list start screen
                companies[len(companies)-1].start_screen(new_day=False)
            else:
                print(f'You need £{round(price - Company.total_money, 2)} more to buy this')

        elif choice == '2' or choice == '':
            #start_screen()
            raise SystemExit

        else:
            print('That was not a valid number')
            buy_company_screen()


    #start_screen()
    raise SystemExit

def calculate_profits():
    total_profit = 0
    
    for company in companies:
        if isinstance(company, Ice_cream_stand):
            # these functions apply to class variables instead of returning something
            company.activate_MIPMs()
            company.calculate_customers()
            company.calculate_amount_made()

            # we can only sell to the number of customers there are. If there are more customers, we can only sell the number of ice creams we have
            # and we can only sell if we are at that company or have an employee
            if Company.pointer == company or company.employee == True:
                profit = min(company.customers, company.amount_made) * company.price
                company.total_ice_creams_sold += min(company.customers, company.amount_made)
            else:
                profit = 0

            # the price of each ice cream
            profit -= company.amount_made * ICE_CREAM_COST
            if company.employee == True:
                profit -= 70

            company.pounds_per_day = round(profit, 2)

            if company.pounds_per_day >= 0:
                company.total_money_made = round(company.total_money_made + company.pounds_per_day, 2)
            total_profit = round(total_profit + profit, 2)

    Company.total_money = round(Company.total_money + total_profit, 2)
    return total_profit

def show_day():
    global day, season
    
    day += 1

    day_of_year = day % 365
    
    if 1 <= day_of_year <= 90 and season != 'Summer':
        season = 'Summer'
        print('\nSUMMER HAS STARTED')
        sleep(2)
        
    elif 91 <= day_of_year <= 181 and season != 'Autumn':
        season = 'Autumn'
        print('\nAUTUMN HAS STARTED')
        sleep(2)
        
    elif 182 <= day_of_year <= 273 and season != 'Winter':
        season = 'Winter'
        print('\nWINTER HAS STARTED')
        sleep(2)
        
    elif 274 <= day_of_year <= 365 and season != 'Spring':
        season = 'Spring'
        print('\nSPRING HAS STARTED')
        sleep(2)
        
    
    if day <= 365:
        print(f'\n------- DAY {day} -------')
    else:
        if day % 365 <= 9:
            print(f'\n---- YEAR {int(day / 365)} DAY {day%365} -----')
        else:
            print(f'\n---- YEAR {int(day / 365)} DAY {day%365} ----')

    total_profits = calculate_profits()

    return total_profits


# to stop recursion, put the global start_screen in a while loop. Anything that goes to this start_screen just has to return None. For each function in global start_screen, put it in a try except RecursionError block. If except is ran, print 'We're sorry to stop you there, but for memory reasons we've put you back to here. Everything is saved, you can carry on how you were with no problems.'
playing = True
while playing:
    n = 0
    valuations = []
    total_valuation = 0
    for company in companies:
        n += 1
        company.calculate_valuation()
        total_valuation += company.valuation
        # structure of valuations
        valuations.append([company.name, company.valuation, company.pounds_per_day])
    
    total_profits = show_day()
    print(f'Money: £{commafy(Company.total_money)}')
    print(f'Valuation: £{commafy(total_valuation)}')
    print(f'Total daily income: £{commafy(total_profits)}')
    print('\nCompanies: ')
    n = 0
    for i in valuations:
        n += 1
        print(f'{n}) {i[0]} -- £{commafy(i[1])} valuation; £{commafy(i[2])} daily income')
    print(f'{n+1}) create new company')

    continue_loop = True
    while continue_loop:
        choice = input('Type number: ')

        if isint(choice) or isfloat(choice):
            choice = int(choice)
            if 1 <= choice <= len(companies):
                try:
                    companies[choice-1].start_screen(new_day=False)
                except RecursionError:
                    print("\nWe're sorry to stop you there, but for memory reasons we've put you back to here. Don't worry, everything is saved so you can carry on how you were with no problems")
                    sleep(2)
                    continue_loop = False
                except SystemExit:
                    continue_loop = False
                
            elif choice == len(companies) + 1:
                try:
                    buy_company_screen()
                except RecursionError:
                    print("\nWe're sorry to stop you there, but for memory reasons we've put you back to here. Don't worry, everything is saved so you can carry on how you were with no problems")
                    sleep(2)
                    continue_loop = False
                except SystemExit:
                    continue_loop = False

            else:
                print('That was not a valid number')
                continue_loop = True

        elif choice == '':
            #start_screen()
            continue_loop = False

        else:
            print('That was not a valid number')
