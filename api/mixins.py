from rest_framework.permissions import IsAuthenticated


class IsAuthenticatedMixin:
    permission_classes = [IsAuthenticated]
