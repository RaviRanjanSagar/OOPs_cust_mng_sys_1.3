#BLL :
import random
class EmployeeMS_inhert:
    employList = []              #static variable ; global storage
    def __init__(self):
        self.id =0
        self.salutation=0
        self.nam=0
        self.age=0
        self.mob=0
        self.mail=0
        self.sex=0
        self.genrt_id=0
        self.star=0
        self.desigination =None         #designation : key factor***
    def addEmployee(self):
        EmployeeMS_inhert.employList.append(self)
    def employeeSearch(self):
        for employee in EmployeeMS_inhert.employList:
            if(employee.id==self.id):
                return employee         #address return


    @staticmethod
    def delEmployee(id):
        for employee in EmployeeMS_inhert.employList:
            if(id==employee.id):
                EmployeeMS_inhert.employList.remove(employee)

    @staticmethod
    def searchEmployee(id):
        for employee in EmployeeMS_inhert.employList:
            if(employee.id==id):
                return employee.desigination



class Directors(EmployeeMS_inhert):
    def __init__(self):
        self.share=0
        super().__init__()
class zonalManager(EmployeeMS_inhert):
    def __init__(self):
        self.zone=0
        super().__init__()
class Manager(EmployeeMS_inhert):
    def __init__(self):
        self.area=0
        super().__init__()
class trainers(EmployeeMS_inhert):
    def __init__(self):
        self.course=0
        super().__init__()



#PL:        presentation layer
def mob_Validation():
    while(3):
        mob = input("Enter EMPLOYEE 's contact  : ").strip().upper()
        if(mob.isnumeric()):
            if(len(mob)==10):
                return mob
            else:
                print("\n\t\t|M-E-S-S-A-G-E : Incorrect length of contact number...T-R-Y AGAIN|")
        else:
            print(f"\n\t\t|M-E-S-S-A-G-E : Incorrect format <{mob}> . T-R-Y AGAIN|")

def gen_authentication_Id():
    while(4):
        auth =random.randint(1000000,9999999)
        if auth not in EmployeeMS_inhert.employList:
            s = "ABCDEFGHIJKlMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            x = random.choice(s)
            final = x+"-"+str(auth)
            return final

def star(var):

        if ( "11"<= str(var) <= "25"):
            rank = "|-*-silver-*-|"
            return rank
        elif(str(var)>="26"):
            rank = "|-**-GOLD-**-|"
            return rank










def id_Verification(id):
    for employee in EmployeeMS_inhert.employList:
        if(employee.id==id):
            return True
        else:
            return False









def showProfile(employee):
    print(f"`````````````````````````````````\nTYPE : {employee.desigination} \nBADGE : {employee.star}\n Full  Name : {employee.salutation} {employee.nam}\n Employee Age : {employee.age} \t\tSex : {employee.sex}\nContact no : {employee.mob}\nE-mail : {employee.mail} ")
    if(employee.desigination=="DIRECTOR"):
        print(f"Director 's share : {employee.share}\n")
    elif(employee.desigination=="ZONAL MANAGER"):
        print(f"Zonal - Manager 's Zone : {employee.zone}\n")
    elif (employee.desigination == "MANAGER"):
        print(f"Manager 's Area : {employee.area}\n")
    elif(employee.desigination == "TRAINER"):
        print(f"Trainer 's Course : {employee.course}\n")
    print(f"\t#AUthenticated ID : {employee.genrt_id}\n`````````````````````````````````\n")




print("\n\t\t\t\tWelcome to Ravi 's ERP system A.1.0")    #@ERP INTRO
while (1):
    print("\n************************\nSELECT : ")
    print("For CREATING  EMPLOY ; PRESS 1 ")                #DISPLAYING OPTIONS
    print("For DELETING  EMPLOY ; PRESS 2 ")
    print("For SEARCHING EMPLOY ; PRESS 3 ")
    print("For UPDATING  EMPLOY ; PRESS 4 ")
    print("For DISPLAY   EMPLOY ; PRESS 5 ")
    print("For EXIT      EMPLOY ; PRESS 6 ")
    print("-----------------------------------")
    ch=input("ACTION : ")       #MAIN_ _ACTIONS TAKING
    if(ch=="1"):                #CREATING EMPLOYEES
        while(2):
            print("\n\tTYPE ' DIRT ' For CREATING  DIRECTORs     employ data  ") # DISPLAYING OPTIONS
            print("\tTYPE ' ZM ' For CREATING  ZONAL MANAGER employ data  ")
            print("\tTYPE ' MANG ' For CREATING  MANAGERs      employ data  ")
            print("\tTYPE ' TRNR ' For CREATING  TRAINERs      employ data  ")
            print("\t ' EXIT or X ' for exit  ")
            sel = input("Choose your <TYPE> : ").strip().upper()
            if(sel=="DIRT" or sel=="DIRECTOR"):          #ADDING DIRECTOR 's data
                directMs = Directors()           #CREATING MANGER 'S OBJECT ;gives priority to DIRECTOR CLASS
                directMs.id = input("Enter EMPLOYEE 's ID  : ").strip().upper()
                directMs.salutation=  input("Enter EMPLOYEE 's salut.[Dr./ Mr./Mrs/]  : ").strip().upper()
                directMs.nam= input("Enter EMPLOYEE 'S name: ").strip().upper()
                directMs.age= input("Enter EMPLOYEE 's age      : ").strip().upper()
                directMs.sex= input("Enter EMPLOYEE 's sex [M/F]: ").strip().upper()
                directMs.mob= mob_Validation()
                directMs.mail=input("Enter EMPLOYEE 's E-mail   : ")
                directMs.share= input("Enter EMPLOYEE 's Share  : ").strip().upper()
                directMs.exper= input("Enter EMPLOYEE 's Exprience (yrs)  : ")
                var= directMs.exper
                directMs.star = star(var)
                directMs.genrt_id = gen_authentication_Id()
                directMs.designation = "DIRECTOR"
                directMs.addEmployee()
                print(f"\n\t\t|M-E-S-S-A-G-E : Directors account for REG. id <{directMs.id}> has been successfully created. . .|")
                break

            elif(sel=="ZM" or sel=="ZONAL MANAGER"):    #ADDING ZONAL-MANAGER 's data
                zms = zonalManager()               #CREATING zm 'S OBJECT ; gives priority to ZONAL MANGER CLASS
                zms.id = input("Enter EMPLOYEE 's ID  : ").strip().upper()
                zms.salutation = input("Enter EMPLOYEE 's salut.[Dr./ Mr./Mrs/]  : ").strip().upper()
                zms.nam = input("Enter EMPLOYEE 'S name: ").strip().upper()
                zms.age = input("Enter EMPLOYEE 's age      : ").strip().upper()
                zms.sex = input("Enter EMPLOYEE 's sex [M/F]: ").strip().upper()
                zms.mob = mob_Validation()
                zms.mail = input("Enter EMPLOYEE 's E-mail   : ")
                zms.zone = input("Enter EMPLOYEE 's ZONE  : ").strip().upper()
                zms.exper = input("Enter EMPLOYEE 's Exprience (yrs)  : ")
                var = zms.exper
                zms.star = star(var)
                zms.genrt_id = gen_authentication_Id()
                zms.designation = "ZM "
                zms.addEmployee()
                print(f"\n\t\t|M-E-S-S-A-G-E : Zonal Manager account for REG. id <{zms.id}> has been successfully created. . .|")
                break
            elif(sel=="MANG" or sel=="MANAGER"):        #ADDING MANAGER 's data
                mangMs = Manager()        #CREATING MANGER 'S OBJECT ; gives priority to MANAGER CLASS
                mangMs.id = input("Enter EMPLOYEE 's ID  : ").strip().upper()
                mangMs.salutation = input("Enter EMPLOYEE 's salut.[Dr./ Mr./Mrs/]  : ").strip().upper()
                mangMs.nam = input("Enter EMPLOYEE 'S name: ").strip().upper()
                mangMs.age = input("Enter EMPLOYEE 's age      : ").strip().upper()
                mangMs.sex = input("Enter EMPLOYEE 's sex [M/F]: ").strip().upper()
                mangMs.mob = mob_Validation()
                mangMs.mail = input("Enter EMPLOYEE 's E-mail   : ")
                mangMs.area = input("Enter EMPLOYEE 's Area  : ").strip().upper()
                mangMs.exper = input("Enter EMPLOYEE 's Exprience (yrs)  : ")
                var = mangMs.exper
                mangMs.star = star(var)
                mangMs.genrt_id = gen_authentication_Id()
                mangMs.designation = "MANAGER"
                mangMs.addEmployee()
                print(f"\n\t\t|M-E-S-S-A-G-E : Manager account for REG. id <{mangMs.id}> has been successfully created. . .|")
                break
            elif(sel=="TRNR" or sel=="TRAINER"):        #ADDING TRAINER 's data
                trnMs = trainers()            #CREATING TRAINER 'S OBJECT ;gives priority to TRAINER CLASS
                trnMs.id = input("Enter EMPLOYEE 's ID  : ").strip().upper()
                trnMs.salutation = input("Enter EMPLOYEE 's salut.[Dr./ Mr./Mrs/]  : ").strip().upper()
                trnMs.nam = input("Enter EMPLOYEE 'S name: ").strip().upper()
                trnMs.age = input("Enter EMPLOYEE 's age      : ").strip().upper()
                trnMs.sex = input("Enter EMPLOYEE 's sex [M/F]: ").strip().upper()
                trnMs.mob = mob_Validation()
                trnMs.mail = input("Enter EMPLOYEE 's E-mail   : ")
                trnMs.course = input("Enter EMPLOYEE 's Course  : ").strip().upper()
                trnMs.exper = input("Enter EMPLOYEE 's Exprience (yrs)  : ")
                var = trnMs.exper
                trnMs.star = star(var)
                trnMs.genrt_id = gen_authentication_Id()
                trnMs.designation = "TRAINER"
                trnMs.addEmployee()
                print(f"\n\t\t|M-E-S-S-A-G-E : Trainee account for REG. id <{trnMs.id}> has been successfully created. . .|")
                break
            elif(sel=="EXIT" or sel=="X"):              #exiting
                break
            else:
                print(f"\n\t Invalid choice ; <{sel}>")

    elif(ch=="2"):              #DELETING EMPLOYEES
        id = input("Enter EMPLOYEE 's Reg. ID : ").strip()
        idV = id_Verification(id)
        if(id_Verification(id)):
            EmployeeMS_inhert.delEmployee(id)
            print(f"\n\t\t|M-E-S-S-A-G-E : Employee account for REG. id <{id}> has been successfully deleted. . .|")
        else:
            print(f"\n\t\t|M-E-S-S-A-G-E : <{id}> Doesn't match. T-R-Y AGAIN|")

    elif(ch=="3"):              #SEARCHING EMPLOYEES            xxxxxxxxxxxxxxxxxxxxxxxx
        id = input("Enter EMPLOYEE 's id : ").strip()
        #idV =id_Verification(id)
        if(id_Verification(id)):
            searchMS = EmployeeMS_inhert()
            searchMS.id = id
            employee = searchMS.employeeSearch()
            showProfile(employee)                    #PROBLEM ONLY FISRT STORED data is shown
        else:
            print(f"\n\t\t|M-E-S-S-A-G-E : <{id}> Doesn't match. T-R-Y AGAIN|")


    elif(ch=="4"):              #MODIFYING EMPLOYEES
        id = input("Enter EMPLOYEE 's id : ").strip()
        if (id_Verification(id)):
            static_2 = EmployeeMS_inhert.searchEmployee(id)
            if(employee.desigination=="DIRECTOR"):
                employee.name =input("Enter Director 's Modified FULL  NAME : ").strip()
                employee.mob  =input("Enter Director 's Modified Contact no : : ").strip()
                employee.mail = input("Enter Director 's Modified E-MAIL    : ").strip()
                employee.share = input("Enter Director 's Modified SHARE    : ").strip()
                print(f"\n\t\t|M-E-S-S-A-G-E : Director account for REG. id <{id}> has been successfully UPDATED . .|")

            elif(employee.desigination=="ZM"):
                employee.name = input("Enter ZONAL-MANAGER 's Modified FULL  NAME : ").strip()
                employee.mob = input("Enter  ZONAL-MANAGER 's Modified Contact no : : ").strip()
                employee.mail = input("Enter ZONAL-MANAGER 's Modified E-MAIL     : ").strip()
                employee.zone = input("Enter ZONAL-MANAGER 's Modified SHARE      : ").strip()
                print(f"\n\t\t|M-E-S-S-A-G-E : ZONAL-MANAGER account for REG. id <{id}> has been successfully UPDATED . .|")
            elif(employee.desigination=="MANAGER"):
                employee.name  = input("Enter MANAGER 's Modified FULL  NAME   : ").strip()
                employee.mob   = input("Enter MANAGER 's Modified Contact no  : ").strip()
                employee.mail  = input("Enter MANAGER 's Modified E-MAIL       : ").strip()
                employee.area = input("Enter MANAGER 's Modified SHARE        : ").strip()
                print(f"\n\t\t|M-E-S-S-A-G-E : MANAGER account for REG. id <{id}> has been successfully UPDATED . .|")
            else:
                employee.name  = input("Enter TRAINER 's Modified FULL  NAME   : ").strip()
                employee.mob   = input("Enter TRAINER 's Modified Contact no  : ").strip()
                employee.mail  = input("Enter TRAINER 's Modified E-MAIL       : ").strip()
                employee.course = input("Enter TRAINER 's Modified SHARE        : ").strip()
                print(f"\n\t\t|M-E-S-S-A-G-E : TRAINER account for REG. id <{id}> has been successfully UPDATED . .|")


        else:
            print(f"\n\t\t|M-E-S-S-A-G-E : <{id}> Doesn't match. T-R-Y AGAIN|")

    elif(ch=="5"):              #DISPLAYING ALL
        for employee in EmployeeMS_inhert.employList:
            showProfile(employee)
    elif(ch=="6"):               #EXIT
        break

    else:                       # INVALID INPUTs
        print(f"\n\n\t\t| M-E-S-S-A-G-E : OOPS ! something went wrong . . . Invalid <{ch}> keywords\n\n")


