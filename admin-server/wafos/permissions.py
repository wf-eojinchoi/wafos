from agency_account.models import AgencyAccount
from rest_framework.response import Response
from rest_framework import status


def agency_required(function):
    def wrap(self, request, *args, **kwargs):
        auth_key = request.META.get('HTTP_AUTHORIZATION', '')

        if not (auth_key):
            return Response({'detail': 'No auth_key'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            self.agency_account = AgencyAccount.objects.get(
                api_seckey=auth_key)
            self.agency = self.agency_account.agency
        except AgencyAccount.DoesNotExist as e:
            print(e)
            return Response({'detail': 'No agency'},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)

        return function(self, request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
