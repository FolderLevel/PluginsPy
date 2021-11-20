# README

Plugin如何编写示例

## 测试方法

* python3 .\LogTools.py PluginExample -h
  ```
  usage: LogTools PluginExample [-h] [-id ID] [-name NAME]
  
  optional arguments:
    -h, --help  show this help message and exit
    -id ID      唯一码
    -name NAME  唯一码别名
  ```
* python3 .\LogTools.py PluginExample -id pax -name zengjf
  ```
  >>> start call Plugin run or CmdMaps method
  >>> enter plugin run method
  实例输出：id: pax, name: zengjf
  <<< end plugin run method
  <<< end call Plugin run or CmdMaps method
  ```

## 自动生成run方法

使用Decorator添加run()方法

```python
import tools.ClassFunctions as ClassFunctions

@ClassFunctions.addRun
class PluginExample:
```

## 参数声明

* 第一行是类说明，在帮助中显示
* @开头并且以:分开的是参数及其说明
* 之外的是普通说明，可以自行添加，譬如以*号开始列表

```python
@ClassFunctions.addRun
class PluginExample:
    """
    PluginExample类是一个编写LogTools插件的示例

    @id: 唯一码
    @name: 唯一码别名
    """
```
