"""
File: main.py
Author: Sai Swaroop Reddy V
Date Created: 15th November 2023
Last Modified: 3rd December 2023
Version: 4.0

Description:
    This is the main entry point of the AutoFinder application. It initializes and displays the main window
    of the application using the Ui_MainWindow class from the ui_imagedialog module. The application provides
    a graphical user interface for users to specify criteria for web scraping and displays the results
    in a dialog box.

Notes:
    Ensure that all dependencies, PyQt6, Python (preferably the latest version), BeautifulSoup and requests, are properly installed and updated for optimal performance.
"""

import sys
from PyQt6.QtWidgets import QDialog, QApplication
from ui_imagedialog import Ui_MainWindow

# Initialize the QApplication
app = QApplication(sys.argv)

# Create and set up the main window
window = QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)

# Display the main window
window.show()

# Execute the application's main loop
sys.exit(app.exec())
