from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics','width','1280')
Config.set('graphics', 'height', '700')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.properties import ObjectProperty
from kivy.lang import Builder


#Format for time interval MM/DD/YYYY HH:MM:SS AM/PM. No leading zeroes

#from database.database import Database
Builder.load_string('''
<MyWidget>:
    orientation: "vertical"
    padding: 0
    spacing: 3
    BoxLayout:
        orientation: "horizontal"
        Label:
            text: "Type of Graph:"
            color: 1, 1, 1, 1
            size_hint_x: 
            
    Label:
        text: "Line Graph"
        color: 1, 1, 1, 1
        size_hint_x: .15
    CheckBox:
        group: "graph_type"
        value: root.line
        size_hint_x: .15

    Label:
        text: "Bar Graph"
        color: 1, 1, 1, 1
        size_hint_x: .15
    CheckBox:
        group: "graph_type"
        value: root.bar
        size_hint_x: .15

    Label:
        text: "Pie Graph"
        color: 1, 1, 1, 1
        size_hint_x: .15
    CheckBox:
        group: "graph_type"
        value: root.pie
        size_hint_x: .15



''')


class MyWidget(BoxLayout):
    line = ObjectProperty(False)
    bar = ObjectProperty(False)
    pie = ObjectProperty(False)


class Application(App):

    def build(self):
        button_b = 0.1
        button_h = 0


        tb_panel = TabbedPanel()

        building_content= BoxLayout(orientation = "vertical")
        building_content.add_widget(Label(text="end me"))
        building_content.add_widget(Label(text="nah b u good"))



        th_interval_head = TabbedPanelHeader(text='Interval')
        th_interval_head.content = Label(text='interval code here')

        th_building_head = TabbedPanelHeader(text="Building")
        th_building_head.content = building_content

        th_lgraph_head = TabbedPanelHeader(text='Graphs')
        th_lgraph_head.content = MyWidget()

        tb_panel.default_tab_text = "Home"

        tb_panel.add_widget(th_interval_head)
        tb_panel.add_widget(th_building_head)
        tb_panel.add_widget(th_lgraph_head)

        return tb_panel






if __name__ == "__main__":
    Application().run()
