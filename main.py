from winotify import Notification
import random
from win32com.client import Dispatch
from QuotesText import quoteList
import datetime

quote = random.choice(quoteList)
speak=Dispatch("SAPI.SpVoice")

class Speaker:
    def __init__(self, time: int) -> None:
        self.time = time
    
    def wish(self) -> str:
        if self.time >= 6 and self.time < 12:
            self.greeting="Good Morning Samit"

        elif self.time >= 12 and self.time <= 16:
            self.greeting="Good Afternoon Samit"

        elif self.time > 16 and self.time < 20:
            self.greeting="Good Evening Samit"

        elif self.time >= 20 and self.time <= 23:
            self.greeting="Good Night Samit"
        else:
            self.greeting="Good night"
        return self.greeting

toast = Notification(app_id="windows app", title="Winotify Test Toast", msg="New Notification!")
spkr = Speaker(int(datetime.datetime.now().time().hour))
speak.Speak(spkr.wish())
toast.show()