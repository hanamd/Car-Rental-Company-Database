#from getpass import getpass
import mysql.connector as mysql
import random
from datetime import datetime
from datetime import timedelta
import functools


try:
    db = mysql.connect(
      host = "localhost",
      user = "root",
      database = "new_data"
    )
    #mycursor = db.cursor()
   # #mycursor.execute("INSERT INTO `customers`(`ID_no`,`FInit`, `LName`, `Phone`) VALUES ('24','H','Kathy','650-969-7296')")
    #mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('238973961','f3fb3658-ce54-','10016','$200.00')")
   # db.commit()
    #Menu
    ans=True
    print("""
    1. Show Compact vehicals available
    2. Show Large vehicals available
    3. Show Medium vehicals available
    4. Show Suv vehicals available
    5. Show Truck vehicals available
    6. Show Van vehicals available
    7. Show Customers List
    8. Show rentals and their dates
    9. Add information about a customer
    10.Add information about a new car
    11.Make a car reservation
    12.Return a rented car
    13. Update rental rate 
    """)
    ans=(int(input("What would you like to do? ")))
    if ans==1:
        mycursor = db.cursor()
        mycursor.execute("SELECT Vehical_ID, Model, Year, car_type FROM cars WHERE car_type = 'Compact'")
        print("************Compact cars***********")
    
        myresult = mycursor.fetchall()
    
        for x in myresult:
            for y in x :
                print(y , end = "\t")
            print("   ")
        print("*******************************")
    
    elif ans==2:
        mycursor.execute("SELECT Vehical_ID, Model, Year, car_type FROM cars WHERE car_type = 'Large'")
        print("************Large cars***********")
    
        myresult = mycursor.fetchall()
    
        for x in myresult:
            for y in x :
                print(y , end = "\t")
            print("   ")
        print("*******************************")
    
    elif ans==3:
        mycursor.execute("SELECT Vehical_ID, Model, Year, car_type FROM cars WHERE car_type = 'Medium'")
        print("************Medium cars***********")
    
        myresult = mycursor.fetchall()
    
        for x in myresult:
            for y in x :
                print(y , end = "\t")
            print("   ")
        print("*******************************")
    
    elif ans==4:
        mycursor.execute("SELECT Vehical_ID, Model, Year, car_type FROM cars WHERE car_type = 'SUV'")
        print("************Suv cars***********")
    
        myresult = mycursor.fetchall()
    
        for x in myresult:
            for y in x :
                print(y , end = "\t")
            print("   ")
        print("*******************************")
    
    elif ans==5:
        mycursor.execute("SELECT Vehical_ID, Model, Year, car_type FROM cars WHERE car_type = 'Truck'")
        print("************Truck cars***********")
    
        myresult = mycursor.fetchall()
        for x in myresult:
            for y in x :
                print(y , end = "\t")
            print("   ")
        print("*******************************")
            
            
    
    elif ans==6:
        mycursor.execute("SELECT Vehical_ID, Model, Year, car_type FROM cars WHERE car_type = 'Van'")
        print("************Van cars***********")
    
        myresult = mycursor.fetchall()
    
        for x in myresult:
            for y in x :
                print(y , end = "\t")
            print("   ")
        print("*******************************")
    
    elif ans==7:
        mycursor.execute("SELECT * FROM `customers`")
        myresult = mycursor.fetchall()
    
        print("************Customer***********")
        for x in myresult:
            for y in x :
                print(y , end = "\t")
            print("   ")
        print("*******************************")
    
    elif ans==8:
        mycursor.execute("SELECT * FROM `rentals`")
        myresult = mycursor.fetchall()
        print("************RENTALS and DATES***********")
        for x in myresult:
            for y in x :
                print(y , end = "\t")
            print("   ")
        print("*******************************")
    
    elif ans==9:
        mycursor = db.cursor()
        print(" To enter cutomer information please enter the following:")
        Intial= (str(input("Enter first Intial: ")))
        LastN = (str(input("Enter Last Name: ")))
        Phone = input("Enter phone number:  ")
        mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('"+ Intial  +"','"+  LastN+"','" + Phone+"')")
        db.commit()
        print("Added to customer system")
        
    elif ans==10:
        mycursor = db.cursor()
        print("To enter Car information please enter the following:")
        ID = input("Enter VIN number found on insurance card : ")
        Model_t = (str(input("Enter Model type: ")))
        Years = input("Enter year of car:  ")
        Type = (str(input("Enter car type (compact, Large,Medium,SUV,Truck, van):  ")))
        mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('"+ ID  +"','"+  Model_t+"','" + Years+"','" + Type+"')")
        db.commit()
        print("Added to car system")
    
    elif ans==11:
        mycursor = db.cursor()
        adr=True
        print("""
        1. Have a customer ID
        2. Don't have customer ID
        """)
        
        adr = (int(input("Select one of the option: ")))
        
        if adr ==1:
            CUS = input("\nPlease Enter your Customer ID to start:")
            rent = (int(input("\nWhat type of rental would you like (1)weekly or (2) daily: ")))
            #kind_of = (str(input("\n what kind of car would you like" 
            
            
            n = (str(random.randint(0,1000000000)))
            if rent==1:
                starter_week = input("\nWhat date would you like to start your rental (in yyyy-mm-dd): ")
                count_1 = input("\nHow many weeks would you like your rental: ")
                #check system if is available
                mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`,`weekly_rental`,`num_weeks`)VALUES ('"+ starter_week  +"','"+ n +"','1','" + count_1+"')") 
                db.commit()
                
                #compare dates
                
                
                
                
            else:
                starer_day = input("\nWhat date would you like to start your rental (in form yyyy-mm-dd): ")
                count_2 = input("\nHow many days would you like your rental: ")
                count_22 = int(count_2)
                #mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`,`daily_rental`,`num_days`)VALUES ('"+ starer_day  +"','"+ n +"','1','" + count_2+"')") 
                #db.commit()
                
                #mycursor.execute("SELECT Return_Date FROM `rentals` WHERE Start_Date = '%s' "%(starer_day))
                #retuns = mycursor.fetchall()
                
                Begindate = datetime.strptime(starer_day, "%Y-%m-%d")
                
                
                Enddate = Begindate.date() + timedelta(days=count_22)
                
                end_2 = str(Enddate)
                
                
                print("Ending date")
                print(end_2)
                
                
                
              #mycursor.execute("SELECT Return_Date FROM `rentals` WHERE Start_Date = '%s' "%(starer_day))
                #mycursor.execute("SELECT * FROM `rentals` WHERE Return_Date >= '%s' "%(Enddate), "Start_Date >= '%s' "%(starer_day)) #signs should be the other way
                #try:
                
                
                mycursor.execute("SELECT * FROM `rentals` WHERE ((Start_Date >  '"+starer_day+"')OR ( Return_Date > '"+starer_day+"' )) AND ((Start_Date > '"+end_2+"' )  OR (Return_Date < '"+end_2+"')) ") #signs should be the other way
                myresult = mycursor.fetchall()
                
                
                if (len(myresult)==0):
                    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`,`daily_rental`,`num_days`)VALUES ('"+ starer_day  +"','"+ n +"','1','" + count_2+"')") 
                    db.commit()
                    print ("added to system")
                    
                    print ("pick a car type:")
                    
                    mycursor.execute("SELECT Vehical_ID, Model, Year, car_type FROM cars WHERE is_available = 1")
                    myresult = mycursor.fetchall()
                    print("--- choose the availabe care out of these options: ")
                    for x in myresult:
                        for y in x :
                            print(y , end = "\t")
                        print("                  ")
                    
                    print("*******************************")
                    
                    cat = (input("Enter the vehical ID of the one you want: "))
                    jop = (input("Enter your Rental ID: "))
                    
                    #update system 
                
                    mycursor.execute("UPDATE rents SET Rental_ID = '" + ID_n + "'" ", ID_no '" + CUS + "'" ",Vehical_ID = '" + cat + "'")
                
                else:
                    print("************RENTALS***********")
                    for x in myresult:
                        for y in x :
                            print(y , end = "\t")
                        print("                  ")
                    print("--- please choose another date these are taken!!! --")
                    print("*******************************")
                
                #except:
                   # mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`,`daily_rental`,`num_days`)VALUES ('"+ starer_day  +"','"+ n +"','1','" + count_2+"')") 
                    #db.commit()
                    #print ("added to system")
                
                    
                
                
                #mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`,`daily_rental`,`num_days`)VALUES ('"+ starer_day  +"','"+ n +"','1','" + count_2+"')") 
                #db.commit()
               
        else:
            print("\nGo to option 9 in menu to creat your customer profile")
            
        
        
        
            
            
            
            
            
            
            
            
            mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('"+ ID  +"','"+  Model_t+"','" + Years+"','" + Type+"')")
            db.commit()
        print("Added to car system")
    
        
        
    
    elif ans==12:
        mycursor = db.cursor()
        print("You are in the system to return a car:")
        ID_n = input("Please enter your rental ID: ")
        qu = (int(input("was you rental (1)daily  or (2) weekly: ")))
        Vhic = input("Please enter your VIN(vehical ID) number: ")
        type_of = (str(input("Enter car type (Compact, Large,Medium,SUV,Truck, Van) PLEASE MATCH SPELLING AND CAP:  ")))
        
        
        if qu==1:
           
           mycursor.execute("SELECT num_days FROM `rentals` WHERE  Rental_ID =  "+ID_n+"")
          
           myresult = mycursor.fetchall()
           
           
           for x in myresult:
           
            
            cur = x[0]
            
            mycursor.execute("SELECT daily_rates FROM `car_list` WHERE car_type = '"+type_of+"'")
            
            myresul = mycursor.fetchall()
            for y in myresul:
                
                vi = y[0]
            
            
            #num = functools.reduce(lambda N, digit: N * 10 + digit, vi, cur)
            
           # num_z = functools.reduce(lambda N, digit: N * 10 + digit, cur)
            total = (vi*cur)
            print ("Amount due for daily rate:", total)
            mycursor = db.cursor()
            mycursor.execute("UPDATE cars SET is_available = 1 WHERE Vehical_ID = '" + ID_n + "'")
            
            mycursor.execute("UPDATE rents SET Amount_due= "+str(total)+", is_scheduled = 0, is_active = 0 WHERE Vehical_ID = '" + ID_n + "'")
            db.commit()
            
            
            

        else:
        
            mycursor.execute("SELECT num_weeks FROM `rentals` WHERE Rental_ID = '"+ID_n+"'")
            myresult = mycursor.fetchall()
           
           
            for x in myresult:
            
                
                cur = x[0]
                
                mycursor.execute("SELECT weekly_ratesFROM `car_list` WHERE car_type = '"+type_of+"'")
                
                myresul = mycursor.fetchall()
                for y in myresul:
                    
                    vi = y[0]
                
                
                #num = functools.reduce(lambda N, digit: N * 10 + digit, vi, cur)
                
            # num_z = functools.reduce(lambda N, digit: N * 10 + digit, cur)
                total = (vi*cur)
                print ("Amount due for weekly rate:", total)
                mycursor = db.cursor()
                mycursor.execute("UPDATE cars SET is_available = 1 WHERE Vehical_ID = '" + ID_n + "'")
                
                mycursor.execute("UPDATE rents SET Amount_due= "+str(total)+", is_scheduled = 0, is_active = 0 WHERE Vehical_ID = '" + ID_n + "'")
                db.commit()
    if ans==13:
        vlo = input("what type of car would you like to update (Compact, Large,Medium,SUV,Truck, Van) PLEASE MATCH SPELLING AND CAP: ")
        
        blo = (int(input(("what would you like to update (1)daily rate or (2)weekly rate: "))))
        
        if blo==1:
        #daily
         yu = input("Enter the daily rate to update to : ")
         mycursor = db.cursor()
         mycursor.execute("UPDATE car_list SET daily_rate = '" + yu + "'" " WHERE car_type = '" + vlo + "'")
         db.commit()
        else:
        #weekly
          pu = input("Enter the weekly rate to update to : ")
          mycursor = db.cursor()
          mycursor.execute("UPDATE car_list SET weekly_rate = '" + pu + "'" " WHERE car_type = '" + vlo + "'")
          db.commit()
            
    elif ans !="":
      print("\nNot Valid Choice Try again")
    
    
    
    
    
    
    
    
    
    #erro found mysql.connector.errors.ProgrammingError: 1054 (42S22): Unknown column 'daily_rate' in 'field list' in line 360
    
    
    
    
    
    
    
   
    
   
    
   
    
   
    
    
    # get all records
    #records = cursor.fetchall()
    
    # do compact, customers, suv, current rental etc
    
   
    
   
    
        
        
   
    
       


except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("something is wrong ")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
     else:
        print(err)

#db = mysql.connector.connect(user="root",  host='127.0.0.1', database="testtest")
#mycursor = db.cursor()

#Queries to fill carlist with data
#mycursor.execute("INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES ('Compact','55','300')") #1
#mycursor.execute("INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES ('Large','60','400')") #2
#mycursor.execute("INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES ('Medium','75','510')") #3
#mycursor.execute("INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES ('SUV','85','580')") #4
#mycursor.execute("INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES ('Truck','80','530')")#5
#mycursor.execute("INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES ('Van','90','600')")#6
##db.commit()
#
#
##Queries to fill cars with data
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10001','Camry','2006','Compact')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10002','Dodge','2010','Large')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10003','Ford','2011','Medium')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10004','Lexus','2013','SUV')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10005','Fiat','2015','Truck')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10006','BMW','2020','Van')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10007','Rover','2017','Compact')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10008','Toyota','2021','Large')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10009','Volvo','2016','Medium')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10010','Bently','2017','SUV')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10011','Audi','2018','Truck')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10012','Volks Wagen','2020','Van')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10013','Jeep','2021','Compact')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10014','Subaru','2022','Large')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10015','Jaguar','2009','Medium')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10016','Mini','2006','SUV')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10017','Lamborghini','2010','Truck')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10018','Bugattie','2014','Van')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10019','Ferrari','2013','Compact')")
#mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10020','Mercede','2014','Large')")
#
#
#
#
#
#
#
#
##Queries to fill customers with data
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('A','Tammy','650-323-8567 ')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('B','Bill','650-236-3345 ')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('B','Sue','650-221-3459 ')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('B','Barbara','650-922-1235 ')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('C','John','652-788-2979')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('C','Scott','650-335-9032')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('C','Don','650-223-4502')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('D','Martin','650-223-4598')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('D','Jan','650-977-3883')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('E','Kelly','655-875-0058')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('E','John','650-198-2433')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('G','Ruth ','650-323-8911 ')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('H','Marco','650-723-8901')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('K','Sandra','650-256-8119')")
#mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('H','Kathy','650-969-7296')")

#mycursor.execute("INSERT INTO `customers`(`ID_no`,`FInit`, `LName`, `Phone`) VALUES ('24','H','Kathy','650-969-7296')")


#yyyy-mm-dd
#Queries to fill rentals with data

#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`,`daily_rental`,`num_days`) VALUES ('2022-05-07 ', 'A1340','1', '3')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`, `num_weeks`) VALUES ('2022-05-11 ','A1651','1', '1')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-05-20 ',   'A1562','1', '4')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`,`num_weeks`) VALUES ('2022-06-01 ', 'A1373','1', '2')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-06-17 ',   'A1994','1', '1')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`, `num_weeks`) VALUES ('2022-06-22 ','A1225','1', '1')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-07-06 ',   'A1236','1', '5')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`, `num_weeks`) VALUES ('2022-09-01 ','A1247','1', '3')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-07-12 ',   'A1458','1', '1')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`, `num_weeks`) VALUES ('2022-10-01 ','A1469','1', '1')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-07-14 ',   'A1470','1', '9')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`, `num_weeks`) VALUES ('2022-10-09 ','A1481','1', '1')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-08-01 ',   'A1322','1', '10')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`, `num_weeks`) VALUES ('2022-10-23 ','A1333','1', '2')")
#
#mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-08-14 ',   'A1344','1', '1')")
#

#Queries to fill rents with data

#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1340','f3faa42b-ce54-','10001','$20.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1651','f3fab55f-ce54-','10002','$30.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1562','f3fb0346-ce54-','10003','$40.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1373','f3fb0b15-ce54-','10004','$50.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1994','f3fb0efa-ce54-','10005','$60.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1225','f3fb157a-ce54-','10006','$70.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1236','f3fb1b10-ce54-','10007','$80.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1247','f3fb1fbd-ce54-','10008','$90.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1458','f3fb2459-ce54-','10009','$100.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1469','f3fb26d3-ce54-','10010','$110.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1470','f3fb291a-ce54-','10011','$120.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1481','f3fb2b6c-ce54-','10012','$130.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1322','f3fb3002-ce54-','10013','$140.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1333','f3fb33df-ce54-','10014','$150.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1344','f3fb3658-ce54-','10015','$160.00')")
#mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('238973961','f3fb3658-ce54-','10016','$200.00')")





                                                                                                                    
                                                                                                                    
#mycursor.execute( "SELECT weekly_rates, daily_rates,num_days, num_weeks FROM car_list, rentals, UPDATE rents SET Amount_due = ((weekly_rates * num_weeks)+(daily_rates * num_days)) WHERE Amount_due = '0'")
                                                                                                                    
                                                                                                                    



#db.commit()
#
#