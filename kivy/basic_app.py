"""
Step 0.
Import the parts of kivy that you will be using.
This is preferential to importing the entire package!
In this example we will only be using App and Label.
"""
from kivy.app import App
from kivy.uix.label import Label


"""
Step 1.
Create a new class that inherits from the kivy App class.
"""
class MyApp(App):

    """
    Step 2.
    Implement the build() method of the class.
    The method should return a Widget instance.
    Label is an example of a Widget!
    """
    def build(self):
        return Label(text='This is a basic example.')

"""
Step 3.
This is the part of the file that runs automatically when the file is executed.
Here, all that it does is start the app running.
"""
if __name__ == '__main__':
    MyApp().run()
