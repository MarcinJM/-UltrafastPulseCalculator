from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# so we can easliy import numpad into the main file
Builder.load_file('simulation_settings.kv')


class SliderWithMultipliers(BoxLayout):
    slider_name = StringProperty('')
    value_string = StringProperty('')
    button1_name = StringProperty('')
    button2_name = StringProperty('')    
    silder_range = ObjectProperty()
    slider_step = NumericProperty()

    def __init__(self,**args):
        self.bind(value = self.set_value_string)

    def set_value_string(self,instancce,value):
        self.value_string = num2str(self.value)
        
 
    def set_button1_multiplier(self):
        pass

    def set_button2_multiplier(self):
        pass
    
    
  

class SimulationSettings(BoxLayout):
    pass
   

class SimulationSettingsApp(App):
    def build(self):
        return SimulationSettings()
        
     
if __name__ == '__main__':  
    SimulationSettingsApp().run()
