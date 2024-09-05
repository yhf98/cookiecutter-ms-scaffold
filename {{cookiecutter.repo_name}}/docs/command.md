# 落地页服务
```bash
python main.py {{cookiecutter.repo_name}}
```

# 启动平台管理
```bash
python main.py {{cookiecutter.repo_name}}
```

# 新建模块
```bash
# Portal
python main.py init-app {{cookiecutter.repo_name}}/模块名称
```

# 数据表结构迁移
```
python main.py migrate --env dev
```

# 根据models生成crud
```
python scripts/crud_generate/user.py
```


## docker 
```bash
docker build -t {{cookiecutter.repo_name}} -f ./docker/{{cookiecutter.repo_name}} .
```