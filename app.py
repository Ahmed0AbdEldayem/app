from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from twilio.rest import Client

account_sid = 'AC633a7b6d31298d083881f5918e490616'
auth_token = '8ab8cb9b1410d116ff2204fd76f5771e'
client = Client(account_sid, auth_token)

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 6
        self.add_widget(Label(text='SMS Message: '))
        self.sms = TextInput()
        self.add_widget(self.sms)
        self.submit = Button(text="Send SMS")
        self.submit.bind(on_press=self.sendsms)
        self.add_widget(self.submit)
        self.add_widget(Label(text='Call Message: '))
        self.call = TextInput()
        self.add_widget(self.call)
        self.submit2 = Button(text='Send Call')
        self.submit2.bind(on_press=self.sendcall)
        self.add_widget(self.submit2)

    def sendsms(self, needed):
        message = self.sms.text
        text = client.messages.create(
            to= '',
            from_= '',
            body=message)
        print('Message sent successfully.')

    def sendcall(self, weeded):
        voice_message = self.call.text
        client.calls.create(
            record=True,
            to= '',
            from_= '',
            twiml='<Response><Say>{}</Say></Response>'.format(voice_message))
        print('Call made successfully.')





class MyApp(App):
    def build(self):
        return MyGridLayout()

MyApp().run()
