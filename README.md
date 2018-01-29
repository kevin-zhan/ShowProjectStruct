# ShowProjectStruct
##What
一个简单的脚本，用来格式化的输出一个目录的层级。  
##Why
有时候需要观察一个项目的结构，而项目中的无关文件又很多，这时候就可以通过这个脚本来计算展示。  
##How
需要安装一PrettyTable这个库：
```shell
pip install prettytable
```
然后就可以来计算了：
```shell
python show_struct.py [dir] [level]
```
