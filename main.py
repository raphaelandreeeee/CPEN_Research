from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, ThreeLineListItem
from kivy.properties import ObjectProperty
from kivy.lang import Builder


class Dashboard(Screen):

    pass


class TapAttend(MDApp):

    def build(self):
        return Dashboard()
    

if __name__ == '__main__':

    TapAttend().run()

