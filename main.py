import kivy

kivy.require("1.11.1")  # Set to your Kivy version
from kivy.app import App
from kivy.uix.textinput import TextInput
import psycopg2


class MyApp(App):
    dbname = "test"
    user = "postgres"

    def build(self):
        self.log_text = TextInput(multiline=True, text="Starting\n")
        self.log_text.insert_text("Hello World!")
        return self.log_text

    def start_psycopg(self):
        connection_str = f"dbname={self.dbname} user={self.user}"
        self.conn = psycopg2.connect(connection_str)
        self.log_text.insert_text(f"Connected to database: {connection_str} %s\n")


if __name__ == "__main__":
    MyApp().run()
