# Character Class

class Character:
    def __init__(self, name="Nikos", xp=0, level=1, type="Man",
                 atk=5, dfn=5):
        self.xp = xp
        self.name = name
        self.level = self.get_level()
        self.rank = self.title()
        self.hp = self.get_hp()
        self.atk = atk
        self.dfn = dfn
        self.type = type
        self.achieve = []
        self.items = []

    def get_hp(self):
        return self.level * 1.5
    
    def get_level(self):
        if self.xp >= 0 and self.xp <= 99:
            return 1
        if self.xp >= 100 and self.xp <= 249:
            return 2
        if self.xp >= 250 and self.xp <= 749:
            return 3
        if self.xp >= 750 and self.xp <= 1199:
            return 4
        if self.xp >= 1200 and self.xp <= 2499:
            return 5
        if self.xp >= 2500 and self.xp <= 4999:
            return 6
        if self.xp >= 5000 and self.xp <= 9999:
            return 7
        if self.xp >= 10000 and self.xp <= 19999:
            return 8
        if self.xp >= 20000 and self.xp <= 34999:
            return 9
        if self.xp >= 35000 and self.xp <= 49999:
            return 10
        if self.xp >= 50000:
            self.xp = 50000
            return "X"

    def title(self):
        if self.level == 1:
            return "Man"
        if self.level == 2 and "ordained" in self.achieve:
            return "Cleric"
        if self.level == 3 and "styx" in self.achieve:
            return "Hero"
        if self.level == 4 and "ambrosia" in self.achieve:
            return "Demigod"
        if self.level == 5 and "ichor" in self.achieve:
            return "Deity"
        if self.level == 6 and "sickle" in self.achieve:
            return "Titan"
        if self.level == 7 and "tartarus" in self.achieve:
            return "Force of Nature"
        if self.level == 8 and "moros" in self.achieve:
            return "Fate"
        if self.level == 9 and "nix" in self.achieve:
            return "Primordial"
        if self.level == 10 and "chaos" in self.achieve:
            return "Agent of Chaos"
        
    def __repr__(self):
        return f"{self.name}, Lvl {self.level} {self.rank}"