'''defines url patterns for learning_logs'''

from django.urls import path

from . import views
#The variable app_name helps Django distinguish this urls.py file from files of the same name in other apps
app_name = 'learning_logs'
#a list of individual pages that can be requested from the learning_logs app
urlpatterns =[
    #home pages
    #path()function takes a stringURL that helps django to route the view;
    #the second argument in path() specifies which function to call in views.py;
    #provides the name index for this URL pattern so we can refer to it more easily in other files (represent the link using this name instead of writing out a URL ).
    path('', views.index, name = 'index'),
    #a page that display all topics 
    path('topics/', views.topics , name = 'topics'),
    path('topics/<int:topic_id>/', views.topic , name = 'topic'),
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # page for adding a new entry,how the topic id will be process
    path ('new_entry/<int:topic_id>/', views.new_entry, name ='new_entry'),
    #page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry,name ='edit_entry'),
    
]
'''
To generate a link, we use
a template tag, which is indicated by braces and percent signs ({% %}). A template
tag generates information to be displayed on a page. The template
tag {% url 'learning_logs:index' %} shown here generates a URL matching
the URL pattern defined in learning_logs/urls.py with the name 'index' 1. In
this example, learning_logs is the namespace and index is a uniquely named
URL pattern in that namespace. The namespace comes from the value we
assigned to app_name in the learning_logs/urls.py file.'''
#无法克服，就永远也除法达到。