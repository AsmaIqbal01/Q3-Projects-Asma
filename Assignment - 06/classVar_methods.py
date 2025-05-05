class Bank:
    bank_name="Global Bank"


    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name=name

if __name__=="__main__":
    b1=Bank()
    b2=Bank()

    print(b1.bank_name)
    print(b2.bank_name)

    Bank.change_bank_name("International Bank")

    print(b1.bank_name)
    print(b2.bank_name)