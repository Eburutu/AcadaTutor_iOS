import kivy
import kivymd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import webbrowser
from kivy.utils import get_color_from_hex
from pyobjus import autoclass
from kivy.base import EventLoop
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import RoundedRectangle, Color


Builder.load_file('screens/background.kv')
# Builder.load_file('screens/home_page.kv')
Builder.load_file('screens/welcome_page.kv')

class BackgroundWidget(BoxLayout):
    pass


class AdmobBanner(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ads = autoclass('adSwitch').alloc().init()
        # self.ads.show_ads()

    def on_start(self):
        self.ads.show_ads()

    # def show_banner(self):
    #     self.ads.show_ads()

    # def hide_banner(self):
    #     self.ads.hide_ads()

    def on_pause(self):
        self.ads.hide_ads()

    def on_resume(self):
        self.ads.show_ads()



class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.5, 0.608, 0.83, 0.1)  # White color for the background  0.5, 0.608, 0.83, 0.1
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20, 20, 20, 20])

    def on_size(self, instance, value):
        self.rect.size = value

    def on_pos(self, instance, value):
        self.rect.pos = value



class ImageButton2(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0, 0, 1)  # White color for the background  0.5, 0.608, 0.83, 0.1
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20, 20, 20, 20])

    def on_size(self, instance, value):
        self.rect.size = value

    def on_pos(self, instance, value):
        self.rect.pos = value


class ImageButton3(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.4, 0.508, 0.33, 0)  # White color for the background  0.5, 0.608, 0.83, 0.1
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20, 20, 20, 20])

    def on_size(self, instance, value):
        self.rect.size = value

    def on_pos(self, instance, value):
        self.rect.pos = value


class ImageButton4(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0, 0, 1)  # White color for the background  0.5, 0.608, 0.83, 0.1
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20, 20, 20, 20])

    def on_size(self, instance, value):
        self.rect.size = value

    def on_pos(self, instance, value):
        self.rect.pos = value


class ImageButton5(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(1, 1, 1, 1)  # White color for the background  0.5, 0.608, 0.83, 0.1
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20, 20, 20, 20])

    def on_size(self, instance, value):
        self.rect.size = value

    def on_pos(self, instance, value):
        self.rect.pos = value



class RoundedButton(Button):
    # pass
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.zoom_animation = None

    def start_zoom_animation(self):
        zoom_in_animation = Animation(
            width=320, height=(48), t="out_quad", duration=2.5
        )
        zoom_out_animation = Animation(
            width=(300), height=(38), t="out_quad", duration=2.5
        )

        def start_next_animation(animation, widget):
            if animation == zoom_in_animation:
                self.zoom_animation = zoom_out_animation
                self.zoom_animation.start(self)
            else:
                self.zoom_animation = zoom_in_animation
                self.zoom_animation.start(self)

        zoom_in_animation.bind(on_complete=start_next_animation)
        zoom_out_animation.bind(on_complete=start_next_animation)

        self.zoom_animation = zoom_in_animation
        self.zoom_animation.start(self)


class EnglishPage(Screen):
    def show_interstitial_and_go_back(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'welcome_page'


    def goto_welcome_page(self):
        # self.manager.current = 'home_page'
        self.manager.current = 'welcome_page'
        # self.show_interstitial_and_go_back()


    def show_interstitial_and_goto_home_page(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'home_page'

    def goto_home_page(self):
        self.show_interstitial_and_goto_home_page()



    def open_web_for_intro_EduBot(self):
        link_url = 'https://humanchat.net/6yBhnQHPBqDd'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url) 


    def show_interstitial_and_goto_EduBot_intro(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()
        # Navigate back to the home page
        self.open_web_for_intro_EduBot()

    def goto_Edubot(self):
        self.show_interstitial_and_goto_EduBot_intro()


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)



class FrenchPage(Screen):
    def show_interstitial_and_go_back(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'welcome_page'


    def goto_welcome_page(self):
        # self.manager.current = 'home_page'
        self.manager.current = 'welcome_page'
        # self.show_interstitial_and_go_back()


    def show_interstitial_and_goto_home_page(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'home_page'

    def goto_home_page(self):
        self.show_interstitial_and_goto_home_page()



    def open_web_for_intro_EduBot(self):
        link_url = 'https://humanchat.net/6yBhnQHPBqDd'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url) 


    def show_interstitial_and_goto_EduBot_intro(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.open_web_for_intro_EduBot()

    def goto_Edubot(self):
        self.show_interstitial_and_goto_EduBot_intro()


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)



class SpanishPage(Screen):
    def show_interstitial_and_go_back(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'welcome_page'


    def goto_welcome_page(self):
        # self.manager.current = 'home_page'
        self.manager.current = 'welcome_page'
        # self.show_interstitial_and_go_back()


    def show_interstitial_and_goto_home_page(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'home_page'

    def goto_home_page(self):
        self.show_interstitial_and_goto_home_page()



    def open_web_for_intro_EduBot(self):
        link_url = 'https://humanchat.net/6yBhnQHPBqDd'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url) 


    def show_interstitial_and_goto_EduBot_intro(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.open_web_for_intro_EduBot()

    def goto_Edubot(self):
        self.show_interstitial_and_goto_EduBot_intro()


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)


class PortuguesePage(Screen):
    def show_interstitial_and_go_back(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'welcome_page'


    def goto_welcome_page(self):
        # self.manager.current = 'home_page'
        self.manager.current = 'welcome_page'
        # self.show_interstitial_and_go_back()


    def show_interstitial_and_goto_home_page(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'home_page'

    def goto_home_page(self):
        self.show_interstitial_and_goto_home_page()



    def open_web_for_intro_EduBot(self):
        link_url = 'https://humanchat.net/6yBhnQHPBqDd'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url) 


    def show_interstitial_and_goto_EduBot_intro(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.open_web_for_intro_EduBot()

    def goto_Edubot(self):
        self.show_interstitial_and_goto_EduBot_intro()


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)


class RussianPage(Screen):
    def show_interstitial_and_go_back(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'welcome_page'


    def goto_welcome_page(self):
        # self.manager.current = 'home_page'
        self.manager.current = 'welcome_page'
        # self.show_interstitial_and_go_back()


    def show_interstitial_and_goto_home_page(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'home_page'

    def goto_home_page(self):
        self.show_interstitial_and_goto_home_page()



    def open_web_for_intro_EduBot(self):
        link_url = 'https://humanchat.net/6yBhnQHPBqDd'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url) 


    def show_interstitial_and_goto_EduBot_intro(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.open_web_for_intro_EduBot()

    def goto_Edubot(self):
        self.show_interstitial_and_goto_EduBot_intro()


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)


class ItalianPage(Screen):
    def show_interstitial_and_go_back(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'welcome_page'


    def goto_welcome_page(self):
        # self.manager.current = 'home_page'
        self.manager.current = 'welcome_page'
        # self.show_interstitial_and_go_back()


    def show_interstitial_and_goto_home_page(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'home_page'

    def goto_home_page(self):
        self.show_interstitial_and_goto_home_page()



    def open_web_for_intro_EduBot(self):
        link_url = 'https://humanchat.net/6yBhnQHPBqDd'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url) 


    def show_interstitial_and_goto_EduBot_intro(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.open_web_for_intro_EduBot()

    def goto_Edubot(self):
        self.show_interstitial_and_goto_EduBot_intro()


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)


class HindiPage(Screen):
    def show_interstitial_and_go_back(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'welcome_page'


    def goto_welcome_page(self):
        # self.manager.current = 'home_page'
        self.manager.current = 'welcome_page'
        # self.show_interstitial_and_go_back()


    def show_interstitial_and_goto_home_page(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'home_page'

    def goto_home_page(self):
        self.show_interstitial_and_goto_home_page()



    def open_web_for_intro_EduBot(self):
        link_url = 'https://humanchat.net/6yBhnQHPBqDd'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url) 


    def show_interstitial_and_goto_EduBot_intro(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.open_web_for_intro_EduBot()

    def goto_Edubot(self):
        self.show_interstitial_and_goto_EduBot_intro()


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)


class GermanPage(Screen):
    def show_interstitial_and_go_back(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'welcome_page'


    def goto_welcome_page(self):
        # self.manager.current = 'home_page'
        self.manager.current = 'welcome_page'
        # self.show_interstitial_and_go_back()


    def show_interstitial_and_goto_home_page(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'home_page'

    def goto_home_page(self):
        self.show_interstitial_and_goto_home_page()



    def open_web_for_intro_EduBot(self):
        link_url = 'https://humanchat.net/6yBhnQHPBqDd'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url) 


    def show_interstitial_and_goto_EduBot_intro(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.open_web_for_intro_EduBot()

    def goto_Edubot(self):
        self.show_interstitial_and_goto_EduBot_intro()


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)


class ChinesePage(Screen):
    def show_interstitial_and_go_back(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'welcome_page'


    def goto_welcome_page(self):
        # self.manager.current = 'home_page'
        self.manager.current = 'welcome_page'
        # self.show_interstitial_and_go_back()


    def show_interstitial_and_goto_home_page(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'home_page'

    def goto_home_page(self):
        self.show_interstitial_and_goto_home_page()



    def open_web_for_intro_EduBot(self):
        link_url = 'https://humanchat.net/6yBhnQHPBqDd'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url) 


    def show_interstitial_and_goto_EduBot_intro(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.open_web_for_intro_EduBot()

    def goto_Edubot(self):
        self.show_interstitial_and_goto_EduBot_intro()


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)




class JapanesePage(Screen):
    def show_interstitial_and_go_back(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'welcome_page'


    def goto_welcome_page(self):
        # self.manager.current = 'home_page'
        self.manager.current = 'welcome_page'
        # self.show_interstitial_and_go_back()


    def show_interstitial_and_goto_home_page(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'home_page'

    def goto_home_page(self):
        self.show_interstitial_and_goto_home_page()



    def open_web_for_intro_EduBot(self):
        link_url = 'https://humanchat.net/6yBhnQHPBqDd'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url) 


    def show_interstitial_and_goto_EduBot_intro(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.open_web_for_intro_EduBot()

    def goto_Edubot(self):
        self.show_interstitial_and_goto_EduBot_intro()


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)


class ArabicPage(Screen):
    def show_interstitial_and_go_back(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'welcome_page'


    def goto_welcome_page(self):
        # self.manager.current = 'home_page'
        self.manager.current = 'welcome_page'
        # self.show_interstitial_and_go_back()


    def show_interstitial_and_goto_home_page(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'home_page'

    def goto_home_page(self):
        self.show_interstitial_and_goto_home_page()



    def open_web_for_intro_EduBot(self):
        link_url = 'https://humanchat.net/6yBhnQHPBqDd'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url) 


    def show_interstitial_and_goto_EduBot_intro(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.open_web_for_intro_EduBot()

    def goto_Edubot(self):
        self.show_interstitial_and_goto_EduBot_intro()


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)



class CustomDropDownItem(ButtonBehavior, BoxLayout):
    def __init__(self, text, image_source, image_source2, spacing=10, welcome_page=None, **kwargs):
        super(CustomDropDownItem, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.welcome_page = welcome_page

        # Create an Image widget
        self.image = Image(source=image_source, size=(120, 70))

        # Create a Label widget
        # self.label = Label(text=text, size_hint_x=0.5, width=250, padding=(5, 0), font_name="ChineseFont")
        self.label_image = Image(source=image_source2, size=(120, 70))

        self.spacing = spacing

        # Add the widgets to the custom item
        self.add_widget(self.image)
        self.add_widget(self.label_image)
        self.text = text
        
        self.bind(on_release=self.on_item_click)


    def on_item_click(self, instance):
        # Handle the item click here
        # You can access the selected item's properties using self.image and self.label_image
        # print(f"Selected: {self.image.source} - {self.label_image.source}")
        Determine = self.image.source
        selected_part1 = Determine.split("/")[1]
        selected_part2 = selected_part1.split(".")[0]

        print(selected_part2)

        if self.welcome_page:
            self.welcome_page.on_dropdown_select(self, self.text)



class WelcomePage(Screen):
    def on_dropdown_select(self, instance, value):
        # Handle the selected item here
        print(f"Selected: {value}")

        global value_p
        value_p = value

        if value == "English":
            self.manager.current = "English"

        elif value == "French":
            self.manager.current = "French"

        elif value == "Spanish":
            self.manager.current = "Spanish"

        elif value == "German":
            self.manager.current = "German"

        elif value == "Portuguese":
            self.manager.current = "Portuguese"

        elif value == "Russian":
            self.manager.current = "Russian"

        elif value == "Japanese":
            self.manager.current = "Japanese"

        elif value == "Hindi":
            self.manager.current = "Hindi"

        elif value == "Chinese":
            self.manager.current = "Chinese"

        elif value == "Italian":
            self.manager.current = "Italian"

        elif value == "Arabic":
            self.manager.current = "Arabic"

    def on_pre_enter(self):
        self.ids.zoom_button.start_zoom_animation()

    def open_dropdown(self, button):
        dropdown = DropDown()
    

        # Add custom items to the dropdown
        items = [("English", "flags/English_write.png", "flags/English.png"),
                 ("Space", "flags/Space.png", "flags/Space.png"), 
                 ("French", "flags/French_write.png", "flags/French.png"), 
                 ("Space", "flags/Space.png", "flags/Space.png"), 
                 ("Spanish" ,"flags/Spanish_write.png", "flags/Spanish.png"), 
                 ("Space", "flags/Space.png", "flags/Space.png"), 
                 ("Chinese", "flags/Chinese_write.png", "flags/Chinese.png"), 
                 ("Space", "flags/Space.png", "flags/Space.png"),
                ("Arabic", "flags/Arabic_write.png", "flags/Arabic.png"),
                 ("Space", "flags/Space.png", "flags/Space.png"), 
                 ("Portuguese", "flags/Portuguese_write.png", "flags/Portuguese.png"), 
                 ("Space", "flags/Space.png", "flags/Space.png"), 
                 ("Russian", "flags/Russian_write.png", "flags/Russian.png"), 
                 ("Space", "flags/Space.png", "flags/Space.png"), 
                 ("Hindi", "flags/Hindi_write.png", "flags/Hindi.png"), 
                 ("Space", "flags/Space.png", "flags/Space.png"), 
                 ("Japanese", "flags/Japanese_write.png", "flags/Japanese.png"), 
                 ("Space", "flags/Space.png", "flags/Space.png"), 
                 ("German", "flags/German_write.png", "flags/German.png"),
                 ("Space", "flags/Space.png", "flags/Space.png"),
                 ("Italian", "flags/Italian_write.png", "flags/Italian.png"),
                 ]

        for text, image_text, image_source in items:
            item = CustomDropDownItem(text= text, image_source=image_source, image_source2=image_text, size_hint_y=None, height=55, welcome_page=self)
            item.bind(on_release=lambda instance, x=text: dropdown.select(x))
            dropdown.add_widget(item)

        # Open the dropdown relative to the button
        dropdown.open(button)


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)




class IntroPage(Screen):
    pass


class HomePage(Screen):

    def open_web_browser_for_Edubot(self):
        # Get the URL from the link reference
        link_url = 'https://core3.m4k.co/m/103595/p/1256125#widget_container_2175921'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url)  

    def show_interstitial_and_go_to_Edubot(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        self.open_web_browser_for_Edubot()
        # self.manager.current = 'academicMaterial_HighSchool_Tertiary'

    def goto_Edubot(self):
        self.show_interstitial_and_go_to_Edubot()
        #     self.manager.previous_screen = 'home_page' #############################################
        #     self.manager.current = 'chatbotHighSchool_page'

        # def goto_chatbotTertiarySchool_page(self):
        #     self.manager.current = 'chatbotTertiarySchool_page'





    def open_web_browser_for_Academic(self):
        # Get the URL from the link reference
        link_url = 'https://core3.m4k.co/m/103595/p/1256231#widget_container_2176048'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url)  

    def show_interstitial_and_go_to_Academic(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        self.open_web_browser_for_Academic()
        # self.manager.current = 'academicMaterial_HighSchool_Tertiary'


    def goto_Academic_4_HighSchool_Tertiary(self):
        # self.manager.current = 'academicMaterial_HighSchool_Tertiary'
        self.show_interstitial_and_go_to_Academic()



    

    # JS
    def open_web_browser_for_JS(self):
        # Get the URL from the link reference
        link_url = 'https://core3.m4k.co/m/103595/p/1256285#widget_container_2176093'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url)   

    def show_interstitial_and_go_to_S_Js(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        self.open_web_browser_for_JS()
    #     self.manager.current = 'scholarship_job_search'

    def goto_scholarship_job_search(self):
        self.show_interstitial_and_go_to_S_Js()



    def show_interstitial_and_go_back(self):
        # Show the interstitial ad
        App.get_running_app().interstitial_ad.InterstitialView()

        # Navigate back to the home page
        self.manager.current = 'English'


    def goto_intro_page(self):
        # self.manager.current = 'home_page'
        value = value_p
        # print(value)
        self.manager.current = value
        # self.show_interstitial_and_go_back()



    def open_web_browser_for_Private(self):
        # Get the URL from the link reference
        link_url = 'https://core3.m4k.co/m/103595/p/1256127'

        # Define the action when the link is clicked
        # For example, open the URL in a web browser        
        import webbrowser
        webbrowser.open(link_url)   


    def on_enter(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)

    def on_start(self):
        # Create an AdmobBanner instance and show the banner ad
        admob_banner = AdmobBanner(size_hint=(1, None), height=120)
        self.ids.banner_layout.add_widget(admob_banner)

        

class AcadaMobileApp(MDApp):

    def build(self):

        self.interstitial_ad = autoclass("adInterstitial").alloc().init()

        admob_banner = AdmobBanner(size_hint=(1, None), height= 170)  # Adjust height as needed


        layout = BackgroundWidget(orientation="vertical")

        kv_directory = 'screens'
        Builder.load_file(f'{kv_directory}/welcome_page.kv')
        Builder.load_file(f'{kv_directory}/home_page.kv')
        Builder.load_file(f'{kv_directory}/intro_page.kv')
        Builder.load_file(f'{kv_directory}/English.kv')
        Builder.load_file(f'{kv_directory}/French.kv')
        Builder.load_file(f'{kv_directory}/Spanish.kv')
        Builder.load_file(f'{kv_directory}/German.kv')
        Builder.load_file(f'{kv_directory}/Portuguese.kv')
        Builder.load_file(f'{kv_directory}/Italian.kv')
        Builder.load_file(f'{kv_directory}/Chinese.kv')
        Builder.load_file(f'{kv_directory}/Hindi.kv')
        Builder.load_file(f'{kv_directory}/Russian.kv')
        Builder.load_file(f'{kv_directory}/Arabic.kv')
        Builder.load_file(f'{kv_directory}/Japanese.kv')


        self.sm = ScreenManager() 
        self.sm.add_widget(WelcomePage(name='welcome_page'))
        self.sm.add_widget(HomePage(name='home_page'))
        self.sm.add_widget(IntroPage(name='intro_page'))
        self.sm.add_widget(EnglishPage(name='English'))
        self.sm.add_widget(FrenchPage(name='French'))
        self.sm.add_widget(SpanishPage(name='Spanish'))
        self.sm.add_widget(GermanPage(name='German'))
        self.sm.add_widget(PortuguesePage(name='Portuguese'))
        self.sm.add_widget(ItalianPage(name='Italian'))
        self.sm.add_widget(ChinesePage(name='Chinese'))
        self.sm.add_widget(HindiPage(name='Hindi'))
        self.sm.add_widget(RussianPage(name='Russian'))
        self.sm.add_widget(ArabicPage(name='Arabic'))
        self.sm.add_widget(JapanesePage(name='Japanese'))
        


        self.sm.set_back_button_handler(self.handle_back_button)  

        layout.add_widget(admob_banner)
        layout.add_widget(self.sm)

        return layout
    

if __name__ == '__main__':
    EventLoop.ensure_window()
    AcadaMobileApp().run()

