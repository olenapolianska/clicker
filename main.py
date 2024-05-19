from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def __init__(self,**kw):
        super().__init__(**kw)
    def click(self):
        self.ids.ball.size_hint = (1, 1)
    def unclick(self):
        self.ids.ball.size_hint = (0.5, 0.5)

class MenuScreen(Screen):
    def __init__(self,**kw):
        super().__init__(**kw)

    def click(self):
        self.ids.start.on_press = self.on_main_screen

    def on_main_screen(self, *args):
        self.manager.current = "main"

class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

class MenuApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        return sm

app = MenuApp()
app.run()

