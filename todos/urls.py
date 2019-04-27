from django.urls import path
from todos import views, auth, api

#app_name='todos'
urlpatterns = [
	path('', views.index, name='index'),
	path('create/', views.create, name='create'),
	path('save/', views.save, name='save'),
	path('complete/<int:id>', views.complete, name="complete"),
	path('edit/todos/<int:id>', views.edit, name='edit'),
	path('delete/todos/<int:id>', views.delete, name='delete'),
	path('login/', auth.login, name="login"),
	path('logout/', auth.logout, name='logout'),
	path('authenticate/', auth.authenticate, name='authenticate'),
	path('signup/', auth.signup, name='signup'),
	path('signup/submit', auth.signup_submit, name='signup_submit'),
	path('api/todos/<int:pk>', api.TodoItemView.as_view(), name='api_todo_item'),
	path('api/todos/', api.TodoListView.as_view(), name="api_todo_list")
]
