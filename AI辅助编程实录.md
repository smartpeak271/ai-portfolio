AI辅助编程实录
1. 我的任务
使用 Python 读取 data/生词表.csv，生成 A/B/C/D 选择题，保存到 练习.txt。

2. 遇到的最大困难
一开始运行代码，总是报错 ModuleNotFoundError: No module named 'weekpath'，后来又报错 FileNotFoundError（找不到生词表）。

3. 我是怎么解决的
我向 AI 求助，AI 帮我修改了代码开头的路径导入方式（加上了 sys.path.insert），并且把寻找文件的路径改成了老师提供的 weekpath.data_path()。最后终于成功跑通了！

4. 我的个人特色
我不满足于老师原本的“造句”功能。我让 AI 帮我改成了生成选择题。现在生成的 练习.txt 里，每道题有 A、B、C、D 四个选项，而且用随机抽取的干扰项打乱了顺序，非常适合用来做课堂小测。