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

from database.database import Database

class Application(App):

    def build(self):
        navigationdrawer = NavigationDrawer()

        side_panel = BoxLayout(orientation='vertical')
        side_panel.add_widget(Label(text='Select Representation'))
        side_panel.add_widget(Button(text='Graphs'))
        navigationdrawer.add_widget(side_panel)

        main_panel = BoxLayout(orientation='vertical')

        main_panel.add_widget(Widget(size_hint_y=None, height=dp(4)))
        main_panel.add_widget(Widget(size_hint_y=None, height=dp(10)))
        navigationdrawer.add_widget(main_panel)

        def set_anim_type(name):
            navigationdrawer.anim_type = name
        modes_layout = BoxLayout(orientation='horizontal')

        #modes_layout.add_widget(Label(text='preset\nanims:'))
        #slide_an = Button(text='slide_\nabove_\nanim')
        #slide_an.bind(on_press=lambda j: set_anim_type('slide_above_anim'))
        #slide_sim = Button(text='slide \nabove \nsimple')
        #slide_sim.bind(on_press=lambda j: set_anim_type('slide_above_simple'))
        #fade_in_button = Button(text='fade_in')
        #fade_in_button.bind(on_press=lambda j: set_anim_type('fade_in'))
        #reveal_button = Button(text='reveal_\nbelow_\nanim')
        #reveal_button.bind(on_press=
                           #lambda j: set_anim_type('reveal_below_anim'))
        #slide_button = Button(text='reveal_\nbelow_\nsimple')
        #slide_button.bind(on_press=
        lambda j: set_anim_type('reveal_above_simple')
        #modes_layout.add_widget(slide_an)
        #modes_layout.add_widget(slide_sim)
        #modes_layout.add_widget(fade_in_button)
        #modes_layout.add_widget(reveal_button)
        #modes_layout.add_widget(slide_button)
        main_panel.add_widget(modes_layout)

        button = Button(text='toggle NavigationDrawer state (animate)',
                        size_hint_y=0.2)
        lambda j: set_anim_type('fade_in')
        button.bind(on_press=lambda j: navigationdrawer.toggle_state())
        button2 = Button(text='toggle NavigationDrawer state (jump)',
                         size_hint_y=0)
        button2.bind(on_press=lambda j: navigationdrawer.toggle_state(False))
        button3 = Button(text='toggle _main_above', size_hint_y=0.2)

        main_panel.add_widget(button)
        #main_panel.add_widget(button2)
        main_panel.add_widget(button3)

        return navigationdrawer


if __name__ == "__main__":
    Application().run()