import BLLtwo

##obj = BLLtwo.Employee()
##rows = obj.getallemployee()
    
UserInput =input("Press 'F' to fetch data,\n      'I' to Insert data,\n      'U' to update data,\n      'D' to Delete data,\n")
                 # ( 'Q' to Quit\n ")

if UserInput == 'F':
    objemp = BLLtwo.Employee()
    rows = objemp.getallemployee()
        
    for i in rows:
        x = BLLtwo.Employee(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        print(x.__dict__)



elif UserInput == 'I':
    objemp = BLLtwo.Employee()
    q = objemp.getnewdata()
    
    print('new data added')


elif UserInput == 'U':
    objemp = BLLtwo.Employee()
    q = objemp.update()

    print('Data updated')


elif UserInput == 'D':
    objemp = BLLtwo.Employee()
    wq = objemp.deleterecord()

    print('record deleted')
##
##
##
##    elif UserInput == 'Q'
##
##
##
else:
    print('Invalid Input') 
