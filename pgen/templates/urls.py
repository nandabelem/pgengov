from django.conf.urls import url, include
from . import views


urlpatterns = [


	##### Categoria URL's #####

	url(r'^pgen/categoria/novo/$', views.categoria_new, name='categoria_new'),
	url(r'^pgen/categoria_cadastradas/$', views.categoria_list, name='categoria_list'),
	url(r'^pgen/categoria/(?P<pk>\d+)/edit/$', views.categoria_edit, name='categoria_edit'),
	url(r'^pgen/categoria/(?P<pk>\d+)/remove/$', views.categoria_remove, name='categoria_remove'),

	##### Instituição URL's #####

	url(r'^pgen/instituicao/novo/$', views.instituicao_new, name='instituicao_new'),
	url(r'^pgen/instituicoes_cadastradas/$', views.instituicao_list, name='instituicao_list'),
	url(r'^pgen/instituicao/(?P<pk>\d+)/edit/$', views.instituicao_edit, name='instituicao_edit'),
	url(r'^pgen/instituicao/(?P<pk>\d+)/remove/$', views.instituicao_remove, name='instituicao_remove'),

	##### Estado URL's #####

	url(r'^pgen/estado/novo/$', views.estado_new, name='estado_new'),
	url(r'^pgen/estados_cadastrados/$', views.estado_list, name='estado_list'),
	url(r'^pgen/estado/(?P<pk>\d+)/edit/$', views.estado_edit, name='estado_edit'),
	url(r'^pgen/estado/(?P<pk>\d+)/remove/$', views.estado_remove, name='estado_remove'),

	##### Cidade URL's #####

	url(r'^pgen/cidade/novo/$', views.cidade_new, name='cidade_new'),
	url(r'^pgen/cidades_cadastradas/$', views.cidade_list, name='cidade_list'),
	url(r'^pgen/cidade/(?P<pk>\d+)/edit/$', views.cidade_edit, name='estado_edit'),
	url(r'^pgen/cidade/(?P<pk>\d+)/remove/$', views.cidade_remove, name='cidade_remove'),
	
	##### Sede URL's #####

	url(r'^pgen/sede/novo/$', views.sede_new, name='sede_new'),
	url(r'^pgen/sedes_cadastradas/$', views.sede_list, name='sede_new_list'),
	url(r'^pgen/sede/(?P<pk>\d+)/edit/$', views.sede_edit, name='sede_edit'),
	url(r'^pgen/sede/(?P<pk>\d+)/remove/$', views.sede_remove, name='sede_remove'),	
]