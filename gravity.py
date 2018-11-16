
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

print ("hello!")

class player(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos



class GravityApp(App):

    def build(self):
        rocket = player()
        #Clock.schedule_interval(game.update, 1.0 / 60.0)


if __name__ == '__main__':

    GravityApp().run();