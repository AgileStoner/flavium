from .permissions import IsOwnerOrReadOnly, IsVenueOwnerOrReadOnly, IsOwner, IsUserOrReadOnlyForVenueOwners, NotVenueOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class VenueOwnerPermissionMixin():
    permission_classes = [
                    IsAuthenticatedOrReadOnly ,
                    IsVenueOwnerOrReadOnly, 
                    IsOwnerOrReadOnly]


class BookingOwnerPermissionMixin():
    permission_classes = [
                    IsAuthenticated, 
                    IsOwner]


class UserOwnerPermissionMixin():
    permission_classes = [
                    IsAuthenticated,
                    IsUserOrReadOnlyForVenueOwners,]


class ReviewOwnerPermissionMixin():
    permission_classes = [
                    IsAuthenticatedOrReadOnly,
                    NotVenueOwnerOrReadOnly,
                    IsOwnerOrReadOnly,]


class ResponseOwnerPermissionMixin():
    permission_classes = [
                    IsAuthenticatedOrReadOnly,
                    IsVenueOwnerOrReadOnly,
                    IsOwnerOrReadOnly,]