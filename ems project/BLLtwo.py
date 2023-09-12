import DBALone

class Employee():

    def __init__(self, id = 0, EmpName = 'no name ', designation = 'unknown', dept = 'eh', dept_id = 0, age = 42, salary = 0): 
        self.Id = id
        self.Name = EmpName
        self.Designation = designation
        self.Dept = dept
        self.Dept_id = dept_id
        self.Age = age
        self.Salary = salary


    def getallemployee(self):
        employees = DBALone.fetchallemployee()
        return employees


    def getnewdata(self):
        data = DBALone.insertdata()
        return data

    def update(self):
        up = DBALone.updatedata()
        return up


    def deleterecord(self):
        qa = DBALone.deletedata()
        return qa

