from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

# Esta clase representa la pantalla de registro
class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)

        # Layout vertical para organizar los campos
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=50)

        # Campo para el nuevo nombre de usuario
        self.new_username = MDTextField(
            hint_text="Nuevo usuario",
            size_hint_x=None,
            width=300,
            pos_hint={"center_x": 0.5}
        )

        # Campo para la nueva contraseña
        self.new_password = MDTextField(
            hint_text="Nueva contraseña",
            password=True,
            size_hint_x=None,
            width=300,
            pos_hint={"center_x": 0.5}
        )

        # Botón para registrarse
        register_button = MDRaisedButton(
            text="Registrar",
            pos_hint={"center_x": 0.5},
            on_release=self.on_register
        )

        # Botón para volver al login
        back_button = MDRaisedButton(
            text="Volver al Login",
            pos_hint={"center_x": 0.5},
            on_release=self.go_to_login
        )

        # Agregamos los widgets al layout
        layout.add_widget(MDLabel(text="Crear una cuenta nueva", halign="center", theme_text_color="Primary"))
        layout.add_widget(self.new_username)
        layout.add_widget(self.new_password)
        layout.add_widget(register_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def on_register(self, instance):
        # Aquí puedes registrar el usuario
        print(f"Usuario registrado: {self.new_username.text}")

    def go_to_login(self, instance):
        # Regresar a la pantalla de login
        self.manager.current = 'login'
