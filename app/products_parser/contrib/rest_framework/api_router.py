from rest_framework import routers


class Router(routers.DefaultRouter):
    include_root_view = False

    def __init__(self):
        super().__init__()
        self.trailing_slash = "/?"
