import pyodbc


##def getconnection():
conn = pyodbc.connect(r'Driver=SQL Server;Server=DESKTOP-7QU74UM\SQLEXPRESS;Database=Project;')
cur = conn.cursor()
##return cur


def fetchallemployee():
##    cur = getconnection()
    cur.execute("select * from EMSdb")
    rows = cur.fetchall()
    return rows


def insertdata():
    ID = int(input('ID'))
    EmpName = input('name')
    Designation = input('Designation')
    Dept =input('Dept')
    Dept_id = int(input('Dept_id'))
    Age = int(input('Age'))
    Salary = int(input('Salary'))

##    cur = getconnection()
##    insert_records = "INSERT INTO EMSdb(ID, EmpName, Designation, Dept, Dept_id, Age, Salary) Values(?,?,?,?,?,?,?)"
##    cur.execute("INSERT INTO EMSdb(ID, EmpName, Designation, Dept, Dept_id, Age, Salary) Values(?,?,?,?,?,?,?)")
    cur.execute(f"INSERT INTO EMSdb Values({ID}, '{EmpName}', '{Designation}', '{Dept}', {Dept_id}, {Age}, {Salary})")
    conn.commit()


def updatedata():
    a = int(input('enter ID to update'))
    w = input('column name')
##    t =cur.execute f"select data_type information_schema.columns where table_name = 'EMSdb' and column_name = '{w}'"
##    print(t)
    
    option = int(input('1 for number value, 2 for char value '))

    if option == 1 :
        v = int(input('enter num value '))    
        update= f"Update EMSdb SET {w} = {v} where ID = {a}"
        cur.execute(update)
        conn.commit()

    else :
        v =(input('enter char value '))    
        update= f"Update EMSdb SET {w} = '{v}' where ID = {a}"
        cur.execute(update)
        conn.commit()


def deletedata():
    rmv = int(input('enter ID to remove'))

##    cur = getconnection()
    delete = f"Delete from EMSdb where ID = {rmv}"
    cur.execute(delete)
    conn.commit()

