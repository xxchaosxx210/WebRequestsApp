# Web Request App
# coded by Paul Millar

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import mainthread

import requests
import threading

def http_handler(*args, **kwargs):
    url = kwargs["url"]
    container = kwargs["container"]
    response = requests.get(url)
    if "text/html" in response.headers["Content-Type"]:
        container.on_http_response(response.text)
    response.close()

class Container(BoxLayout):
    
    @mainthread
    def on_http_response(self, html):
        self.ids.response_text_input.text = html
    
    def on_fetch_release(self):
        threading.Thread(target=http_handler, kwargs={
            "url": self.ids.fetch_text_input.text,
            "container": self
        }).run()

class MainApp(App):
    pass

def main():
    MainApp().run()
    
if __name__ == '__main__':
    main()