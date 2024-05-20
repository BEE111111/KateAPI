from django.urls import path

from app.ScientistsViews import ScientistRegistrationAPIView, ScientistDetailAPIView, ScientistUpdateAPIView
from app.bibTexViews import BibTexUploadView, BibTexListView, BibTexByAuthorListView, \
    BibTexByUserListView, AuthorListView, BibTexByDOIView, UncheckedBibTexView, BibTexUploadAndCheckView, \
    CheckedBibTexView
from app.userViews import UserRegistrationAPIView, LoginAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('upload-bibtex/', BibTexUploadView.as_view(), name='upload-bibtex'),
    path('bibtex/', BibTexListView.as_view(), name='bibtex-list'),
    path('bibtex/author/<str:author_name>/', BibTexByAuthorListView.as_view(), name='bibtex-by-author'),
    path('bibtex/user/<str:username>/', BibTexByUserListView.as_view(), name='bibtex-by-user'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('bibtex/doi/<path:doi>/user/<str:username>/', BibTexByDOIView.as_view(), name='bibtex-by-doi'),
    path('bibtex/unchecked/<str:username>/', UncheckedBibTexView.as_view(), name='unchecked-bibtex'),
    path('bibtex/checked/<str:username>/', CheckedBibTexView.as_view(), name='checked-bibtex'),
    path('bibtex/check/<int:pk>/', BibTexUploadAndCheckView.as_view(), name='check-bibtex'),
    path('scientist/register/', ScientistRegistrationAPIView.as_view(), name='register-scientist'),
    path('scientist/<str:username>/', ScientistDetailAPIView.as_view(), name='get-scientist'),
    path('scientist/update/<str:username>/', ScientistUpdateAPIView.as_view(), name='update-scientist'),
]
