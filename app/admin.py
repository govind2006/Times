from django.contrib import admin

# Register your models here.
from .models import today_stories
from .models import current_news
from .models import state
from .models import latestnews
from .models import editorial
from .models import weeklyspecial
from .models import otherimportantlink
from .models import AdvertiseTariffPlan
from .models import International
from .models import Buisness
from .models import Sport
from .models import National
from .models import opinion_editorial
from .models import column_editorial
from .models import letter_editorial
from .models import sunday_magazine_top_stories
from .models import Bollywood_Buzz
from .models import Personality
from .models import Health
from .models import Career_Education
from .models import Society
from .models import Book_Review
from .models import Fashion
from .models import Heritage
from .models import Science_Technology,Art_Culture,photo_gallery,Magazine_photo



admin.site.register(Magazine_photo)
admin.site.register(photo_gallery)
admin.site.register(Art_Culture)
admin.site.register(Science_Technology)
admin.site.register(Heritage)
admin.site.register(Fashion)
admin.site.register(Book_Review)
admin.site.register(Society)
admin.site.register(Career_Education)
admin.site.register(Health)
admin.site.register(Personality)
admin.site.register(Bollywood_Buzz)
admin.site.register(sunday_magazine_top_stories)
admin.site.register(column_editorial)
admin.site.register(letter_editorial)
admin.site.register(opinion_editorial)
admin.site.register(National)
admin.site.register(Sport)
admin.site.register(Buisness)
admin.site.register(International)
admin.site.register(AdvertiseTariffPlan)
admin.site.register(otherimportantlink)
admin.site.register(weeklyspecial)
admin.site.register(editorial)
admin.site.register(latestnews)
admin.site.register(current_news)
admin.site.register(today_stories)
admin.site.register(state)