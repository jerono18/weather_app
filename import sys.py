import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,QPushButton,QLabel,QLineEdit)

from PyQt5.QtCore  import Qt
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel("Enter a city name:",self)
        self.city_input=QLineEdit(self)
        self.get_weather_button=QPushButton("Get Weather", self)
        self.temperature_Label=QLabel("70F" ,self)
        self.description_Label=QLabel("sunny",self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Weather App")
        
        vbox=QVBoxLayout()
        
        vbox.addWidget(self.city_Label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addwidget(self.temperature_Label)
        vbox.addWidget(self.emoji_Label)
        vbox.addWidget(self.description_Label)
        
        self.setLayout(vbox)
        
         


        self.city_Label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperture_Label.setAlignment(Qt.AlignCenter)
        self.emoji_Label.setAlignment(Qt.AlignCenter)
        self.description_Label.setAlignment(Qt.AlignCenter)




        self.city_Label.setObjectName("city_Label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_Label.setObjectName("temperure_Label")
        self.emoji_Label.setObjectName("emoji_Label")
        self.description_Label.setObjectName("description_Label")

        self.setStyleSheet("""
        QLabel,QPushButton{
        font-family:calibri;
        }
        Qlabel#city_Label{
            font-size:40px;
            font-style:italic;
        }
        QLineEdit#city_input{
            font-size:30px;
            font-weight:bold;
        }
        QLabel#temperture_Label{
            font-size:75;
        }
        QLabel#emoji_Label{
            font-size: 100px
            font-family:Segoe UI emoji; 
        } 
        QLabel#description_Label{
            font-size: 100px;
        }       
      """)




if __name__=="__main__":
    app=QApplication(sys.argv)
    weather_app=WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())