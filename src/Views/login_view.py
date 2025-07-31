from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

# Esta clase representa la pantalla de login
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # Layout vertical para colocar los elementos en columna
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=50)

        # Campo de texto para el usuario
        self.username = MDTextField(
            hint_text="Nombre de usuario",
            size_hint_x=None,
            width=300,
            pos_hint={"center_x": 0.5}
        )

        # Campo de texto para la contraseña
        self.password = MDTextField(
            hint_text="Contraseña",
            password=True,
            size_hint_x=None,
            width=300,
            pos_hint={"center_x": 0.5}
        )

        # Botón de iniciar sesión
        login_button = MDRaisedButton(
            text="Iniciar Sesión",
            pos_hint={"center_x": 0.5},
            on_release=self.on_login
        )

        # Botón para ir al registro
        register_button = MDRaisedButton(
            text="Registrarse",
            pos_hint={"center_x": 0.5},
            on_release=self.go_to_register
        )

        # Agregamos los widgets al layout
        layout.add_widget(MDLabel(text="Bienvenido a ControlCash", halign="center", theme_text_color="Primary"))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_button)
        layout.add_widget(register_button)

        # Agregamos el layout a la pantalla
        self.add_widget(layout)

    def on_login(self, instance):
        # Aquí puedes validar el login
        print(f"Intentando iniciar sesión como: {self.username.text}")

    def go_to_register(self, instance):
        # Cambia a la pantalla de registro
        self.manager.current = 'register'
#