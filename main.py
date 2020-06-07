class Employee():

  raise_amt=1.04

  def __init__(self,first,last,pay):
    self.first=first
    self.last=last
    self.email=first+"."+last+"@gmail.com"
    self.pay=pay

  def fullname(self):
    return "{} {}".format(self.first,self.last)

  def apply_raise(self):
    self.pay=int(self.pay*self.raise_amt)

class developer(Employee):
  raise_amt=1.10

  def __init__(self,first,last,pay,prog_lang):
    super().__init__(first,last,pay)
    self.prog_lang=prog_lang


class Manager(Employee):
    def __init__(self,first,last,pay,Employee=None):
      super().__init__(first,last,pay)
      if Employee is None:
        self.Employee=[]
      else:
        self.Employee=Employee

    def add_emp(self, emp):
      if emp not in self.Employee:
        self.Employee.append(emp)

    def remove_emp(self, emp):
      if emp  in self.Employee:
        self.Employee.remove(emp)

    def print_emps(self):
      for emp in self.Employee:
        print ('-->',emp.fullname)


dev1=developer("John","Max",5000,"Python")
dev2=developer("Nancy","Pedro",7000,"Java")

mgr_1=Manager("Man","Jas",50000,[dev1])

print (mgr_1.email)

mgr_1.add_emp(dev2)

mgr_1.print_emps
