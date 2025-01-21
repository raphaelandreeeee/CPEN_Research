from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import MDList, TwoLineIconListItem, IconLeftWidget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from db_handler import DatabaseHandler
from my_heap import MinHeapQ


KV = """
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"

<HomeScreen>
    canvas:
        Color:
            rgba: 234, 239, 189, 0
        Rectangle:
            pos: self.pos
            size: self.size

    MDRoundFlatButton:
        text: "Go to Class"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_press:
            root.screen_manager.current = "CPEN"

<StudentListView>
            
MDNavigationLayout:

    MDScreenManager:
        id: screen_manager

        HomeScreen:
            name: "Home Screen"
            screen_manager: screen_manager

            MDLabel:
                text: f"[color=#002500][font=RobotoBlack]Tap[/font][font=RobotoMedium]Attend[/font]"
                markup: True
                font_style: "H2"
                pos_hint: {'center_x': 0.5, 'top': 0.8}
                adaptive_size: True

        MDScreen:
            name: "CPEN"

            MDTopAppBar:
                pos_hint: {"center_x": 0.5, "top": 1}
                elevation: 0
                md_bg_color: "C9E3AC"
                specific_text_color: "37371F"
                left_action_items:
                    [['menu', lambda x: nav_drawer.set_state("open")]]

            MDTextField:
                id: scan_id_input
                size_hint_x: None
                width: 900
                pos_hint: {"center_x": 0.5, "top": 0.9}
                hint_text: "Scan ID"
                helper_text: "or type ID"
                icon_left: "account"

            MDRectangleFlatButton:
                size_hint_x: None
                width: 300
                pos_hint: {"center_x": 0.35, "top": 0.8}
                text: "Scan ID"
                on_press:
                    app.search_student_instance()

            MDRectangleFlatButton:
                size_hint_x: None
                width: 300
                pos_hint: {"center_x": 0.65, "top": 0.8}
                text: "Show All"
                on_press:
                    app.append_student()

            MDIconButton:
                size_hint_x: None
                width: 300
                pos_hint: {"center_x": 0.9, "top": 0.8}
                icon: "delete"
                on_press:
                    app.clear_list()

            StudentListView:
                id: studentview        
                pos_hint: {"center_x": 0.5, "top": 0.7}
                size_hint_x: 0.9

        MDScreen:
            name: "Add Student"

            MDTopAppBar:
                title: "Add Student"
                pos_hint: {"center_x": 0.5, "top": 1}
                elevation: 0
                md_bg_color: "C9E3AC"
                specific_text_color: "37371F"
                left_action_items:
                    [['menu', lambda x: nav_drawer.set_state("open")]]

            MDTextField:
                id: add_id_input
                size_hint_x: None
                width: 900
                pos_hint: {"center_x": 0.5, "top": 0.9}
                hint_text: "Student ID"

            MDTextField:
                id: add_class_name
                size_hint_x: None
                width: 900
                pos_hint: {"center_x": 0.5, "top": 0.8}
                hint_text: "Class Name"

            MDTextField:
                id: add_first_name
                size_hint_x: None
                width: 900
                pos_hint: {"center_x": 0.5, "top": 0.7}
                hint_text: "First Name"

            MDTextField:
                id: add_last_name
                size_hint_x: None
                width: 900
                pos_hint: {"center_x": 0.5, "top": 0.6}
                hint_text: "Last Name"
            
            MDRectangleFlatButton:
                size_hint_x: None
                width: 300
                pos_hint: {"center_x": 0.5, "top": 0.5}
                text: "Add Student"
                on_press:
                    app.add_student_instance()

        MDScreen:
            name: "Edit Student"

            MDTopAppBar:
                title: "Edit Student"
                pos_hint: {"center_x": 0.5, "top": 1}
                elevation: 0
                md_bg_color: "C9E3AC"
                specific_text_color: "37371F"
                left_action_items:
                    [['menu', lambda x: nav_drawer.set_state("open")]]

            MDTextField:
                id: edit_id_input
                size_hint_x: None
                width: 900
                pos_hint: {"center_x": 0.5, "top": 0.9}
                hint_text: "Student ID"

            MDTextField:
                id: edit_class_name
                size_hint_x: None
                width: 900
                pos_hint: {"center_x": 0.5, "top": 0.8}
                hint_text: "Class Name"

            MDTextField:
                id: edit_first_name
                size_hint_x: None
                width: 900
                pos_hint: {"center_x": 0.5, "top": 0.7}
                hint_text: "First Name"

            MDTextField:
                id: edit_last_name
                size_hint_x: None
                width: 900
                pos_hint: {"center_x": 0.5, "top": 0.8}
                hint_text: "Last Name"
            
            MDTextField:
                id: edit_attendance
                size_hint_x: None
                width: 900
                pos_hint: {"center_x": 0.5, "top": 0.7}
                hint_text: "Attendance"

            MDRectangleFlatButton:
                size_hint_x: None
                width: 300
                pos_hint: {"center_x": 0.5, "top": 0.6}
                text: "Edit Student"
                on_press:
                    app.edit_student_instance()
        
        MDScreen:
            name: "Remove Student"

            MDTopAppBar:
                title: "Remove Student"
                pos_hint: {"center_x": 0.5, "top": 1}
                elevation: 0
                md_bg_color: "C9E3AC"
                specific_text_color: "37371F"
                left_action_items:
                    [['menu', lambda x: nav_drawer.set_state("open")]]

            MDTextField:
                id: remove_id_input
                size_hint_x: None
                width: 900
                pos_hint: {"center_x": 0.5, "top": 0.9}
                hint_text: "Student ID"

            MDTextField:
                id: remove_class_name
                size_hint_x: None
                width: 900
                pos_hint: {"center_x": 0.5, "top": 0.8}
                hint_text: "Class Name"

            MDRectangleFlatButton:
                size_hint_x: None
                width: 300
                pos_hint: {"center_x": 0.5, "top": 0.7}
                text: "Remove Student"
                on_press:
                    app.remove_student_instance()
        
    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 16, 16, 0)

        MDNavigationDrawerMenu:

            MDNavigationDrawerHeader:
                title: "TapAttend"
                title_color: "#4a4939"
                spacing: "4dp"
                padding: "12dp", 0, 0, "56dp"

            DrawerClickableItem:
                icon: "home"
                text: "Home"
                on_press:
                    nav_drawer.set_state("close")
                    root._screen_manager.current = "Home Screen"

            MDNavigationDrawerDivider:

            DrawerClickableItem:
                icon: "plus"
                text: "Add Student"
                on_press:
                    nav_drawer.set_state("close")
                    root._screen_manager.current = "Add Student"

            DrawerClickableItem:
                icon: "pencil"
                text: "Edit Student"
                on_press:
                    nav_drawer.set_state("close")
                    root._screen_manager.current = "Edit Student"

            DrawerClickableItem:
                icon: "delete"
                text: "Remove Student"
                on_press:
                    nav_drawer.set_state("close")
                    root._screen_manager.current = "Remove Student"

"""


class HomeScreen(Screen):
    screen_manager = ObjectProperty()


class StudentListView(MDList):
    pass


class TapAttend(MDApp):

    dialog = None
    id_input = ObjectProperty()

    heapq = MinHeapQ()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__database = DatabaseHandler()
        self.__database.create_class("CPEN")

    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)
    
    def add_student_instance(self):
        student_id = self.root.ids.add_id_input.text
        class_name = self.root.ids.add_class_name.text
        first_name = self.root.ids.add_first_name.text
        last_name = self.root.ids.add_last_name.text

        self.__database.add_student(first_name, last_name, student_id, class_name)  

        self.root.ids.add_id_input.text = ""
        self.root.ids.add_class_name.text = ""
        self.root.ids.add_first_name.text = ""
        self.root.ids.add_last_name.text = ""     
    
    def edit_student_instance(self):
        student_id = self.root.ids.edit_id_input.text
        class_name = self.root.ids.edit_class_name.text
        first_name = self.root.ids.edit_first_name.text
        last_name = self.root.ids.edit_last_name.text
        attendance = self.root.ids.edit_attendance.text

        self.__database.edit_student(student_id, class_name, new_id_number=None, new_first_name=first_name, new_last_name=last_name, new_attendance=attendance)

        self.root.ids.edit_id_input.text = ""
        self.root.ids.edit_class_name.text = ""
        self.root.ids.edit_first_name.text = ""
        self.root.ids.edit_last_name.text = ""     
        self.root.ids.edit_attendance.text = ""     

    def remove_student_instance(self):
        student_id = self.root.ids.remove_id_input.text
        class_name = self.root.ids.remove_class_name.text

        if not self.dialog:
            self.dialog = MDDialog(
                text="Confirm action?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color, 
                        on_release=self.dialog_close
                    ),
                    MDFlatButton(
                        text="CONFIRM",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color, 
                        on_release=self.dialog_close
                    )
                ]
            )
        self.dialog.open()

        self.__database.remove_student(student_id, class_name)

        self.root.ids.remove_id_input.text = ""
        self.root.ids.remove_class_name.text = ""

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)

    def search_student_instance(self):
        student_id = self.root.ids.scan_id_input.text

        student = self.__database.search_student(student_id, self.root._screen_manager.current)

        if student is not None:
            self.heapq.insert(student)
            self.__database.increment_student_attendance(student[-1], self.root._screen_manager.current)
        
        self.root.ids.scan_id_input.text = ""

    def append_student(self):
        for _ in range(len(self.heapq)):

            student = self.heapq.delete()
            attendance, first_name, last_name, student_id = student

            name = f"{first_name} {last_name}"

            current = self.root._screen_manager.current
            
            self.root.ids.studentview.add_widget(
                TwoLineIconListItem(
                    IconLeftWidget(
                        icon="account"
                    ), 
                    text=name,
                    secondary_text=str(attendance),
                )
            )

    def clear_list(self):
        self.root.ids.studentview.clear_widgets()

if __name__ == '__main__':

    TapAttend().run()

