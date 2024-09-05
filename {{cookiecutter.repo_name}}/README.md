# {{cookiecutter.repo_name}}

# 启动服务
```bash
python main.py {{cookiecutter.repo_name}}
```

# 新建模块
```bash
# python main.py {{cookiecutter.repo_name}}
python main.py init-app python main.py {{cookiecutter.repo_name}}/home
```

# 数据表结构迁移
```
python main.py migrate --env dev
```

# 根据models生成crud
```
export PYTHONPATH=/www/wwwroot/{{cookiecutter.repo_name}}

python scripts/crud_generate/data.py
```

## docker 
```bash
docker build -t ms-api-admin -f ./docker/{{cookiecutter.repo_name}} .
```