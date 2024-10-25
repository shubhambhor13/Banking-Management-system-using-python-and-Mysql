# Banking management 
import mysql.connector # type: ignore
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "banking_management"
)
mycursor = db.cursor()
print("Welcome to the SBI Bank")
try:
 print("1.Create Account\n2.View Account\n3.Deposit Money\n4.Withdraw Money\n5.Delete Account")
 choose = input("select one option:")
except ValueError as e:
   print("Something went to wrong ! Please try again")
if choose == '1':
    print("Please Create your account!!")
    a = input("Enter your account_holders_name:")
    b = float(input("Enter your deposit amount:"))
    c = input("Enter your Phone no.:")
    d = input("Enter your Account_number:")

    sql = "Insert into customer(account_holders_name,deposit_amount,phone_number,Account_number) Value(%s,%s,%s,%s)"
    val = (a,b,c,d)
    mycursor.execute(sql,val)
    db.commit()
    print("Successfully create your account")

elif choose == '2':
    print("View Account")
    d = input("Enter your Account_number:")
    sql = "Select*from customer where Account_number =%s "
    val = (d,)
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    if result:
        for x in result:
            print(x)
        print("Account details successfully fetched!")
    else:
        print("Invalid account number. Please try again.")   

elif choose == '3':
    print("Deposit Money")
    try:
        d = input("Enter your Account_number:")
        sql = "select deposit_amount from customer where Account_number =%s "
        val = (d,)
        mycursor.execute(sql,val)
        result = mycursor.fetchone()
        if result:
            current_balance = float(result[0])
            print("current_balance :₹",current_balance)
            deposit_amount = float(input("Enter your deposit_amount:"))
            new_balance = current_balance  + deposit_amount  
            import datetime
            p = datetime.datetime.now()
            sql = "INSERT INTO deposite (Account_number, deposit_amount,datetime, new_balance) VALUES (%s, %s, %s, %s)"
            val =(d,deposit_amount,p,new_balance)
            mycursor.execute(sql,val)
            db.commit()
            print("Deposit Amount datetime",p)
            sql = "Update customer Set deposit_Amount = %s Where Account_number = %s"
            val = (new_balance,d)
            mycursor.execute(sql,val)
            db.commit()
            print("Successfully deposit Amount !! Your new balance ₹:",new_balance)
        else:
         print("Invalid Account number !! Please enter valid account numbar")
         exit()
    except ValueError:
        print("Something went to wrong  amount is not deposit")

elif choose == '4':
   print("Withdraw Money")
   a = input("Enter your Account number:")
   Withdraw_Amount = float(input("Enter the Amount to Withdraw:"))
   sql = "Select deposit_Amount from customer where Account_number = %s"
   val = (a,)
   mycursor.execute(sql,val)
   abc = mycursor.fetchone()
   if abc:
      current_balance = float(abc[0])
      minimum_balance = 1000
      if Withdraw_Amount <= current_balance:
         print("Sufficent balance ")
         if Withdraw_Amount >= minimum_balance:
             new_balance = current_balance - Withdraw_Amount  
             if new_balance >= minimum_balance:
                sql = "Update customer Set deposit_amount = %s Where Account_number = %s"
                val = (new_balance,a)
                mycursor.execute(sql,val)
                db.commit()
                print("Withdraw Successfully ! Your current Balance is ₹",new_balance)
                import datetime
                p = (datetime.datetime.now()) 
                sql = "INSERT INTO withdraw (Account_number, Withdraw_Amount, datetime, Remainning_Balance) VALUES (%s, %s, %s, %s)"
                val = (a,Withdraw_Amount,p,new_balance)
                mycursor.execute(sql,val)
                db.commit()
                print("Withdraw amount datetime",p)
             else:
                print("Withdraw UnSuccessfully")
                print("After withdrew your balance less than minimum balance(1000) Remaining Balance",new_balance,"! Your withdrw process Exit !")
         else:
            print("Withdraw Failed ! Your Withdraw amount Greater than Minimum balance ! Please try again")   
      else:
         print("Insufficent balance")
   else:
      print("Account not found")
      
elif choose == '5':
   print("Delete Bank Account")
   s = input("Do you want to delete your account? (yes/no): ")
   if s == 'yes':
     a = input("Please enter your Account Number to  deletion: ")
     sql = "Delete From customer where Account_number = %s"
     val = (a,)
     mycursor.execute(sql,val)
     db.commit()
     print("Deleted your account successfully")
   else:
      print("Not Deleted your account !! Please try again")

else:
   print("choose wrong option !! please choose correct option")
print("Thnak you !!")
