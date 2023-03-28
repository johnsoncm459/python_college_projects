from datetime import date, datetime

class Customer:
    def __init__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.email = None
        self.dob = None
    
    def get_age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    
    def is_eligble(self):
        return self.get_age() >= 21


class Loan:
    def __init__(self):
        self.id = 1234
        self.agent = "John Doe"
        self.amount = 1000.00
        self.rate = 0.07
        self.customer = None
    
    def __str__(self):
        return "Loan: {0}, {1}, {2}, {3}, {4}".format(self.id, self.agent, self.amount, self.rate, self.customer.id)
    
    def make_loan(self, customer):
        if customer.is_eligble():
            self.customer = customer
        else:
            raise ValueError()


def maintest():
    mycust = Customer()
    mycust.id = input("Please enter customer Id: ")
    mycust.firstname = input("Please enter customer firstname: ")
    mycust.lastname = input("Please enter customer lastname: ")
    mycust.email = input("Please enter customer email: ")
    mycust.dob = datetime.strptime(input("Please enter customer dob (mm/dd/yyyy): "), '%m/%d/%Y')

    print("Customer Content:")
    print("       Id:", mycust.id)
    print("Firstname:", mycust.firstname)
    print(" Lastname:", mycust.lastname)
    print("    email:", mycust.email)
    print("      DOB:", mycust.dob)

    try:
        loan = Loan()
        loan.make_loan(mycust)
        print("Customer is {0} years old.".format(mycust.get_age()))
        print(loan)
    except ValueError:
        print("Customer is not eligible")


if __name__ == "__main__":
    maintest()
