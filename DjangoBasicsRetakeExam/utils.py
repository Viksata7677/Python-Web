from traveler.models import Traveler


def get_user_obj():
    return Traveler.objects.first()