import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,QPushButton,QLabel,QLineEdit)

from PyQt5.QtCore  import Qt
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_Label=QLabel("Enter a city name:",self)
        self.city_input=QLineEdit(self)
        self.get_weather_button=QPushButton("Get Weather", self)
        self.temperature_Label=QLabel (self)
        self.description_Label=QLabel(self)
        self.emoji_Label=QLabel(self)
        self.initUI()




    def initUI(self):
        self.setWindowTitle("Weather App")
        
        vbox=QVBoxLayout()
        
        vbox.addWidget(self.city_Label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_Label)
        vbox.addWidget(self.emoji_Label)
        vbox.addWidget(self.description_Label)
        
        self.setLayout(vbox)
        
         


        self.city_Label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_Label.setAlignment(Qt.AlignCenter)
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
            font-size: 50px;
        }       
      """)
        self.get_weather_button.clicked.connect(self.get_weather)
    def get_weather(self):
        api_key="14ffff94b52fa9d5bf06386220d1f82d"
        city= self.city_input.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()

            if data["cod"] ==200:
                self.display_weather(data)
        except requests.exceptions.HTTPError:
            match response.status_code:


                case 400:
                     print("Bad request\nplease check your input")
                case 401:
                     print("Unauthorized\nInvalid API key")
                case 403:
                      print("Forbidden\nAccess is denied")
                case 404: 
                    print("Not found\ncity not found")   
                case 500: 
                     print("Internal server\nPlease try again later") 
                case 502:
                    print("Bad get Gateway\nInvalid resopnse from the server")
                case 503:
                    print("Service not available\nServer is down")
                case 504:
                    print("Bad request\nNo response from the server")
                case _:
                    print(f"HTTP errror occured\nhttp_error")


        except requests.exceptions.ConnectionError:
            print("Connection error\ncheck your internet connection")
        except requests.exceptions.Timeout:
            print("Time out error\nThe request timed out")
        except requests.exceptions.RequestException:
            print("TooManyRedirects\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            print(f"Request Error:\n{req_error}")
       
    def display_error(self,message):
        self.temperature_Label.setStyleSheet("font-size:30px;")
        self.temperature_Label.setText(message)
        self.description_Label()
    def display_weather(self,data):
        self.temperature_Label.setStyleSheet("font-size:30px;")
        temperature_k=data["main"]["temp"]
        temperature_c=temperature_k-273.15
        temperature_f=(temperature_k*9/5)-459.67
        weather_id=data["weather"][0]["id"]
        weather_description=data["weather"][0]["description"]

        
        self.temperature_Label.setText(f"{temperature_f}F")
        self.emoji_Label.setText(self.get_weather_emoji(weather_id))
        self.description_Label.setText(weather_description)
    @staticmethod
    def get_weather_emoji(weather_id):

        if 200<= weather_id<=232:
            return "🌧" 
            
        elif 300<=weather_id<=321:
            return"🌧"
        elif 500<=weather_id<=531:
            return"🌧"
        elif 600<=weather_id<=622:
            return"❄"
        elif 701<=weather_id<=741:
            return"🌫"
        elif weather_id==762:
            return"🌋" 
        elif weather_id==771:
            return"💨"
        elif weather_id==781:
            return"🌬"
        elif weather_id==800:
            return"☀"
        elif 801<=weather_id<=804:
            return"☁"
        else:
            return""
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    weather_app=WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())