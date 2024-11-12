import uvicorn

if __name__ == '__main__':
    uvicorn.run(app='main:create_app', host="0.0.0.0", port={{cookiecutter.repo_port}}, lifespan="on", factory=True)