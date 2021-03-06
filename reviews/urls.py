from django.contrib import admin
from django.urls import path, include
import reviews.views

urlpatterns = [
    path('', reviews.views.index, name='view_reviews'),
    path('create/<course_id>', reviews.views.create_review, name='create_review'),
    path('update/<review_id>', reviews.views.update_review, name='update_review'),
    path('delete/<review_id>', reviews.views.delete_review, name='delete_review'),
    path('create/comment/<review_id>', reviews.views.create_comment, name='create_comment'),
]
