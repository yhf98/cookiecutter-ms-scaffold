from apps.services.http.controller.v1.user import app as user_app

urls = [
    {"ApiRouter": user_app, "prefix": "/user/api", "tags": ["用户"]},
]