## Ⅰ 基本概述

### 1 为什么使用虚拟环境

用于在开发中创建一个隔离的环境
这个环境中的包和库，只会在这个环境中有效。不会影响其他环境
Python默认使用全局环境

### 2 虚拟环境分类

* `venv`：Python 内置模块，用于创建隔离的Python环境。
* `Conda`：开源的包管理系统 和 环境管理系统，用于安装多种包，也可以创建多个独立环境。

## Ⅱ 创建和使用虚拟环境

### 1 创建venv

#### 1.1 使用VSCode创建

> **==创建==**

按F1打开帮助界面，输入 `Create Environment`

![|500](../001_python_tutorial/assets/note_image/image-20240129172535517.png)


选择 `Venv`

![|500](../001_python_tutorial/assets/note_image/image-20240129172625122.png)

指定 Python 环境，选择安装的 `python.exe` 
右下角，显示创建成功，环境为： 
```sh
# 已选择以下环境: 
# d:\BaiduSyncdisk\Program_Workspace\Python\venv_sms_demo\.venv\Scripts\python.exe
```

目录部分出现 `.venv` 目录， 所有在这个目录下的包，都可以共享这个环境
![|180](../001_python_tutorial/assets/note_image/image-20240129172934821.png)

#### 1.2 终端创建虚拟环境（建议使用）

VScode中使用 `ctrl + ~` 打开终端，终端中选择 `Command Prompt` ，就是CMD

![|200](../001_python_tutorial/assets/note_image/image-20240129173542226.png)
```sh
# 创建虚拟环境，目录保存到当前目录下的 .venv 下
python -m venv .venv     
# 激活虚拟环境
.venv\Scripts\activate
# (.venv) D:\BaiduSyncdisk\Program_Workspace\Python\test_for_del>       出现（.venv）已经激活
```

### 2 使用虚拟环境

```sh
# 查看当前环境的库
pip list
# 导出当前环境，生成 requirements.txt
pip freeza > requirements.txt
# 使用requirement.txt 同步到新虚拟环境
pip install -r requirements.txt
```

### 3 删除虚拟环境

首先 `deactivate`
```sh
(.venv) D:\BaiduSyncdisk\Program_Workspace\Python\test_for_del>.venv\Scripts\deactivate
```
然后F1 输入 `Select Interpreter` 选择现在使用的 `python.exe` 
![|500](../001_python_tutorial/assets/note_image/image-20240129175346065.png)
最后物理删除文件目录
```sh
rmdir /s .venv
```
