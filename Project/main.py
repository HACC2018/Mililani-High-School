from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics','width','1280')
Config.set('graphics', 'height', '700')
from kivy.app import App
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.metrics import dp

from kivy.garden.navigationdrawer import NavigationDrawer

#from database.database import Database

class Application(App):

    def build(self):
        navigationdrawer = NavigationDrawer()

        side_panel = BoxLayout(orientation='vertical')
        side_panel.add_widget(Label(text='Select Representation'))
        side_panel.add_widget(Button(text='Graphs'))
        navigationdrawer.add_widget(side_panel)

        main_panel = BoxLayout(orientation='vertical')

        navigationdrawer.add_widget(main_panel)

        modes_layout = BoxLayout(orientation='horizontal')

        main_panel.add_widget(modes_layout)



        navigationdrawer.toggle_state(True)
        def show_drawer(toggle):
            if toggle == 1:
                navigationdrawer.toggle_state(True)
        button = Button(text= "show", background_color = (1,2,2,1), size_hint = (0.1,0.1), pos_hint = {'top': 5})
        button.bind(on_press = lambda j: show_drawer(1))
        main_panel.add_widget(button)
        return navigationdrawer


if __name__ == "__main__":
    Application().run()
