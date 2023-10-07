from django.urls import path

from principal.views import PublicacaoApiView, PublicacaoDetalheApiView

urlpatterns = [
    path('api/publicacao', PublicacaoApiView.as_view()),
    path('api/publicacao/<int:id>', PublicacaoDetalheApiView.as_view())

    #path('api/autor', ...)
]