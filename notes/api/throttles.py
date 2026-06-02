from rest_framework.throttling import UserRateThrottle


class NoteThrottle(UserRateThrottle):
    rate="10/min" 