class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name, self.surname, self.phone, self.email = name, surname, phone, email

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    def contact(self):
        print (f'Wybieram numer +48 {self.phone} i dzwonię do {self.full_name}')

    def __str__(self):
        return self.full_name

    def label_length(self):
        print(f'Długość imienia: {len(self.name)} i długość nazwiska {len(self.surname)}') 

    __repr__ = __str__

from faker import Faker

if __name__ == '__main__':
    family = [
        BaseContact('Piotr', 'Kowalski', 123456789, 'piotr.kowalski@wp.pl'),
        BaseContact('Aleksandra', 'Nowak',122334455, 'aleksandra.nowak@wp.pl')
    ]
    fake = Faker()

class BusinessContact(BaseContact):

    def __init__(self, position, company, company_phone, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.position, self.company, self.company_phone = position, company, company_phone

    def contact(self):
        super().contact()
        print(f'Wybieram numer +48 {self.company_phone} i dzwonię do {self.full_name}')

    def label_length(self):
        print(f'Długość imienia: {len(self.name)} i długość nazwiska {len(self.surname)}')

if __name__ == '__main__':
    family = [
        BaseContact('Piotr', 'Kowalski', 123456789, 'piotr.kowalski@wp.pl'),
        BaseContact('Aleksandra', 'Nowak',122334455, 'aleksandra.nowak@wp.pl'),
        BusinessContact('CFO','Apple',133987234,'Krzysztof','Zyk',1234556778,'k.zyk@apple.com')
    ]
    family[1].surname = family[0].surname
    print(sorted(family, key=lambda contact:contact.surname))
    fake = Faker()   

    for person in family:
        person.contact()

def create_contacts():
        for i in range (5):
            print (f'{fake.name()},{fake.phone_number(),{fake.email()}}')

print(create_contacts())
