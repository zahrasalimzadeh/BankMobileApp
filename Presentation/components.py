from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from Common.config import BACKGROUND, PRIMARY, SUBTITLE


def make_layout():
    return MDBoxLayout(orientation="vertical", padding=30, spacing=20, md_bg_color=BACKGROUND)


def make_label(text, height="30dp", color=SUBTITLE, font_style="Body1", halign="center"):
    return MDLabel(text=text, halign=halign, font_style=font_style, size_hint_y=None, height=height, theme_text_color="Custom", text_color=color)


def make_title(text, font_style="H4", height="48dp"):
    return MDLabel(text=text, halign="center", font_style=font_style, size_hint_y=None, height=height)


def make_button(text, callback, color=PRIMARY):
    button = MDCard(size_hint_y=None, height="56dp", radius=[14], md_bg_color=color, ripple_behavior=True, on_release=callback)
    button.add_widget(MDLabel(text=text, halign="center"))
    return button