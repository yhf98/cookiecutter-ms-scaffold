# 落地页服务
```bash
python main.py {{cookiecutter.repo_port}}
```

# 启动平台管理
```bash
python main.py platform
```

# 新建模块
```bash
# {{cookiecutter.repo_port}}
python main.py init-app {{cookiecutter.repo_port}}/home
```

# 数据表结构迁移
```
python main.py migrate --env dev
```

# 根据models生成crud
```
python scripts/crud_generate/data_page.py
```


## docker 
```bash
docker build -t ms-api-admin -f ./docker/{{cookiecutter.repo_port}} .
```