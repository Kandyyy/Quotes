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
            self.greeting="Good Morning"

        elif self.time >= 12 and self.time <= 16:
            self.greeting="Good Afternoon"

        elif self.time > 16 and self.time < 20:
            self.greeting="Good Evening"

        elif self.time >= 20 and self.time <= 23:
            self.greeting="Good Night"
        else:
            self.greeting="Good night"
        return self.greeting

spkr = Speaker(int(datetime.datetime.now().time().hour))
toast = Notification(app_id=spkr.wish(), title="The wise words of " + quote["author"], msg=quote["text"],icon=r"E:\VScode\Python\Notifier\sunIcon.ico")
speak.Speak(spkr.wish() + "Samit")
toast.show()