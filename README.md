Swallow
----------
个人网站管理后台后端，基于[Flask](https://www.palletsprojects.com/p/flask/)。 前端部分代码查看[swallow-front](https://github.com/boyaziqi/swallow-front)

#### 功能
- 富文本管理
- 文章列表与预览
- 评论管理
- 相册管理
- 用户账号管理 

#### 构建
克隆项目源，进入项目目录
```shell
python3 -m venv .venv
# 初始化数据库 (确保配置的SQLALCHEMY_DATABASE_URI参数已经指向正确的数据库）
python init_db.py
source .venv/bin/activate
flask run
```

本项目为个人项目，主要目的是学习和自用。并不具备很好的扩展和兼容性。想学习`Flask`的可以克隆本仓库，并参考相关文档实战练习。
