class Rocket:
    def __init__(self, name:str, mass:float) -> None:
        #Ассерт можемо також задати через IF
        #if not isinstance(name, str):
        #    raise AssertionError("Назва ракети має бути типу стрічка")
        assert isinstance(name, str), "Назва ракети має бути типу стрічка"
        assert name.isascii(), "Назва повинна містити символи з таблиці ASCII."
        #assert mass > 0, "Маса має буити більшою за 0!"
        
        self.name = name
        self.mass = mass

    @property
    def info(self):
        return f"Ракета {self.name} важить {self.mass} кг."
    
    @property
    def info_en(self):
        return f"Ракета {self.name} важить {self.convert_mass()} lb."

    def convert_mass(self):
        return self.mass * 2.20462262

class Rocket_2(Rocket):
    def __init__(self, name: str, mass) -> None:
        super().__init__(name, mass)


def test_correct_mass():
    r = Rocket("Falcon 9", 549054)
    assert r.mass > 0, "Маса має буити більшою за 0!"
    return True

#r = Rocket("Falcon 9", 549054)
#print(r.info)
#print(r.info_en)  
# 
if test_correct_mass():
    print("Маса відображається коректно")   