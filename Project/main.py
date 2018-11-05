from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics','width','1280')
Config.set('graphics', 'height', '700')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
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
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Rectangle

import database.database as data

#from database.database import Database
Builder.load_string('''
<GraphSelect>:
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


class GraphSelect(BoxLayout):
    line = ObjectProperty(False)
    bar = ObjectProperty(False)
    pie = ObjectProperty(False)

global database
database = data.Database('database/csv/AnalyticsData_20181019174047.csv')

buildings = ['1', '2', '3', '4', '5', '6', '7']
totalnum = 0
for i in buildings:
    totalnum+=1
class Application(App):

    def build(self):

        tb_panel = TabbedPanel()
        #tb_panel.do_default_tab = False
        #building_content= FloatLayout()

        #th_interval_head = TabbedPanelHeader(text="Interval")
        #th_interval = FloatLayout()
        #th_interval.add_widget(date1)
        #date2=datepicker.DatePicker(size_hint = (0.1,0.1))
        #th_interval.add_widget(date2)

        #th_interval_head.content = th_interval

        #th_building_head = TabbedPanelHeader(text="Building")
        #th_building_head.content = building_content




        graph_content = FloatLayout()

        StartDate = Label(text='Start Date:', size_hint=(0.1, 0.1), pos_hint = {"x":0.2, "top": 1})
        graph_content.add_widget(StartDate)

        startmonth = TextInput(text='', multiline=False, pos_hint = {"x":1, "top":0.5}, hint_text="Month (MM)", input_filter='int')
        start_month_area= FloatLayout(size_hint = (0.1,0.05), pos_hint = {"x":0.19, "top":1})
        start_month_area.add_widget(startmonth)
        graph_content.add_widget(start_month_area)

        slashDate1 = Label(text='/', size_hint=(0.1, 0.1), pos_hint = {"x":0.35, "top":1})
        graph_content.add_widget(slashDate1)

        startday = TextInput(multiline=False, hint_text="Day (DD)",pos_hint = {"x":1, "top":0.5}, input_filter='float')
        start_day_area = FloatLayout(size_hint = (0.1,0.05), pos_hint = {"x":0.31, "top":1})
        start_day_area.add_widget(startday)
        graph_content.add_widget(start_day_area)

        slashDate2 = Label(text='/', size_hint=(0.1, 0.1), pos_hint = {"x":0.47, "top":1})
        graph_content.add_widget(slashDate2)

        startyear = TextInput(multiline=False, hint_text="Year (YYYY)", pos_hint = {"x":1, "top":0.5}, input_filter='float')
        start_year_area = FloatLayout(size_hint = (0.1,0.05), pos_hint = {"x":0.43, "top":1})
        start_year_area.add_widget(startyear)
        graph_content.add_widget(start_year_area)

        starthour = TextInput(multiline=False, hint_text="Hour (HH)", pos_hint = {"x":1, "top":0.5}, input_filter='float')
        start_hour_area = FloatLayout(size_hint = (0.1,0.05), pos_hint = {"x":0.6, "top":1})
        start_hour_area.add_widget(starthour)
        graph_content.add_widget(start_hour_area)

        colonDate1 = Label(text=':', size_hint=(0.1, 0.1), pos_hint = {"x":0.76, "top":1})
        graph_content.add_widget(colonDate1)

        startminute = TextInput(multiline=False, hint_text="Minutes (MM)",pos_hint = {"x":1, "top":0.5} , input_filter='float')
        start_minute_area = FloatLayout(size_hint = (0.1,0.05), pos_hint = {"x":0.72, "top":1})
        start_minute_area.add_widget(startminute)
        graph_content.add_widget(start_minute_area)

        bt3 = ToggleButton(text='AM', group='time1', size_hint=(0.05, 0.025), pos_hint = {"x":0.925, "top":0.974})
        graph_content.add_widget(bt3)
        bt4 = ToggleButton(text='PM', group='time1', size_hint=(0.05, 0.025), pos_hint = {"x":0.925, "top":0.95})
        graph_content.add_widget(bt4)




        EndDate = Label(text='End Date:', size_hint=(0.1, 0.1), pos_hint={"x": 0.2, "top": 0.9})
        graph_content.add_widget(EndDate)

        endmonth = TextInput(text='', multiline=False, pos_hint={"x": 1, "top": 0.5}, hint_text="Month (MM)",
                               input_filter='int')
        end_month_area = FloatLayout(size_hint=(0.1, 0.05), pos_hint={"x": 0.19, "top": 0.9})
        end_month_area.add_widget(endmonth)
        graph_content.add_widget(end_month_area)

        slashDate3 = Label(text='/', size_hint=(0.1, 0.1), pos_hint={"x": 0.35, "top": 1})
        graph_content.add_widget(slashDate3)

        endday = TextInput(multiline=False, hint_text="Day (DD)", pos_hint={"x": 1, "top": 0.5}, input_filter='float')
        end_day_area = FloatLayout(size_hint=(0.1, 0.05), pos_hint={"x": 0.31, "top": 0.9})
        end_day_area.add_widget(endday)
        graph_content.add_widget(end_day_area)

        slashDate4 = Label(text='/', size_hint=(0.1, 0.1), pos_hint={"x": 0.47, "top": 1})
        graph_content.add_widget(slashDate4)

        endyear = TextInput(multiline=False, hint_text="Year (YYYY)", pos_hint={"x": 1, "top": 0.5}, input_filter='float')
        end_year_area = FloatLayout(size_hint=(0.1, 0.05), pos_hint={"x": 0.43, "top": 0.9})
        end_year_area.add_widget(endyear)
        graph_content.add_widget(end_year_area)

        endhour = TextInput(multiline=False, hint_text="Hour (HH)", pos_hint={"x": 1, "top": 0.5}, input_filter='float')
        end_hour_area = FloatLayout(size_hint=(0.1, 0.05), pos_hint={"x": 0.6, "top": 0.9})
        end_hour_area.add_widget(endhour)
        graph_content.add_widget(end_hour_area)

        colonDate2 = Label(text=':', size_hint=(0.1, 0.1), pos_hint={"x": 0.76, "top": 0.9})
        graph_content.add_widget(colonDate2)

        endminute = TextInput(multiline=False, hint_text="Minutes (MM)", pos_hint={"x": 1, "top": 0.5},
                                input_filter='float')
        end_minute_area = FloatLayout(size_hint=(0.1, 0.05), pos_hint={"x": 0.72, "top": 0.9})
        end_minute_area.add_widget(endminute)
        graph_content.add_widget(end_minute_area)

        bt5 = ToggleButton(text='AM', group='time2', size_hint=(0.05, 0.025), pos_hint={"x": 0.925, "top": 0.874})
        graph_content.add_widget(bt5)
        bt6 = ToggleButton(text='PM', group='time2', size_hint=(0.05, 0.025), pos_hint={"x": 0.925, "top": 0.85})
        graph_content.add_widget(bt6)

        def ampmSET1(self):
            global ampm1
            ampm1 = "AM"

        def ampmSET2(self):
            global ampm1
            ampm1 = "PM"

        def ampmSET3(self):
            global ampm2
            ampm2 = "AM"

        def ampmSET4(self):
            global ampm2
            ampm2 = "PM"



        bt3.bind(on_press = ampmSET1)
        bt4.bind(on_press = ampmSET2)
        bt5.bind(on_press = ampmSET3)
        bt6.bind(on_press = ampmSET4)

        def buttonClicked(self):

            sMonth = int(startmonth.text)
            sDay = int(startday.text)
            sYear = int(startyear.text)

            sHour = int(starthour.text)
            sMin = int(startminute.text)

            eMonth = int(endmonth.text)
            eDay = int(endday.text)
            eYear = int(endyear.text)

            eHour = int(endhour.text)
            eMin = int(endminute.text)


            if sMonth > 12:
                sMonth = 12
            if sMonth < 0:
                sMonth = 0

            if sMonth in [4, 6, 9, 11]:
                if sDay > 30:
                    sDay = 30
            elif sMonth in [1, 3, 5, 7, 8, 10, 12]:
                if sDay > 31:
                    sDay = 31
            elif sMonth == 2:
                sDay = 28
            if sDay < 0:
                sDay = 0

            if sYear > 2020:
                sYear = 2020
            if sYear < 0:
                sYear = 0

            if sHour > 12:
                sHour = 12
            if sHour < 0:
                sHour = 0

            if sMin > 60:
                sMin = 60
            if sMin < 0:
                sMin = 0

            if eMonth in [4, 6, 9, 11]:
                if eDay > 30:
                    eDay = 30
            elif eMonth in [1, 3, 5, 7, 8, 10, 12]:
                if eDay > 31:
                    eDay = 31
            elif eDay == 2:
                eDay = 28
            if eDay < 0:
                eDay = 0

            if eYear > 2020:
                eYear = 2020
            if eYear < 0:
                eYear = 0

            if eHour > 12:
                eHour = 12
            if eHour < 0:
                eHour = 0

            if eMin > 60:
                eMin = 60
            if eMin < 0:
                eMin = 0

            startinterval = (" " + str(sMonth) + "/" + str(sDay) + "/" + str(sYear) + " " + str(sHour) + ":" + str(sMin) + ":" + "00 " + ampm1)
            endinterval = (" " + str(eMonth) + "/" + str(eDay) + "/" + str(eYear) + " " + str(eHour) + ":" + str(eMin) + ":" + "00 " + ampm2)

            database.SetInterval(startinterval, endinterval)
            database.ReadData()

            plt.gcf().clear()

            # Initialize graph after prospects
            # Loop for grabbing buildings and data points
            ticks = []
            labels = []
            for buildingNum in range(0, len(database.buildingsData)):
                timestamps = []
                kilowatts = []
                for dataPoint in range(0, len(database.buildingsData[buildingNum].dataPoints)):
                    timestamps.append(
                        database.SetDateToUnix(database.buildingsData[buildingNum].dataPoints[dataPoint].timestamp))
                    kilowatts.append(
                        float(database.buildingsData[buildingNum].dataPoints[dataPoint].kilowatts))
                plt.plot(timestamps, kilowatts, label=str(database.buildingsData[buildingNum].name))
                plt.xlabel('Timestamp')
                plt.ylabel('Kilowatts')
                plt.legend()

            tickNum = 8
            for x in range(0, tickNum):
                ticks.append((x * ((database.unixInterval[1] - database.unixInterval[0]) / tickNum) + database.unixInterval[0]))
                # print(self.ticks[x])#verifies the graph ticks
                labels.append(database.SetUnixToDate((x * ((database.unixInterval[1] - database.unixInterval[0]) / tickNum) + database.unixInterval[0])))
                # print(self.labels[x])#verifies the graph tick labels
            ticks.append(database.unixInterval[1])
            labels.append(database.SetUnixToDate(database.unixInterval[1]))
            plt.xticks(ticks=ticks, labels=labels, rotation=15)
            plt.title("Dynamic Kilowatt/hr Graph")

            graphwidget = FigureCanvasKivyAgg((plt.gcf()))
            graph_area = FloatLayout(size_hint=(0.75,0.8), pos_hint = {"left": 0, "top":0.9})
            graph_area.add_widget(graphwidget)
            graph_content.add_widget(graph_area)









        ok = Button(text="Graph", size_hint=(.2, .2 ), pos_hint = {"x":0, "top":1})
        ok.bind(on_press=buttonClicked)
        graph_content.add_widget(ok)


        buildingButtons = []
        def createButton(name, index):
            button = ToggleButton(text = name, size_hint = (0.25, 0.05), pos_hint = {"right":1, "y":0.05*index})
            button.bind(on_press = lambda x: (database.ChangeBuilding(index + 1)))
            graph_content.add_widget(button)
        for i, val in enumerate(database.buildings):
            createButton(val,i)






        #_lgraph_head = TabbedPanelHeader(text='Graphs')
        #th_lgraph_head.content = graph_content

        tb_panel.default_tab_content = graph_content

        tb_panel.default_tab_text = "Graphs"

        #tb_panel.add_widget(th_interval_head)
        #tb_panel.add_widget(th_building_head)
        #tb_panel.add_widget(th_lgraph_head)


        return tb_panel






if __name__ == "__main__":
    Application().run()
