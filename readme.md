1. 使用 `pip` 命令安装依赖
   
   ``` bash
   pip install require.txt
   ```
   
2. 安装 `edge` 浏览器，注意安装的版本

   我这里使用的是 ` 98.0.1108.50 ` 

   有能力的可以尝试把代码改成使用 `chrome` 浏览器的，`chrome` 会更方便一点。

3. 下载 `edge` 浏览器的驱动

   下载链接 https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/

   注意要下载和浏览器版本相同的驱动

4. 修改 `config.py` 

   | `driver_path`  | 本机 `edge` 驱动的路径                    |
   | -------------- | ----------------------------------------- |
   | `show_browser` | 是否显示浏览器界面，可选 `true` ，`false` |

5. 登录 `QQ` ，因为用的是 `selenium` ，不太好搞验证码，所以是模拟点击 `QQ` 登录从而登录微校园。**一定要确认自己可以通过`QQ` 登录华中大微校园** 

6. 命令行运行

   ~~~ bash
   python main.py > log.txt 2> err.txt
   ~~~

   把运行过程中的日志信息输出到 `log.txt`，把错误信息输出到 `err.txt`，命令行输出的都是一些调试工具的信息，不用管。

   如果运行错误，可以尝试多运行几次。也可以改用 `pycharm` 运行。
   
7. 博客 [HUST疫情填报 | Luobuyu's Blog](https://www.luobuyu.ml/2022/hust-yqtb/) 

