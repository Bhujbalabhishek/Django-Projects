from django.urls import path
from news.views import scrape, news_list, setcookie, showcookie, delete_co, cookie_session, cookie_delete, create_session,access_session, delete_session



urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('', news_list, name="home"),
  path('setcookie', setcookie),
  path('getcookie', showcookie),
  path('deltecookie', delete_co),
  path('testcookie/', cookie_session),
  path('deletecookie/', cookie_delete),
  path('create/', create_session),
  path('access/', access_session),
  path('delete/', delete_session)
]
