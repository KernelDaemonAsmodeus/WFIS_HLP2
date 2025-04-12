class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def introduction(self):
        return f"Hi, I'm {self.first_name} {self.last_name}."

class Worker(Person):
    def __init__(self, first_name, last_name, age, position, wage):
        super().__init__(first_name, last_name, age)
        self.position = position
        self.wage = wage

    def work_info(self):
        return f"I work as {self.position} and make {self.wage} pln."

class Manager(Worker):
    def __init__(self, first_name, last_name, age, position, wage, team):
        super().__init__(first_name, last_name, age, position, wage)
        self.team = team

    def introduction(self):
        return f"Hi, I'm {self.first_name} {self.last_name} and I manage {len(self.team)} people."

    def add_team_member(self, worker):
        self.team.append(worker)

mr = Manager("mName", "mLastName", 19, "Manager", 20000, [])
wr1 = Worker("wFirstName1", "wLastName1", 40, "Worker", "3000")
wr2 = Worker("wFirstName2", "wLastName2", 36, "Worker", "2000")

print(mr.add_team_member(wr1))
print(mr.add_team_member(wr2))

print(mr.introduction())
print(mr.work_info())

print(wr1.introduction())
print(wr1.work_info())

print(wr2.introduction())
print(wr2.work_info())
