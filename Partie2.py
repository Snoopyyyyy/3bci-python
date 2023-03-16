import random
import json

# chere florian, au vue de cette ennoncé qui me turlupine (poo avec des dico)
# j'ai dessider de faire deux façon, une qui me parait correct et l'autre qui respect ton ennoncé
# Enjoy !

class HumanClean:
    # construcotr with all Human atribute
    def __init__(self, firstname, surname, age, gender):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.gender = gender

    # getter
    def get_firstname(self):
        return self.firstname
    
    # setter
    def set_firstname(self, firstname):
        self.firstname = firstname

    # getter
    def get_surname(self):
        return self.surname
    
    # setter
    def set_surname(self, surname):
        self.surname = surname

    # getter
    def get_age(self):
        return self.age
    
    # setter
    def set_age(self, age):
        self.age = age

    # getter
    def get_gender(self):
        return self.gender
    
    # setter
    def set_gender(self, gender):
        self.gender = gender

    # return a json string with all human attribute 
    def serialize(self):
        return json.dumps({
            'firstname': self.firstname,
            'surname': self.surname,
            'age': self.age,
            'gender': self.gender
        })

class HumanDico:
    # construcotr with all Human atribute but store in a dictionary
    def __init__(self, firstname, surname, age, gender):
        self.me = {
            'firstname': firstname,
            'surname': surname,
            'age': age,
            'gender': gender
        }
        
    # setter
    def _set_me(self, me):
        self.me = me

    # getter
    def _get_me(self):
        return self.me

    # return a json string with all human attribute stored in the dictionary
    def serialize(self):
        return json.dumps(self.me)
    
jakie = HumanClean("jakie", "biden", 72, "Transpalette");
joe = HumanDico("joe", "biden", 10, "Ferrarie");

print(jakie.serialize())
print(joe.serialize())