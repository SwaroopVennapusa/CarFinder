"""
File: ui_imagedialog.py
Author: Sai Swaroop Reddy V
Date Created: 15th November 2023
Last Modified: 3rd December 2023
Version: 4.0

Description:
    This script is designed to perform web scraping tasks based on user inputs from a graphical user interface (GUI).
    The GUI allows users to select various options to specify their scraping criteria. Upon receiving the user's choices,
    the script dynamically constructs a query, sends a request to the target website, and then parses the received data.
    The scraped information is neatly formatted and displayed back to the user through the UI's dialog box. This tool
    is particularly focused on extracting data from automotive website, providing a user-friendly way to gather
    information about vehicles based on specified parameters such as body style, powertrain, engine type, and price range.
"""

from PyQt6 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1053, 659)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.label_5.setObjectName("label_5")
        self.powertrain = QtWidgets.QComboBox(parent=self.centralwidget)
        self.powertrain.setGeometry(QtCore.QRect(540, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.powertrain.setFont(font)
        self.powertrain.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.powertrain.setObjectName("powertrain")
        self.powertrain.addItem("")
        self.powertrain.addItem("")
        self.powertrain.addItem("")
        self.type = QtWidgets.QComboBox(parent=self.centralwidget)
        self.type.setGeometry(QtCore.QRect(540, 70, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.type.setFont(font)
        self.type.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.engine = QtWidgets.QComboBox(parent=self.centralwidget)
        self.engine.setGeometry(QtCore.QRect(540, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.engine.setFont(font)
        self.engine.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.engine.setObjectName("engine")
        self.engine.addItem("")
        self.engine.addItem("")
        self.engine.addItem("")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.label_2.setObjectName("label_2")
        self.find_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.find_btn.setGeometry(QtCore.QRect(430, 200, 151, 28))

        self.find_btn.clicked.connect(self.do_search)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.find_btn.setFont(font)
        self.find_btn.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.find_btn.setObjectName("find_btn")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(540, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 250, 991, 381))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setOpenExternalLinks(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Price"))
        self.label_5.setText(_translate("MainWindow", "Engine"))
        self.powertrain.setItemText(0, _translate("MainWindow", "FWD"))
        self.powertrain.setItemText(1, _translate("MainWindow", "RWD"))
        self.powertrain.setItemText(2, _translate("MainWindow", "AWD"))
        self.type.setItemText(0, _translate("MainWindow", "Sedan"))
        self.type.setItemText(1, _translate("MainWindow", "Hatchback"))
        self.type.setItemText(2, _translate("MainWindow", "SUV"))
        self.engine.setItemText(0, _translate("MainWindow", "Gasoline"))
        self.engine.setItemText(1, _translate("MainWindow", "Hybrid"))
        self.engine.setItemText(2, _translate("MainWindow", "Electric"))
        self.label_2.setText(_translate("MainWindow", "Power train"))
        self.find_btn.setText(_translate("MainWindow", "Find vehicle"))
        self.label_4.setText(_translate("MainWindow", "Type"))
        self.comboBox.setItemText(0, _translate("MainWindow", "$30000-$35000"))
        self.comboBox.setItemText(1, _translate("MainWindow", "$35000-$40000"))
        self.comboBox.setItemText(2, _translate("MainWindow", "$40000-$45000"))
        self.comboBox.setItemText(3, _translate("MainWindow", "$45000-$50000"))
        self.comboBox.setItemText(4, _translate("MainWindow", "$50000-$55000"))
        self.comboBox.setItemText(5, _translate("MainWindow", "$60000-$65000"))
        self.comboBox.setItemText(6, _translate("MainWindow", "$65000-$70000"))

    def do_search(self):
        # Clearing the text browser for new search results
        self.textBrowser.clear()

        # Constructing the base URL for the search
        base_url = "https://www.cars.com/shopping/results/?body_style_slugs[]="
        body_style = self.type.currentText().lower()
        base_url += body_style + "&dealer_id=&drivetrain_slugs[]="

        # Matching powertrain options and updating the URL
        powertrain_map = {
            "AWD": "all_wheel_drive",
            "FWD": "front_wheel_drive",
            "RWD": "rear_wheel_drive"
        }
        powertrain = powertrain_map.get(self.powertrain.currentText())
        base_url += powertrain + "&fuel_slugs[]=" + self.engine.currentText().lower() + "&keyword=&list_price_max="

        # Handling price range selection and updating the URL
        price_range_map = {
            "$30000-$35000": 30000,
            "$35000-$40000": 35000,
            "$40000-$45000": 40000,
            "$45000-$50000": 45000,
            "$50000-$55000": 50000,
            "$55000-$60000": 55000,
            "$60000-$65000": 60000,
            "$65000-$70000": 65000
        }
        price_min = price_range_map.get(self.comboBox.currentText())
        price_max = price_min + 5000
        base_url += f"{price_max}&list_price_min={price_min}&makes[]=&maximum_distance=all&mileage_max=&page="

        # Iterating through pages of search results
        page_number = 1
        search_url = base_url + str(page_number) + "&page_size=100&sort=best_match_desc&stock_type=used&year_max=&year_min=&zip="

        # Making a request to the URL and parsing the response
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting and calculating the total count of entries
        count_text = soup.find('span', class_='total-entries').text
        total_count = int(''.join(filter(str.isdigit, count_text))) / 100
        print(total_count)

        # Finding all vehicle details and adding them to the text browser
        vehicle_list = soup.findAll('div', class_='vehicle-details')
        for vehicle in vehicle_list:
            link = 'https://www.cars.com' + vehicle.find('a')['href'].strip()
            name = vehicle.find('h2', class_='title').text
            price = vehicle.find('span', class_='primary-price').text
            display_text = f'<a href="{link}">{name}---{price}</a>'
            self.textBrowser.append(display_text)
