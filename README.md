# 安装    
## 安装java环境、配置环境变量（Windows x64 或 Mac OS X x64）
* 下载地址：https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
* 配置环境变量

        # 环境变量
        JAVA_HOME   C:\Java\jdk1.8.0_144
        path：%JAVA_HOME%\bin
* 测试命令：java -version

## android环境安装
* 安装SDK Platform-Tools
    下载:https://www.androiddevtools.cn/
* 解压到C:\Android\sdk
*  设置环境变量：

        ANDROID_SDK_HOME  C:\Android\sdk
        ANDROID_SDK_ROOT  C:\Android\sdk
        # path：
        %ANDROID_SDK_HOME%\tools
        %ANDROID_SDK_HOME%\platform-tools 
* 测试命令：adb

## nodejs 安装
* 下载地址：https://nodejs.org/en/
* 设置path：如C:\ProgramFiles\nodejs\
* 测试命令：node -v

## appium 安装    
    npm install -g appium

## python 安装
* 下载地址：https://www.python.org/downloads/
    
## python插件安装
    pip install selenium -U
    pip install Appium-Python-Client
    pip install pywin32
    pip install openpyxl
    ## 图形界面
    pip install wxpyhton

# adb命令

    # 查看android设备名
    adb devices

    #连接appium -a表示ip，-p表示端口，-U表示设备的udid 可以通过appium -h查看更多命令
    appium -a 127.0.0.1 -p4723 -U4d007e9a1b0050d1 

# appium命令

    # 启动appium
    appium

# 启动python程序

    python [文件名]

# 问题

1. 就是可以通过模拟小红书搜索结果  用红色可以框出来所需要的内容，然后截图保存，同时可以把截图根据词来保存到本地并可以合并到表格里；
2. 可以根据词的搜索结果 导出 前多少页面的链接
3. 可以知道某一个链接或者标题 在小红书中搜索知道他被收录没有
