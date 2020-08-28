from lib import User
from database import db
consumer_input=["ConsuemrName","ConsumerSurname","ConsumerUsername","ConsumerPassword"]
def getdatafromConsumer():
    consumerinput_data=[]

    for i in consumer_input:
        consumerinput_data.append(input(i+":"))
    return consumerinput_data

def Createconsumerobject():
    return User(*getdatafromConsumer())
def addconsumerdatatodatabase():
     db.append(Createconsumerobject())
def showAllconsumer():
    for user in db:
     user.showData()
def showconsumerbyName():
     print("Student information")
     name=input('Enter name: ') 
     for i in db:
        if(name==i.consumername):
            i.showData()
            break
        else:
         print("Not found")
         break
def programStart():
     if(int(input("Type 1 to start "))==1):
        for i in range(int(input('Add student count:'))):
         addconsumerdatatodatabase()
         i+=1

     showAllconsumer()
     emr=input("Enter 2: for getting student by name \n Enter 3: for getting the longest username \n Enter 4: for getting student name whose password larger than 8 \n "  )
     if (emr=="2"):
        showconsumerbyName()
     if (emr=="3"):
        FindLongest()
     if (emr=="4"):
       FindPasswordwith8character()

def FindLongest():   
   print("The longest Name")
   length=len(db) 
   max=len(db[0].consumername)
   maxelement=db[0]
   for i in range(0,length):
     if( max < len((db[i]).consumername)):
         max=len(db[i].consumername)
         maxelement=db[i]
   maxelement.showData()

def FindPasswordwith8character():
    print("With 8 character")
    length=len(db) 
    a=[]
    for i in range(0,length):
        if(len(db[i].consumerpassword)>8):
         a.append(db[i])
    for i in a:
     print(i.consumername)        
