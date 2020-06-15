import os                      

import kivy 
kivy.require('1.11.1')

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock 
from kivy.uix.popup import Popup 

import time                     
import json                      
import threading                
import ast                      
import configparser             
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
import re

# Constants
config = configparser.ConfigParser()
config.read("./config.ini")

APPTITLE            = config["GUIConstants"]["APPTITLE"]
class MainScreen(RelativeLayout):        
    """ Description: 
            This is the applications controller. It will contain the core functionality of the 
            application.  
    """    
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.store = {}

        
    def updateSettings(self, taskName, value, active):
        """ Updates the controller settings  """        
        # Update all other values in current combination    
        self.store[taskName] = value 
        self.updateProgressBar()  
        self.displayOutput("Updating setting")

            
    def handleSpinnerValues(self, taskName, value):
        """ Updates the settings on dropdown values """        
        self.updateProgressBar()
        self.displayOutput("Updating spinner values")      
    
        
    def updateOtherSettings(self,*args): 
        """ Updates Global settings """
        for elem in args: 
            print(elem)
        
    def startTask(self):
        """ Main call that starts a task """        
        #self.thread = threading.Thread(target=startThread, args=())  
        self.displayOutput("Starting Server Thread")
        self.thread.start() 
        
    def onTaskCompletion(self): 
        """ After each task is completed it increments progress bar."""       
        self.count = self.autoBar.value + 1        
        self.autoBar.value = self.count       
        self.displayOutput(f"Finished task")  
   
    
    def updateProgressBar(self):
        """ Updates the combinations progress bar """
        #self.progressBar.value = self.updateProgressBar.value + 1  
        pass
 
    
    def displayOutput(self, msg=None):
        """ Displays information unto app screen """      
        self.outputWidget.text = msg
            
    def saveCommandPrompt(self, outputWidget):
        """ Saves the output widget to later update information """
        self.outputWidget = outputWidget 
        return "" 
        
def startThread(*threadArgs):
    """ Generic method used to start thread"""
    threadArgs[1].execute(threadArgs[0], threadArgs[0].params,threadArgs[2])
           
class FeederUserInterfaceApp(App):   
    main = ObjectProperty(MainScreen())    
    def build(self):
        """ Required kivy method that starts application """
        self.title = APPTITLE

           
if __name__ =='__main__':
    FeederUserInterfaceApp().run()
