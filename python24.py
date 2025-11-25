#CLASS AND OBJECTS

class faculty:
    def putdata(self):          # method1
        self.id = int(input("enter faculty id "))
        self.name = input("enter name ")
        self.salary = float(input("enter faculty salary "))

    def display(self):          # method2
        print("faculty id:", self.id)
        print("faculty name:", self.name)
        print("faculty salary", self.salary)

a = faculty()
a.putdata()
a.display()
