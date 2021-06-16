from django.conf.urls import url, include
from django.contrib import admin
from LMList import views 

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),
    url('admin/', admin.site.urls),   
    url(r'^LMList/new$', views.new_list, name='new_list'),    
    url(r'^LMList/(\d+)/$', views.view_list, name='view_item'),
    url(r'^LMList/form$', views.form_list, name='form_list'),  
    url(r'^LMList/next$', views.next_list, name='next_list'),  
    url(r'^LMList/third$', views.third_list, name='third_list'),  
    url(r'^LMList/fourth$', views.fourth_list, name='fourth_list'), 
    url(r'^LMList/contact$', views.contact_list, name='contact_list'),    
    url(r'^LMList/(\d+)/add_item$', views.add_item, name='add_item'),]

    

