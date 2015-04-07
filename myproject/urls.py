from django.conf.urls import patterns, include, url
from django.contrib import admin
#from cms import views

urlpatterns = patterns('',
    # Examples: 
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(.*)$', 'cms_users_put.views.dbMngt', name = 'dbMngt'),
)
