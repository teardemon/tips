#MkDocs
MKDocs可以简单快速的构建项目文档静态网站文件．

参考链接：

* [http://www.mkdocs.org/][l2]
* [https://readthedocs.org/][l3]
##安装
使用pip安装MKDocs,检测是否反装
```bash
~$ python --version
Python 2.7.6
~$ pip --version
pip 1.5.4 from /usr/lib/python2.7/dist-packages (python 2.7)
```
使用pip安装mkdocs
```bash
 pip install mkdocs
```
安装完成,查看mkdocs
```bash
$ mkdocs --version
mkdocs, version 0.15.3
```
##Getting started
创建项目
```bash
mkdocs new my-project
cd my-project
```
查看项目目录结构
```bash
$ tree my-project/
my-project/
├── docs
│   └── index.md
└── mkdocs.yml
```
使用mkdocs serve使用mkdocs自带的网页服务器预览文档,访问[ http://127.0.0.1:8000/][l1]
```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```
##Building the site
构建文档
```bash
mkdocs build
```
使用git版本管理，不需要将生成的文档加入源，添加'site/'至'.gitignore'
文件
##编辑文档
TBD...
##发布
TBD...

[l1]: http://127.0.0.1:8000/
[l2]: http://www.mkdocs.org/
[l3]: https://readthedocs.org/


