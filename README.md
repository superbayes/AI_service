# AI_service
这个项目主要用来解决AI在生产遇到的问题,如模型部署方案等
## AI模型部署

- 机器学习是python语言的长处，而Java在web开发方面更具有优势，如何通过java来调用python中训练好的模型进行在线的预测呢？
- 在java语言中去调用python构建好的模型主要有三种方法：

- [ ] 1.在Java语言中，通过python的解释器执行python代码，简单来说就是在java中通过python解释器对象，传入写好的python代码，进行执行，这样的方式运行的效率非常低，而且存在很多python包无法使用的情况，只适合做简单的python代码的运行，并不推荐使用。

- [ ] 2.通过PMML工具，将在sklearn中训练好的模型生成一个pmml格式的文件，在该文件中，主要包含了模型的一些训练好的参数，以及输入数据的格式和名称等信息。生成了pmml文件之后，在java中导入pmml相关的包，我们就能通过pmml相关的类读取生成的pmml文件，使用其中的方法传入指定的参数就能实现模型的预测，速度快，效果不错。

- [ ] 3.第二种方法因为模型已经训练好了，无法改变，不能实现在线调参的功能，我们可以通过socket服务来进行python和java之间的网络通信，python提供socket服务，java端将模型的参数通过网络传给python端，python端接受到参数之后，进行模型的训练，训练完成之后，将得到的结果返回给Java端。

### 在socket文件夹中主要采用第三种方案

- 第一步,你需要首先启动**py_socketserver.py**这个文件,开启服务端

  - 你可以通过host,port来设置服务端的IP,端口号

    ```python
        host = "localhost"
        port = 9999
        start_server(host=host, port=port).start_socketserver(RequestHandler)
    ```

  - 你也可以在这个API当中包装你的业务逻辑

    ```python
    def model_predict(data):
        """
        在这里处理你的模型预测,业务逻辑
        :param data:传入参数,根据你的业务而定
        :return:
        """
        data = data +  '----机器学习的模型在这里处理数据,返回结果......'
        return data
    ```

- 第二步,启动**py_client.py**这个文件,当做client客户端
  - 建议通过cmd>>python py_client.py 的方法来启动
  - 你也可以写java,C++的socket 客户端代码,并向服务端发送参数

### 最后,如果你遇到模型部署的其他问题,也可及时联系我.....

my adress: nanyangjx@126.com


