from apps.portal.home.services.http.v1.views import app as portal_app

urls = [
    {"ApiRouter": portal_app, "prefix": "/{{cookiecutter.repo_name}}/api", "tags": []},
]