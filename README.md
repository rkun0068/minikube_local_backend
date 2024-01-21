### 介绍
  基于Django的一个本地minikube后端，通过命令获取信息，进行简单数据展示
### 前端地址
[https://github.com/rkun0068/minikube_local_frontend](https://github.com/rkun0068/minikube_local_frontend)
### 界面展示
![image.png](https://cdn.nlark.com/yuque/0/2024/png/29558585/1705829558323-9ed19b26-40d7-4475-95d9-0b293e9eec1b.png#averageHue=%23f8f8f7&clientId=ueca9d727-6b7b-4&from=paste&height=838&id=cLTyJ&originHeight=1048&originWidth=1860&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=149328&status=done&style=none&taskId=ueeb29647-37cc-4c56-ad3c-4300ddc1513&title=&width=1488)

### 项目启动
#### 创建虚拟环境
```bash
python -m venv venv
```
#### 激活虚拟环境
```bash
source venv/bin/activate   #Linxu/MacOS
venv\Scripts\activate      # Windows

```
#### 安装依赖
```bash
pip install -r requirements.txt

```
#### 启动项目
```bash
python manage.py runserver

```
### 项目结构
```bash
|-- __pycache__                       # Python 编译缓存文件目录，包含已编译的 Python 文件
|-- api                               # Django APP
|-- common                            # Django APP
|-- k8s_platform_backend              # Django 项目的主目录，可能包含项目的设置和配置等文件
|-- manage.py                         # Django 项目管理脚本，用于执行不同的 Django 命令
|-- pod                               # Django APP
|-- requirements.txt                  # 项目的依赖文件，包含项目所需的 Python 包及其版本信息
|-- templates                         # 存放 Django 项目中的 HTML 模板文件的目录
|-- tmp.yaml                          # 临时 YAML 文件，用于自定义创建集群资源
`-- work_load                         # Django APP

```

