from django.shortcuts import render
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
# Create your views here.
def index(request):
    national = National.objects.all()
    sport = Sport.objects.all()
    buisness = Buisness.objects.all()
    international = International.objects.all()
    advertise = AdvertiseTariffPlan.objects.all()
    otherlink = otherimportantlink.objects.all()
    weekly = weeklyspecial.objects.all()
    eds = editorial.objects.all()
    lnews = latestnews.objects.all()
    states = state.objects.all()
    dest = current_news.objects.all()
    dests = today_stories.objects.all()

    k = {'dests':dests,'lnews':lnews,'dest':dest,'states':states,'eds':eds,'weekly':weekly,
        'advertise':advertise,'international':international,'buisness':buisness,'sport':sport,
        'national':national,'otherlink':otherlink}

    return render(request,'index.html',k)


def bstate(request):
    bstate = state.objects.all()
    return render(request,'state.html',{'bstate':bstate})



def bnational(request):
    m = National.objects.all()
    return render(request,'national.html',{'m':m})


def buisness(request):
    m = Buisness.objects.all()
    return render(request,'buisness.html',{'m':m})

from .models import opinion_editorial
from .models import column_editorial
from .models import letter_editorial
def opinion(request):
    ce = column_editorial.objects.all()
    le = letter_editorial.objects.all()
    eds = editorial.objects.all()
    m = opinion_editorial.objects.all()
    k = {'eds':eds,'m':m,'le':le,'ce':ce}
    return render(request,'opinion.html',k)


def sport(request):
    m = Sport.objects.all()
    return render(request,'sport.html',{'m':m})

def international(request):
    m = International.objects.all()
    return render(request,'international.html',{'m':m})


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
def sunday_magazine(request):
    ac = Art_Culture.objects.all()
    st = Science_Technology.objects.all()
    hr = Heritage.objects.all()
    f = Fashion.objects.all()
    br = Book_Review.objects.all()
    so = Society.objects.all()
    ce = Career_Education.objects.all()
    h = Health.objects.all()
    B = Bollywood_Buzz.objects.all()
    m = sunday_magazine_top_stories.objects.all()
    p = Personality.objects.all()
    k = {'m':m,'B':B,'p':p,'h':h,'ce':ce,'so':so,'br':br,'f':f,'hr':hr,'st':st,'ac':ac}
    return render(request,'sundaymagazine.html',k)

def gallery(request):
    mp = Magazine_photo.objects.all()
    pg = photo_gallery.objects.all()
    m = {'pg':pg,'mp':mp}
    return render(request,'gallery.html',m)