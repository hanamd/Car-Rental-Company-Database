import mysql.connector as mysql

try:
    db = mysql.connect(
      host = "localhost",
      user = "root",
      database = "new_data"
    )

    db = mysql.connector.connect(user="root",  host='127.0.0.1', database="testtest")
    mycursor = db.cursor()
    
    Queries to fill carlist with data
    mycursor.execute("INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES ('Compact','55','300')") #1
    mycursor.execute("INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES ('Large','60','400')") #2
    mycursor.execute("INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES ('Medium','75','510')") #3
    mycursor.execute("INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES ('SUV','85','580')") #4
    mycursor.execute("INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES ('Truck','80','530')")#5
    mycursor.execute("INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES ('Van','90','600')")#6
    #db.commit()
    
    
    #Queries to fill 20 cars with data
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10001','Camry','2006','Compact')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10002','Dodge','2010','Large')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10003','Ford','2011','Medium')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10004','Lexus','2013','SUV')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10005','Fiat','2015','Truck')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10006','BMW','2020','Van')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10007','Rover','2017','Compact')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10008','Toyota','2021','Large')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10009','Volvo','2016','Medium')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10010','Bently','2017','SUV')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10011','Audi','2018','Truck')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10012','Volks Wagen','2020','Van')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10013','Jeep','2021','Compact')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10014','Subaru','2022','Large')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10015','Jaguar','2009','Medium')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10016','Mini','2006','SUV')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10017','Lamborghini','2010','Truck')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10018','Bugattie','2014','Van')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10019','Ferrari','2013','Compact')")
    mycursor.execute("INSERT INTO `cars`(`Vehical_ID`, `Model`, `Year`, `car_type`) VALUES ('10020','Mercede','2014','Large')")
    
    
    
    
    
    
    
    
    #Queries to fill 15 customers with data
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('A','Tammy','650-323-8567 ')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('B','Bill','650-236-3345 ')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('B','Sue','650-221-3459 ')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('B','Barbara','650-922-1235 ')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('C','John','652-788-2979')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('C','Scott','650-335-9032')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('C','Don','650-223-4502')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('D','Martin','650-223-4598')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('D','Jan','650-977-3883')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('E','Kelly','655-875-0058')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('E','John','650-198-2433')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('G','Ruth ','650-323-8911 ')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('H','Marco','650-723-8901')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('K','Sandra','650-256-8119')")
    mycursor.execute("INSERT INTO `customers`(`FInit`, `LName`, `Phone`) VALUES ('H','Kathy','650-969-7296')")
    
    mycursor.execute("INSERT INTO `customers`(`ID_no`,`FInit`, `LName`, `Phone`) VALUES ('24','H','Kathy','650-969-7296')")
    
    
    #yyyy-mm-dd
    #Queries to fill rentals with data
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`,`daily_rental`,`num_days`) VALUES ('2022-05-07 ', 'A1340','1', '3')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`, `num_weeks`) VALUES ('2022-05-11 ','A1651','1', '1')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-05-20 ',   'A1562','1', '4')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`,`num_weeks`) VALUES ('2022-06-01 ', 'A1373','1', '2')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-06-17 ',   'A1994','1', '1')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`, `num_weeks`) VALUES ('2022-06-22 ','A1225','1', '1')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-07-06 ',   'A1236','1', '5')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`, `num_weeks`) VALUES ('2022-09-01 ','A1247','1', '3')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-07-12 ',   'A1458','1', '1')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`, `num_weeks`) VALUES ('2022-10-01 ','A1469','1', '1')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-07-14 ',   'A1470','1', '9')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`, `num_weeks`) VALUES ('2022-10-09 ','A1481','1', '1')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-08-01 ',   'A1322','1', '10')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `weekly_rental`, `num_weeks`) VALUES ('2022-10-23 ','A1333','1', '2')")
    
    mycursor.execute("INSERT INTO `rentals`(`Start_Date`, `Rental_ID`, `daily_rental`,`num_days`) VALUES ('2022-08-14 ',   'A1344','1', '1')")
    
    
    #Queries to fill rents with data
    
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1340','f3faa42b-ce54-','10001','$20.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1651','f3fab55f-ce54-','10002','$30.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1562','f3fb0346-ce54-','10003','$40.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1373','f3fb0b15-ce54-','10004','$50.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1994','f3fb0efa-ce54-','10005','$60.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1225','f3fb157a-ce54-','10006','$70.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1236','f3fb1b10-ce54-','10007','$80.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1247','f3fb1fbd-ce54-','10008','$90.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1458','f3fb2459-ce54-','10009','$100.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1469','f3fb26d3-ce54-','10010','$110.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1470','f3fb291a-ce54-','10011','$120.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1481','f3fb2b6c-ce54-','10012','$130.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1322','f3fb3002-ce54-','10013','$140.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1333','f3fb33df-ce54-','10014','$150.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('A1344','f3fb3658-ce54-','10015','$160.00')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('238973961','f3fb3658-ce54-','10016','$200.00')")
    
    
    
    
    
                                                                                                                    
                                                                                                                    
    mycursor.execute( "SELECT weekly_rates, daily_rates,num_days, num_weeks FROM car_list, rentals, UPDATE rents SET Amount_due = ((weekly_rates * num_weeks)+(daily_rates * num_days)) WHERE Amount_due = '0'")
                                                                                                                    
    mycursor.execute("INSERT INTO `customers`(`ID_no`,`FInit`, `LName`, `Phone`) VALUES ('24','H','Kathy','650-969-7296')")
    mycursor.execute("INSERT INTO `rents`(`Rental_ID`,`ID_no`,`Vehical_ID`,`Amount_due`) VALUES ('238973961','f3fb3658-ce54-','10016','$200.00')")                                                                                                         
    
    

db.commit()

except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("something is wrong ")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
     else:
        print(err)
