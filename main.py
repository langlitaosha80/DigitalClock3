"""
Digital Clock - Android App
A customizable digital clock with always-on-top feature
"""

import kivy
kivy.require('2.2.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.properties import ListProperty, NumericProperty
from kivy.graphics import Color, Rectangle
from datetime import datetime

# Color presets
COLORS = {
    'white': (1, 1, 1, 1),
    'black': (0, 0, 0, 1),
    'red': (1, 0, 0, 1),
    'green': (0, 1, 0, 1),
    'blue': (0, 0.5, 1, 1),
    'yellow': (1, 1, 0, 1),
}


class ClockLabel(Label):
    """Custom label with background color support"""
    bg_color = ListProperty([0, 0, 0, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.bg_color)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def set_bg_color(self, color):
        self.bg_color = color


class DigitalClockApp(App):
    # Background color property
    bg_color = ListProperty([0, 0, 0, 1])
    # Text color property
    text_color = ListProperty([1, 1, 1, 1])
    # Pin state
    is_pinned = False

    def build(self):
        # Main layout
        main_layout = BoxLayout(
            orientation='vertical',
            padding=20
        )

        # Clock container with background
        self.clock_container = BoxLayout(
            size_hint=(1, 1),
        )
        with self.clock_container.canvas.before:
            Color(*self.bg_color)
            self.bg_rect = Rectangle(size=self.clock_container.size, pos=self.clock_container.pos)

        self.clock_container.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        # Clock label
        self.clock_label = ClockLabel(
            text='00:00:00',
            font_size='80sp',
            bold=True,
            color=self.text_color,
            halign='center',
            valign='middle',
            bg_color=self.bg_color
        )
        self.clock_container.add_widget(self.clock_label)
        main_layout.add_widget(self.clock_container)

        # Settings button
        settings_btn = Button(
            text='设置',
            size_hint=(1, None),
            height='50dp',
            on_press=self.show_settings
        )
        main_layout.add_widget(settings_btn)

        # Start clock updates
        Clock.schedule_interval(self.update_time, 1)
        self.update_time(None)

        return main_layout

    def _update_bg_rect(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def update_time(self, dt):
        """Update the clock display with current time"""
        now = datetime.now()
        time_str = now.strftime('%H:%M:%S')
        self.clock_label.text = time_str

    def update_bg_color(self, color):
        """Update background color"""
        self.bg_color = color
        self.bg_rect.rgba = color

    def update_text_color(self, color):
        """Update text color"""
        self.text_color = color
        self.clock_label.color = color
        self.clock_label.set_bg_color(color)

    def show_settings(self, instance):
        """Show settings popup"""
        content = GridLayout(cols=2, padding=10, spacing=10)

        # Always on top toggle
        self.pin_btn = Button(
            text='关闭置顶',
            on_press=self.toggle_pin
        )
        content.add_widget(Label(text='置顶模式:'))
        content.add_widget(self.pin_btn)

        # Background color selector
        content.add_widget(Label(text='背景色:'))
        bg_colors_layout = BoxLayout(size_hint_y=None, height='50dp')
        for color_name, color_value in COLORS.items():
            btn = Button(
                text=color_name[:1].upper(),
                background_color=color_value,
                on_press=lambda x, c=color_value: self.set_bg_color(c)
            )
            bg_colors_layout.add_widget(btn)
        content.add_widget(bg_colors_layout)

        # Text color selector
        content.add_widget(Label(text='文字色:'))
        text_colors_layout = BoxLayout(size_hint_y=None, height='50dp')
        for color_name, color_value in COLORS.items():
            btn = Button(
                text=color_name[:1].upper(),
                background_color=color_value,
                on_press=lambda x, c=color_value: self.set_text_color(c)
            )
            text_colors_layout.add_widget(btn)
        content.add_widget(text_colors_layout)

        # Close button
        close_btn = Button(
            text='关闭',
            size_hint_y=None,
            height='50dp',
            on_press=lambda x: popup.dismiss()
        )
        content.add_widget(close_btn)
        content.add_widget(Label())

        popup = Popup(
            title='设置',
            content=content,
            size_hint=(0.8, 0.6)
        )
        popup.open()

    def toggle_pin(self, instance):
        """Toggle always-on-top mode"""
        self.is_pinned = not self.is_pinned

        if self.is_pinned:
            self.pin_btn.text = '开启置顶'
            # Request system alert window permission on Android
            try:
                from android import api21
                api21.request_alert_window_permission()
            except Exception:
                pass
        else:
            self.pin_btn.text = '关闭置顶'

    def set_bg_color(self, color):
        """Set background color"""
        self.update_bg_color(color)

    def set_text_color(self, color):
        """Set text color"""
        self.update_text_color(color)


if __name__ == '__main__':
    DigitalClockApp().run()
