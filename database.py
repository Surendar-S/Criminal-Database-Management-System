import sqlite3

class Databases():
  def PoliceDB(self):
    con = sqlite3.connect("Databases/PoliceDB.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Police_Details(Name varchar, Rank varchar, Police_ID varchar, DOB varchar, State varchar, District varchar, Branch varchar, Gender varchar, Phno varchar, Emailid varchar)")
    cur.execute("CREATE TABLE IF NOT EXISTS Police_Login(Police_ID varchar, Password varchar, Re_Password varchar)")
    con.commit()
    con.close()

  def CriminalDB(self):
    con = sqlite3.connect("Databases/CriminalDB.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Criminal_Details(Name varchar, ID varchar, Age varchar, Gender varchar, Phone_number varchar, Address varchar, No_of_cases varchar, No_of_yrs_prisoned varchar, Case_history varchar)")
    con.commit()
    con.close()

