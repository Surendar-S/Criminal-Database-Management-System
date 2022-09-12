# Self Library Imports
from projectlayout1.form import Ui_layout1
from projectlayout2.form import Ui_layout2
from projectlayout3.form import Ui_layout3
from projectlayout3_5.form import Ui_Layout3_5
from projectlayout4.form import Ui_layout4
from projectlayout5.form import Ui_layout5
from database import Databases

# PyQt5 Imports
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

# Tkinter Imports
from tkinter import messagebox
from tkinter import *

# Basic Imports
import sys
import cv2
import sqlite3
import os
import face_recognition

# Class for Layout3
class Layout3(QMainWindow):
    def __init__(self):
        super(Layout3, self).__init__()
        self.ui3 = Ui_layout3()
        self.ui3.setupUi(self)
        self.ui3.l3_search.returnPressed.connect(self.search)
        self.ui3.L3signoutb4.clicked.connect(self.sign_out)
        self.ui3.l3cameralabel.mousePressEvent = self.layout3_capture
        self.ui3.l3capb1.clicked.connect(self.img_search)
        self.ui3.l4newfileb4.clicked.connect(self.layout3_new_case_file)

    def img_search(self):
        res = []
        res_dict = {}
        myList = os.listdir("Image")
        for i in range(len(myList)):
            search_img = face_recognition.load_image_file('.temp/temp.jpg')
            search_img = cv2.cvtColor(search_img, cv2.COLOR_BGR2RGB)
            db_img = face_recognition.load_image_file('Image/' + myList[i])
            db_img = cv2.cvtColor(db_img, cv2.COLOR_BGR2RGB)
            encode_search_img = face_recognition.face_encodings(search_img)[0]
            encode_db_img = face_recognition.face_encodings(db_img)[0]
            results = face_recognition.compare_faces([encode_search_img], encode_db_img)
            faceDis = face_recognition.face_distance([encode_search_img], encode_db_img)
            if results[0]:
                res.append(faceDis[0])
                res_dict.update({faceDis[0]: myList[i]})
        try:
            true = min(res)
            os.remove(".temp/temp.jpg")
            self.layout3_view(res_dict[true].replace(".jpg", ""))
        except ValueError:
            Tk().withdraw()
            messagebox.askokcancel("NO MATCH", "Given Image Doesn't Match any images in the Database. Please try again!")

    def layout3_view(self, id):
        con = sqlite3.connect("Databases/CriminalDB.db")
        cur = con.cursor()
        cur.execute("SELECT Name, ID, Age, Gender, Phone_number, Address, No_of_cases, No_of_yrs_prisoned, Case_history FROM Criminal_Details WHERE ID = '" + id + "'")
        Details = cur.fetchall()
        Name = Details[0][0]
        ID = Details[0][1]
        Age = Details[0][2]
        Gender = Details[0][3]
        Phno = Details[0][4]
        Address = Details[0][5]
        Noofcases = Details[0][6]
        Noofyrsprisoned = Details[0][7]
        Casehistory = Details[0][8]

        self.ui4 = Layout4(Name, ID, Age, Gender, Phno, Address, Noofcases, Noofyrsprisoned, Casehistory)
        self.ui4.show()

    def sign_out(self):
        Tk().withdraw()
        ch = messagebox.askyesno("CONFIRM", "ARE YOU SURE")
        if ch:
            self.ui = mainwindow()
            self.ui.show()
            self.close()

    def layout3_new_case_file(self):
        self.ui6 = Layout6()
        self.ui6.show()

    def search(self):
        con = sqlite3.connect("Databases/CriminalDB.db")
        cur = con.cursor()
        cur.execute("SELECT Name, ID, Phone_number FROM Criminal_Details")
        cur2 = cur.fetchall()
        for i in cur2:
            Names.append(i[0])
            IDs.append(i[1])
            PhNos.append(i[2])
        self.ui3_5 = Layout3_5(self.ui3.l3_search.text())
        self.ui3_5.show()
        Names.clear()
        IDs.clear()
        PhNos.clear()
        self.close()

    def layout3_capture(self, event):
        cam = cv2.VideoCapture(0)
        while cam.isOpened():
            ret, frame = cam.read()
            k = cv2.waitKey(1)
            if k == ord('c'):
                break
            elif k % 256 == 32:
                img_name = ".temp/temp.jpg"
                cv2.imwrite(img_name, frame)
                pix = QPixmap(".temp/temp.jpg")
                re_pix = pix.scaled(250, 250)
                self.ui3.l3cameralabel.setPixmap(re_pix)
                break
            cv2.imshow("Capture", frame)
        cv2.destroyAllWindows()

# Class for Layout 2
class Layout2(QMainWindow):
    def __init__(self):
        super(Layout2, self).__init__()
        self.ui2 = Ui_layout2()
        self.ui2.setupUi(self)
        #self.showMaximized()
        self.Gender = ""
        # Submit button in Layout 2
        self.ui2.l2checkM.stateChanged.connect(self.Check_Box_ChangedM)
        self.ui2.l2checkF.stateChanged.connect(self.Check_Box_ChangedF)
        self.ui2.l2submitb1.clicked.connect(self.layout_submit)

    def Check_Box_ChangedM(self):
        if self.ui2.l2checkM.isChecked():
            self.ui2.l2checkF.setChecked(False)
            self.Gender = "Male"

    def Check_Box_ChangedF(self):
        if self.ui2.l2checkF.isChecked():
            self.ui2.l2checkM.setChecked(False)
            self.Gender = "Female"

    # Layout2 Button (submit)
    def layout_submit(self):
        if not (self.ui2.l2name.text() == "" or self.ui2.l2rank.text()=="" or self.ui2.l2id.text()=="" or self.ui2.l2dob.text()=="" or self.ui2.l2state.text()=="" or self.ui2.l2district.text()=="" or self.ui2.l2branch.text()=="" or self.Gender=="" or self.ui2.l2password.text()=="" or self.ui2.l2repassword.text()=="" or self.ui2.l2phno.text()=="" or self.ui2.l2mail.text()==""):
            con = sqlite3.connect("Databases/PoliceDB.db")
            cur = con.cursor()
            cur.execute("INSERT INTO Police_Details VALUES (" + "'" + self.ui2.l2name.text() + "'," + "'" + self.ui2.l2rank.text() + "'," + "'" + self.ui2.l2id.text() + "'," + "'" + self.ui2.l2dob.text() + "',"  + "'" + self.ui2.l2state.text() + "'," + "'" + self.ui2.l2district.text() + "'," + "'" + self.ui2.l2branch.text() + "'," + "'" + self.Gender + "'," + "'" + self.ui2.l2phno.text() + "'," + "'" + self.ui2.l2mail.text() + "'" + ")")
            cur.execute("INSERT INTO Police_Login VALUES (" + "'" + self.ui2.l2id.text() + "'," + "'" + self.ui2.l2password.text() + "'," + "'" + self.ui2.l2repassword.text() + "'" + ")")
            con.commit()
            con.close()
            self.close()
        else:
            Tk().withdraw()
            messagebox.askokcancel("Error","sootha mooditu ellathaiyum fill pandra dash")

# CLass for Layout 3_5
class Layout3_5(QMainWindow):
    def __init__(self, txt):
        super(Layout3_5, self).__init__()
        self.ui = Ui_Layout3_5()
        self.ui.setupUi(self)
        self.layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.ui.scrollAreaWidgetContents.setLayout(self.layout)
        self.ui.l3_5back.clicked.connect(self.layout3_5back)
        #self.showMaximized()
        y = 10
        for i in range(len(Names)):
            if txt == Names[i]:
                self.Card_Widget(Names[i], IDs[i], PhNos[i], 10, y)
                y += 160

        self.ui.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, y))

    def layout3_5back(self):
        self.ui3 = Layout3()
        self.ui3.show()
        self.close()

    def Card_Widget(self, name, cid, ph, x, y):
        self.frame = QFrame(self.ui.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(x, y, 780, 150))
        self.frame.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.clayout_cimage_label = QLabel(self.frame)
        self.clayout_cimage_label.setGeometry(QtCore.QRect(25, 25, 100, 100))
        self.clayout_cimage_label.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.clayout_cimage_label.setText("")
        self.clayout_cimage_label.setObjectName("clayout_cimage_label")
        pix = QPixmap("Image/" + cid + ".jpg")
        re_pix = pix.scaled(120, 120)
        self.clayout_cimage_label.setPixmap(re_pix)
        self.view_btn = QPushButton(self.frame)
        self.view_btn.setGeometry(QtCore.QRect(650, 100, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.view_btn.setFont(font)
        self.view_btn.setStyleSheet("color: rgb(0, 0, 0);")
        self.view_btn.setAutoRepeatInterval(10)
        self.view_btn.setObjectName("view_btn")
        self.view_btn.setText("View")
        self.view_btn.clicked.connect(lambda check, arg=cid: self.layout3_5view(arg))
        self.clayout_phno_label = QLabel(self.frame)
        self.clayout_phno_label.setGeometry(QtCore.QRect(150, 95, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clayout_phno_label.setFont(font)
        self.clayout_phno_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.clayout_phno_label.setObjectName("clayout_phno_label")
        self.clayout_phno_label.setText(ph)
        self.clayout_cname_label = QLabel(self.frame)
        self.clayout_cname_label.setText(name)
        self.clayout_cname_label.setGeometry(QtCore.QRect(150, 25, 625, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clayout_cname_label.setFont(font)
        self.clayout_cname_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.clayout_cname_label.setObjectName("clayout_cname_label")
        self.clayout_cid_label = QLabel(self.frame)
        self.clayout_cid_label.setGeometry(QtCore.QRect(150, 60, 500, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clayout_cid_label.setFont(font)
        self.clayout_cid_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.clayout_cid_label.setObjectName("clayout_cid_label")
        self.clayout_cid_label.setText(cid)

    def layout3_5view(self, id):
        con = sqlite3.connect("Databases/CriminalDB.db")
        cur = con.cursor()
        cur.execute("SELECT Name, ID, Age, Gender, Phone_number, Address, No_of_cases, No_of_yrs_prisoned, Case_history FROM Criminal_Details WHERE ID = '" + id + "'")
        Details = cur.fetchall()
        Name = Details[0][0]
        ID = Details[0][1]
        Age = Details[0][2]
        Gender = Details[0][3]
        Phno = Details[0][4]
        Address = Details[0][5]
        Noofcases = Details[0][6]
        Noofyrsprisoned = Details[0][7]
        Casehistory = Details[0][8]

        self.ui4 = Layout4(Name, ID, Age, Gender, Phno, Address, Noofcases, Noofyrsprisoned, Casehistory)
        self.ui4.show()

# Class for Layout 4
class Layout4(QMainWindow):
    def __init__(self, Name, ID, Age, Gender, Phno, Address, No_of_cases, No_years, Case_history):
        super(Layout4, self).__init__()
        self.ui4 = Ui_layout4()
        self.ui4.setupUi(self)
        #self.showMaximized()

        #Layout 4 button
        self.ui4.L4backb1.clicked.connect(self.layout4_back)
        self.ui4.L4editb.clicked.connect(lambda: self.Layout4_edit(Name, ID, Age, Gender, Phno, Address, No_of_cases, No_years, Case_history))
        self.ui4.L4deleteb.clicked.connect(self.layout4_delete)
        self.ui4.l4name.setText(Name)
        self.ui4.l4id.setText(ID)
        pixmap = QPixmap("Image/" + ID + ".jpg")
        re_pix = pixmap.scaled(120, 120)
        self.ui4.l4photolabel.setPixmap(re_pix)
        self.ui4.l4age.setText(Age)
        self.ui4.l4gender.setText(Gender)
        self.ui4.l4phno.setText(Phno)
        self.ui4.l4address.setText(Address)
        self.ui4.l4noofcases.setText(No_of_cases)
        self.ui4.l4noofyrsprisoned.setText(No_years)
        self.ui4.l4casehistory.setText(Case_history)

    def layout4_back(self):
        self.close()

    def layout4_delete(self):
        con = sqlite3.connect("Databases/CriminalDB.db")
        cur = con.cursor()
        cur.execute("DELETE FROM Criminal_Details WHERE ID = '" + self.ui4.l4id.text() + "'")
        con.commit()
        con.close()
        os.remove("Image/" + self.ui4.l4id.text() + ".jpg")
        self.close()

    def Layout4_edit(self, Name, ID, Age, Gender, Phno, Address, No_of_cases, No_years, Case_history):
        self.ui5 = Layout5(Name, ID, Age, Gender, Phno, Address, No_of_cases, No_years, Case_history)
        self.ui5.show()


# Class for Layout 5
class Layout5(QMainWindow):
    def __init__(self, Name, ID, Age, Gender, Phno, Address, No_of_cases, No_years, Case_history):
        super(Layout5, self).__init__()
        self.ui5 = Ui_layout5()
        self.ui5.setupUi(self)
        self.showMaximized()
        self.CriGender = ""
        #layout5 button (function call)
        self.ui5.l5genderMcheck.stateChanged.connect(self.Check_Box_M)
        self.ui5.l5genderFcheck.stateChanged.connect(self.Check_Box_F)
        self.ui5.l5captureb1.clicked.connect(self.layout5_capture)
        self.ui5.l5submitb3.clicked.connect(self.layout5_submit)
        self.ui5.l5criname.setText(Name)
        self.ui5.l5criid.setText(ID)
        self.ui5.l5criage.setText(Age)
        self.CriGender = Gender
        if self.CriGender == "Male":
            self.ui5.l5genderMcheck.setChecked(True)
        else:
            self.ui5.l5genderFcheck.setChecked(True)
        self.ui5.l5criphno.setText(Phno)
        self.ui5.l5address.setText(Address)
        self.ui5.l5noofcases.setText(No_of_cases)
        self.ui5.l5noofprisoned.setText(No_years)
        self.ui5.l5ch.setText(Case_history)

    def Check_Box_M(self):
        if self.ui5.l5genderMcheck.isChecked():
            self.ui5.l5genderFcheck.setChecked(False)
            self.CriGender = "Male"

    def Check_Box_F(self):
        if self.ui5.l5genderFcheck.isChecked():
            self.ui5.l5genderMcheck.setChecked(False)
            self.CriGender = "Male"

    def layout5_submit(self):
        if not (self.ui5.l5criname.text() == "" or self.ui5.l5criid.text() == "" or self.ui5.l5criage.text() == "" or self.CriGender == "" or self.ui5.l5criphno.text() == "" or self.ui5.l5address.toPlainText() == "" or self.ui5.l5noofcases.text() == "" or self.ui5.l5noofprisoned.text() == "" or self.ui5.l5ch.toPlainText() == "" ):
            con = sqlite3.connect("Databases/CriminalDB.db")
            cur = con.cursor()
            cur.execute("UPDATE Criminal_Details SET Name = '" + self.ui5.l5criname.text() + "', ID = " + "'" + self.ui5.l5criid.text() + "', Age = " + "'" + self.ui5.l5criage.text() + "', Gender = " + "'" + self.CriGender + "', Phone_number = " + "'" + self.ui5.l5criphno.text() + "', Address = " + "'" + self.ui5.l5address.toPlainText() + "', No_of_cases = " + "'" + self.ui5.l5noofcases.text() + "', No_of_yrs_prisoned = " + "'" + self.ui5.l5noofprisoned.text() + "', Case_history = " + "'" + self.ui5.l5ch.toPlainText() + "' WHERE ID = '" + self.ui5.l5criid.text() + "'")
            con.commit()
            con.close()
            self.close()
        else:
            Tk().withdraw()
            messagebox.askokcancel("ERROR","FILL ALL THE DETAILS")

    def layout5_capture(self):
        if not self.ui5.l5criid.text() == "":
            cam = cv2.VideoCapture(0)
            while cam.isOpened():
                ret, frame = cam.read()
                k = cv2.waitKey(1)
                if k == ord('c'):
                    break
                elif k % 256 == 32:
                    img_name = "Image/" + self.ui5.l5criid.text() + ".jpg"
                    cv2.imwrite(img_name, frame)
                    self.set_img(self.ui5.l5criid.text())
                    break
                cv2.imshow("Capture", frame)
            cv2.destroyAllWindows()
        else:
            Tk().withdraw()
            messagebox.askokcancel("Error", "Please Enter Criminal ID to Capture Image")

    def set_img(self, id):
        pix = QPixmap("Image/" + id + ".jpg")
        re_pix = pix.scaled(120, 120)
        self.ui5.l5capturel.setPixmap(re_pix)

class Layout6 (QMainWindow):
    def __init__(self):
        super(Layout6, self).__init__()
        self.ui5 = Ui_layout5()
        self.ui5.setupUi(self)
        # self.showMaximized()
        self.CriGender = ""
        self.ui5.l5genderMcheck.stateChanged.connect(self.Check_Box_M)
        self.ui5.l5genderFcheck.stateChanged.connect(self.Check_Box_F)
        self.ui5.l5captureb1.clicked.connect(self.layout5_capture)
        self.ui5.l5submitb3.clicked.connect(self.layout5_submit)

    def Check_Box_M(self):
        if self.ui5.l5genderMcheck.isChecked():
            self.ui5.l5genderFcheck.setChecked(False)
            self.CriGender = "Male"

    def Check_Box_F(self):
        if self.ui5.l5genderFcheck.isChecked():
            self.ui5.l5genderMcheck.setChecked(False)
            self.CriGender = "Male"

    def layout5_submit(self):
        if not(self.ui5.l5criname.text() == "" or self.ui5.l5criid.text() == "" or self.ui5.l5criage.text() == "" or self.CriGender == "" or self.ui5.l5criphno.text() == "" or self.ui5.l5address.toPlainText() == "" or self.ui5.l5noofcases.text() == "" or self.ui5.l5noofprisoned.text() == "" or self.ui5.l5ch.toPlainText() == ""):
            print("Entered")
            con = sqlite3.connect("Databases/CriminalDB.db")
            cur = con.cursor()
            cur.execute("INSERT INTO Criminal_Details VALUES (" + "'" + self.ui5.l5criname.text() + "'," + "'" + self.ui5.l5criid.text() + "'," + "'" + self.ui5.l5criage.text() + "'," + "'" + self.CriGender + "'," + "'" + self.ui5.l5criphno.text() + "'," + "'" + self.ui5.l5address.toPlainText() + "'," + "'" + self.ui5.l5noofcases.text() + "'," + "'" + self.ui5.l5noofprisoned.text() + "'," + "'" + self.ui5.l5ch.toPlainText() + "'" + ")")
            con.commit()
            con.close()
            self.close()
        else:
            Tk().withdraw()
            messagebox.askokcancel("ERROR", "FILL ALL THE DETAILS")

    def layout5_capture(self):
        if not self.ui5.l5criid.text() == "":
            cam = cv2.VideoCapture(0)
            while cam.isOpened():
                ret, frame = cam.read()
                k = cv2.waitKey(1)
                if k == ord('c'):
                    break
                elif k % 256 == 32:
                    img_name = "Image/" + self.ui5.l5criid.text() + ".jpg"
                    cv2.imwrite(img_name, frame)
                    self.set_img(self.ui5.l5criid.text())
                    break
                cv2.imshow("Capture", frame)
            cv2.destroyAllWindows()
        else:
            Tk().withdraw()
            messagebox.askokcancel("Error", "Please Enter Criminal ID to Capture Image")

    def set_img(self, id):
        pix = QPixmap("Image/" + id + ".jpg")
        re_pix = pix.scaled(120, 120)
        self.ui5.l5capturel.setPixmap(re_pix)

# Class for Layout 1
class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_layout1()
        self.ui.setupUi(self)
        #self.showMaximized()

        # Set background
        # self.setStyleSheet("background-image: url(background_image/bg.jpg);")

        # Layout 1 Create New Account Button (function call)
        self.ui.l1createb2.clicked.connect(self.layout_create_new_account)
        self.ui.l1signb1.clicked.connect(self.layout_sign_in)

    # Layout 1 Create New Account Button
    def layout_create_new_account(self):
        self.ui2 = Layout2()
        self.ui2.show()

    # Layout 1 Sign In button
    def layout_sign_in(self):
        pid = self.ui.l1pid.text()
        ppassword = self.ui.l1ppassword.text()
        self.state = self.check_id_and_pass(pid, ppassword)
        if self.state:
            self.ui3 = Layout3()
            self.ui3.show()
            self.close()

    def check_id_and_pass(self, id, passwd):
        IDs = []
        con = sqlite3.connect("Databases/PoliceDB.db")
        id_cur = con.cursor()
        pass_cur = con.cursor()
        id_cur.execute("Select Police_ID from Police_Login")
        row = id_cur.fetchall()
        for i in row:
            IDs.append(i[0])
        if id in IDs:
            pass_cur.execute("SELECT Password FROM Police_Login WHERE Police_ID = " + "'" + id + "'")
            ps = pass_cur.fetchall()
            Pass = ps[0][0]
            if passwd == Pass:
                return True
            else:
                Tk().withdraw()
                messagebox.askretrycancel("ERROR", "WORNG PASSWORD")
                return False
        else:
            Tk().withdraw()
            messagebox.askokcancel("Error", "veliya po da vadakkans")

if not os.path.exists("Databases/PoliceDB.db"):
    db = Databases()
    db.PoliceDB()
if not os.path.exists("Databases/CriminalDB.db"):
    db = Databases()
    db.CriminalDB()

#Globals
Names = []
IDs = []
PhNos = []

app = QApplication(sys.argv)
win = mainwindow()
win.show()
exit(app.exec_())