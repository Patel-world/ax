try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url

from .views import QuizListView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake, index, login_user, logout_user

urlpatterns = [
    url(r'^$', view=index, name='index'),
    url(r'^login/$', view=login_user, name='login'),
    url(r'^logout/$', view=logout_user, name='logout'),
    url(r'^quizzes/$',
        view=QuizListView.as_view(),
        name='quiz_index'),

    url(r'^dashboard/$',
        view=CategoriesListView.as_view(),
        name='dashboard'),

    url(r'^category/(?P<category_name>[\w|\W-]+)/$',
        view=ViewQuizListByCategory.as_view(),
        name='quiz_category_list_matching'),

    url(r'^progress/$',
        view=QuizUserProgressView.as_view(),
        name='quiz_progress'),

    url(r'^marking/$',
        view=QuizMarkingList.as_view(),
        name='quiz_marking'),

    url(r'^marking/(?P<pk>[\d.]+)/$',
        view=QuizMarkingDetail.as_view(),
        name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    url(r'^(?P<slug>[\w-]+)/$',
        view=QuizDetailView.as_view(),
        name='quiz_start_page'),

    url(r'^(?P<quiz_name>[\w-]+)/take/$',
        view=QuizTake.as_view(),
        name='quiz_question'),
]
