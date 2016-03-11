from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freelancer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'news.views.main', name='main'),
    url(r'^league/(?P<league_id>.+)$', 'news.views.league', name='league'),
    url(r'^team/(?P<team_id>.+)$', 'news.views.team', name='team'),
    url(r'^content/(?P<content_id>.+)$', 'news.views.content', name='content'),
    #url(r'^brand/(?P<brand_id>.+)$', 'main.views.brand',name='brand'),
    #url(r'^model/(?P<model_id>.+)$', 'main.views.model',name='model'),
    #url(r'^instance/(?P<instance_id>.+)$', 'main.views.instance',name='instance'),
    #url(r'^add_instance/phones$', 'main.views.add_instance_phones',name='add_instance_phones'),
    #url(r'^add_instance/notebooks$', 'main.views.add_instance_notebooks',name='add_instance_notebooks'),
    #url(r'^add_instance/tablets$', 'main.views.add_instance_tablets',name='add_instance_tablets'),
    #url(r'^add_instance/accessories$', 'main.views.add_instance_accessories',name='add_instance_accessories'),
    #url(r'^delete_diesel/$', 'main.views.delete_from_diesel',name='delete_diesel'),
    #url(r'^signin$', 'main.views.signin',name='signin'),
    #url(r'^signup$', 'main.views.signup',name='signup'),
    #url(r'^signout$', 'main.views.signout',name='signout'),
)
