from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

# Importamos las pantallas (vistas)
from src.Views.login_view import LoginScreen
from src.Views.registro_view import RegisterScreen
from src.Views.Home import HomeScreen


# Clase principal de la aplicación
class ControlCashApp(MDApp):
    def build(self):
        # Creamos el manejador de pantallas
        sm = ScreenManager()

        # Añadimos cada pantalla con un nombre único
        sm.add_widget(LoginScreen(name='login'))       # Login -> 'login'
        sm.add_widget(RegisterScreen(name='register')) # Registro -> 'register'
        #sm.add_widget(HomeScreen(name='home'))
        # Retornamos el screen manager como raíz
        return sm

# Ejecutamos la app
if __name__ == '__main__':
    ControlCashApp().run()
