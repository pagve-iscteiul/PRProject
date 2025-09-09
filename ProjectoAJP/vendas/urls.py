from django.conf.urls import url
from . import views

app_name = 'vendas'
urlpatterns = [url(r'^$', views.index, name='index'),

url(r'^Administrador/$', views.Administrador, name='Administrador'),
url(r'^pesquisa/$', views.pesquisa, name='pesquisa'),
url(r'^(?P<carro_id>[0-9]+)/FormularioCompra/$', views.FormularioCompra, name='FormularioCompra'),
url(r'^(?P<carro_id>[0-9]+)/pagamentoRemover/$', views.pagamentoRemover, name='pagamentoRemover'),
url(r'^StoqueCarro/$', views.StoqueCarro, name='StoqueCarro'),
url(r'^contact_us/$', views.contact_us, name='contact_us'),
url(r'^about_us/$', views.about_us, name='about_us'),
url(r'^how_to_buy/$', views.how_to_buy, name='how_to_buy'),
url(r'^quality/$', views.quality, name='quality'),
url(r'^spare_parts/$', views.spare_parts, name='spare_parts'),
url(r'^distributors/$', views.distributors, name='distributors'),
url(r'^loginview/$', views.loginview, name='loginview'),
url(r'^logoutview/$', views.logoutview, name='logoutview'),
url(r'^paginalogin/$', views.paginalogin, name='paginalogin'),
url(r'^envia_email/$', views.envia_email, name='envia_email'),
url(r'^adicionarCarro/$', views.adicionarCarro, name='adicionarCarro'),
url(r'^guardarCarro/$', views.guardarCarro, name='guardarCarro'),


url(r'^RemoverCarro/$', views.RemoverCarro, name='RemoverCarro'),
url(r'^apagarCarro/$', views.apagarCarro, name='apagarCarro'),
url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
url(r'^Carronexiste/$', views.Carronexiste, name='Carronexiste'),

url(r'^utilizador/$', views.utilizador, name='utilizador'),
url(r'^utilizadorAU/$', views.utilizadorAU, name='utilizadorAU'),
url(r'^InformacaoUtilizador/$', views.InformacaoUtilizador, name='InformacaoUtilizador'),
url(r'^guardarUtilizador/$', views.guardarUtilizador, name='guardarUtilizador'),
url(r'^paginaregisto/$', views.paginaregisto, name='paginaregisto'),
url(r'^(?P<cliente_id>[0-9]+)/alterar/$', views.alterar, name='alterar'),

url(r'^questao/$', views.questao, name='questao'),
url(r'^guardarQ/$', views.guardarQ, name='guardarQ'),
url(r'^(?P<questao_id>[0-9]+)/resposta/$', views.resposta, name='resposta'),
url(r'^passaPergResp/$', views.passaPergResp, name='passaPergResp'),

]
