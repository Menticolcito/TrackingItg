from django.conf.urls import patterns, include, url
from django.contrib import admin
from Mapa.views import recorrido, posicion, getFrey, getDonLucho, getKronos, getBahaireII, getMara, getApolo, getOdin, getColombia, getMexico, getPeru, getMapa, getBoreas, getEosii, getAlisios, getCapidahl, getMistral, getSaga, getTitania, getChinook, getSirocco, getAquavit, getCarex, getVali, getTanok, getSeatrout, getKin, getBarupacifico, getBaruInti , getCristina

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TrackingItg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', getMapa),
    (r'^boreas$', getBoreas),
    (r'^odin$', getOdin),
    (r'^frey$', getFrey),
    (r'^colombia$', getColombia),
    (r'^mexico$', getMexico),
    (r'^eosii$', getEosii),
    (r'^alisios$', getAlisios),
    (r'^donlucho$', getDonLucho),
    (r'^capidahl$', getCapidahl),
    (r'^mistral$', getMistral),
    (r'^cristina$', getCristina),
    (r'^tanok$', getTanok),
    (r'^seatrout$', getSeatrout),
    (r'^kin$', getKin),
    (r'^saga$', getSaga),
    (r'^titania$', getTitania),
    (r'^apolo$', getApolo),
    (r'^mara$', getMara),
    (r'^vali$', getVali),
    (r'^carex$', getCarex),
    (r'^aquavit$', getAquavit),
    (r'^chinook$', getChinook),
    (r'^bahaireii$', getBahaireII),
    (r'^kronos$', getKronos),
    (r'^sirocco$', getSirocco),
    (r'^barupacifico$', getBarupacifico),
    (r'^baruinti$', getBaruInti),
    (r'^peru$', getPeru),
    (r'^posicion$', posicion),
    (r'^recorrido$', recorrido),


    url(r'^admin/', include(admin.site.urls)),
)
