from winotify import Notification
import random
from win32com.client import Dispatch
from QuotesText import quoteList

quote = random.choice(quoteList)
speak=Dispatch("SAPI.SpVoice")

toast = Notification(app_id="windows app", title="Winotify Test Toast", msg="New Notification!")

toast.show()