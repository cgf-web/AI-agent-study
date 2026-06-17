`安装 faiss`

`pip install faiss-cpu`

`embedding 嵌入（向量化）`

`Q：老师这节课和text to sql的关联可以讲讲吗？`

`text to sql：函数调用，让大模型可以调用函数 进行SQL查询`

`相似度的检索，比如有些SQL的写法（Question, SQL answer 写入到知识库）`

`Q：faiss是在trae上安装吗`

`pip install faiss-cpu`

`Q：什么时候用ES来做向量数据库`

`数据量很大，而且想要同时支持  关键词 + 向量相似检索`
支持`单索引 21亿数据`

`Q：老师，天池那个到了508怎么都降低不下去，而且越做越高，是不是应该从新来做一遍了？中间一次让他做了比较多的特征工程，反而越来越高`

`是不错的方式`

`Q：老是用阿里的Qoder 做开发工具怎么样。`

`RAG 知识库检索 = 底层逻辑> embedding`  

`3329 = 1元特征的数量 + 2元特征的数量 + 3元特征的数量`

`1000 + 1000 + 1329 = 3329`

`用现在的这种方法，是推荐的策略，但是问题在于：`

`特征维度太大了，而且 很多特征值为0 => 存储空间 太浪费，而且计算量会比较大`
![[Pasted image 20260617232917.png]]

`Q：min_count=1是什么参数`

`最小出现的词频 >=1`

`min_count = 10`

`Q：我们实操的时候`

`怎么知道特征设置多少维比较好呢？`

`做实验的过程，embedding  size, vector_size = 100`

`Q：word2vec 商品2vec， word 如何转换为商品？`

`word2vec => embedding is all you need  万事万物都可以embedding`

`商品A 和 商品B 像不像？=> 推荐系统，淘宝上，看中了某个商品A，淘宝给你推荐商品B`

`A B C D E (句子）`

`点击商品的顺序，组成一个句子；`

`session1：商品A 商品B 商品C ... 商品F`

`session2：商品B 商品E 商品F ... 商品H`

 `...`

`很多的商品看过的序列 组成的句子 => word2vec`（2014谷歌）

`学习商品embedding`

`========`

`商品点击的序列 =》 句子的模式`

`商品购买的序列 => 句子的模式`

`人物 能否做相似度的推荐`

`session1：人物a 人物b 。。。 人物f`

`session2：人物b 人物e 。。。 人物h`

`=》 句子`

`学习人物embedding`

`Q：vector_size=100 和刚刚n=100是一样的意思吗`

`Q：像这种超参数，有没有经验数值？`

`embedding size`

`Q：词转向量`

`Q：安装jieba和gensim包就可以运行了`

`向量化`

`Q：min_count是什么？`

`min_count = 10 词频要>=10的单词才进行embedding学习`

`Q：孙悟空+唐僧-孙行者，答案是不是更应该是唐僧才是最接近的啊`

`Q：one-hot编码方式本身不是向量吗？`

`是向量，但是维度太大 => 稀疏`

`embedding 减少0   使更稠密`

`https://huggingface.co/spaces/mteb/leaderboard`

`开源的embedding模型，在modelscope里面可以检索 embedding模型`

`https://modelscope.cn/models/Qwen/Qwen3-Embedding-8B/files 15.15GB，4090显卡`

`也可以使用商业的embedding模型，通过DASHSCOPE_API_KEY 调用`

`Q：中文embeding哪个最好，并且方便本地部署`

`qwen3-embedding 8B`

`bge-m3`

`https://modelscope.cn/models/BAAI/bge-m3`

`Q：多语言是不是就等于实时翻译了？`

`embedding 不等于翻译`

`Q：有科技论文多语言模型吗`

`Q：千文的8B要钱吗？还是下载到本地，不用花钱？`

`免费开源的`

`https://modelscope.cn/models/Qwen/Qwen3-Embedding-8B`

`Q：老师，这里的选择模型，就是选择的中间隐藏层的内容吗`

`embedding 保存到隐藏层中`

`Q：数据集怎么做`

`测试；先准备知识库（金融股票知识）`

`query1 => 从知识库里检索到哪些chunk`

`Q：我们做RAG的时候，需要用这种embedding模型先转向量再保存到向量数据库吗？这种模型的使用场景也是相似度比较，跟向量数据库功能上是类似的？`

`知识库 => 切分成了chunks（原文）=> chunk embedding => 保存到向量数据库`

`Q：老师，我要这个embeddings干嘛？业务场景我可能还是不太明白，如果我用了大模型，还需要额外用embedding吗？大模型本身不带embedding的吗？`

`LLM模型 => 推理，回答问题（LLM尺寸，文件大小 很大，DeepSeek R1 671B）`

`embedding模型 =》 不需要回答推理任务，只是做 相似度判断， 判断知识库里哪些chunk 和 query 很像`

`知识库里面有1万chunks，如果要通过LLM进行筛选 chunks 哪个好，哪个不好 => 计算1万次`

`embedding`

`Q：多语种的embedding 是怎么实现的？`

`数据源是多语言，训练方式是一样`

`Q：谷歌最开始，怎么给man和women定向量的值，每个词本身有自己向量才能看两个词之间的相似度吧`

`很多的句子 => 给到神经网络（无监督的学习，自己找到 embedding规律）`

`Q：做消费者行为分析的话，可以用embedding来做特征提取分析吗，还是要用SQL来做呢`

`embedding 相似度的检索，知识检索`

`消费者A 行为embedding`

`消费者B 行为embedding`

`=》 计算两者像不像`

`Q：老师，升维是否一定维持或提升检索准确度？`

`维度是固定列表值，还是在最大值以下的任意值？ => 固定列表值`

`Q：transformer里的embedding为什么不可以是原始文本`

`我想知道迪士尼的退票政策`

`LLM => 推理`

`Q：什么是chunk 和 句子进行分词 一样么？`

`chunk 是对全文的一种切片，一片文章可能会有10万字 => 1个chunk （比较粗）`

`# 在加载的FAISS索引中执行搜索`

`distances, retrieved_ids = loaded_index.search(query_vector, k)`

`--- 排名 1 (相似度得分/距离: 0.3222) ---`

`ID: 2`

`原始文本: 对于在线购买的迪士尼门票，如果需要退票，必须在票面日期前48小时通过原购买渠道提交申请，并可能收取手续费。`

`元数据: {'source': 'online_policy.html', 'category': '退票政策', 'author': 'E-commerceTeam'}`

`--- 排名 2 (相似度得分/距离: 0.3312) ---`

`ID: 0`

`原始文本: 迪士尼乐园的门票一经售出，原则上不予退换。但在特殊情况下，如恶劣天气导致园区关闭，可在官方指引下进行改期或退款。`

`元数据: {'source': 'official_faq_v1.pdf', 'category': '退票政策', 'author': 'Admin'}`

`--- 排名 3 (相似度得分/距离: 1.0135) ---`

`ID: 1`

`原始文本: 购买“奇妙年卡”的用户，可以享受一年内多次入园的特权，并且在餐饮和购物时有折扣。`

`元数据: {'source': 'annual_pass_rules.docx', 'category': '会员权益', 'author': 'MarketingDept'}`

`向量 cos值（cos值越大 => 越相似） **** [-1, 1]`

`向量的 欧式距离（距离越小 => 越相似）`

`Step1，创建faiss 数据库（存储这些embedding）`

`Step2，query => query embedding`

`Step3，在faiss中进行 向量的相似检索 => TopK`

`Q：10MB文档，要embedding，用faiss适合 吗？`

`适合`

`任何的向量数据库，都要使用 第三方的embedding（比如 qwen3-embedding）`

`存储这些embedding，以及检索这些embedding`

`faiss`

`Q：哪些数据属于metadata`

`数据的所属文件，数据的时间，数据的作者 。。。`

`Q：faiss 的数据存在哪？`

`持久化 保存到文件中`

`faiss 是一个向量，python 可以对向量进行持久化  pickle`

`Q：这都还没到大模型呢，还在匹配知识库提示词的阶段`

`LLM推理 + RAG知识库（如何筛选找到相似的知识）`

`Q：FAISS和LanceDB都有什么区别？都是向量数据库吗？前者是向量检索库，后者是完整的向量数据库？`

`faiss = 库`

`向量数据库 = 一个完整的软件 （包括 FAISS库 + 管理界面，元数据的管理）`

`Q：有没有既使用LLM又要使用embedding的场景`

`RAG = 知识库的问答`

`LLM问答，回答你的问题`

`LLM + 相关的上下文（embedding的标准，检索出来的相似的TopK chunk）`

`Q：FAISS是python的工具，但是企业级应用中一般都是java语言，企业级应用向量库推荐用什么？`

`ES`

`Q：只是做个10个人以内的小系统`

`Q：这个计算需要GPU加速吗`

`embedding模型，通过GPU可以进行批量的计算`

`Q：为啥没有 chroma`

`你用 Java 没听到过 es 吗`

`Q：query embedding 到 faiss 中检索， 是和 faiss 中的向量进行相似度计算？检索实质是计算相似的？`

`是的`

`大家都按照相同的标准，比如都是 1024维`

`Q：这里的元数据指的是？`

`数据来源，作者，时间`

`Q：PDF可以Embedding吗`

`可以，pdf 提取文本，提取图片 => embedding`

`Q：java直接用ES不就好了？`

`Q：元数据就是经过向量化的数据`

`元数据 = 数据的数据`

`Q：rag的embedding和transform的embedding一样吗`

`Q：如果想做专利检索数据库进行专利相似度比对的话，需要embedding数据库吗，数据集怎么做？怎么切分？`

`需要的`

`专利的数据，`

`Q：老师，faiss最后存哪儿了？可以看下保存之后长啥样吗？请问您平时用什么数据库？`

`# 把index 保存到文件中`

`index => .pkl    pickle.dump`

`Q：dify的知识库想要切换这些向量数据库，要安装软件或插件吗？还是改一下配置文件中的向量数据库名就行？`

`Q：10维和20维内容具体的区别是什么呢？`

`x1, x2, ..., x10 性格、年龄、身高 ...`

`x1, x2, ..., x10，x11, ..., x20 性格、年龄、身高 ... 籍贯、父母的情况`

`Q：变成向量的数据，如何转回成文本信息传给LLM`

`Q：对，我也想问faiss算的时候是暴力遍历吗？ 还是说只有L2是暴力的？那要是数据极大，用最近邻的话就不准了啊？最终还是是要分桶吧？`

`Q：如果更换embedding模型，是不是向量数据库中的数据都不能用了?即使更换前后维度是一样的？`

`Q：Word2Vec工具是每个词元只跟窗口内的词元做相关度计算吗？而不是跟文档的所有词元做相关度计算？`

`Q：不同embedding之间解析出的向量数据，是不能互相理解的吧？`

`Q：用embedding能做价格预测吗？`

`Q：存向量库前使用的embedding和query的embedding必须是同一个吗？`

`是的！`

`Q：知识一直在变 是不是需要一直执行全量embedding计算？ 是否可以增量计算`

`可以增量`

`Q：中文的国王和英文的king两个词在多语言enbbing库中，向量相似度会很相近么？`



判断两个向量之间像不像，用余项计算相似度
计算A和B的余弦相似度:
句子A:这个程序代码太乱，那个代码规范
句子B:这个程序代码不规范，那个更规范
Step1，分词    （更小的颗粒度）   工具--jieba
句子A:这个/程序/代码/太乱，那个/代码/规范
句子B:这个/程序/代码/不/规范，那个/更/规范
Step2，列出所有的词
这个，程序，代码，太乱，那个，规范，不，更
Step3,计算词频
句子A:这个1，程序1，代码2，太乱1，那个1，规范1，不0，更0    [1,1,2,1,1,1,0,0]
句子B:这个1，程序1，代码1，太乱0，那个1，规范2，不1，更1    [1,1,1,0,1,2,1,1]

计算A和B的余弦相似度:
Step4，计算词频向量的余弦相似度
句子A:(1, 1, 2, 1, 1, 1, 0, 0)
句子B:(1, 1, 1, 0, 1, 2, 1, 1)
![[Pasted image 20260617225652.png]]
结果接近1，说明句子A与句子B是相似的

什么是N-Gram(N元语法):
基于一个假设:第n个词出现与前n-1词相关，而与其他任何词不相关.
N=1时为unigram, N=2为bigram,N=3为trigram·
N-Gram指的是给定一段文本，其中的N个item的序列
比如文本:A B C D E,对应的Bi-Gram为A B, B C, CD, DE
·当一阶特征不够用时，可以用N-Gram做为新的特征。比如在处理文本特征时，一个关键词是一个特征，但有些情况不够用，需要提取更多特征。组合采用N-Gram=>可以理解是相邻两个关键词的特征组合

如何了解事物的特征表达?N-Gram就是最基本的一种方式


#### 什么是Embedding:
·一种降维方式，将不同特征转换为维度相同的向量:
·离线变量转换成one-hot=>维度非常高，可以将它转换为固定size的embedding向量
·任何物体，都可以将它转换成为向量的形式，从Trait#1到#N
·向量之间，可以使用相似度进行计算
当我们进行推荐的时候，可以选择相似度最大的

Rag的基础就是因为万事万物都能Embedding     < === ===数学工具：cos值    比较两者之间的相似性

50维度向量 可以做加减
king-man+woman == ==queen

10000维--压缩->300维       替代关系

##### Word2Vec:
通过Embedding，把原先词所在空间映射到一个新的空间中去，使得语义上相似的单词在该空间内距离相近      近似等比例映射

Word Embedding=>学习隐藏的权重矩阵

输入层是one-hot编码

隐藏层的神经元数量为hidden_size(Embedding Size）
对于输入层和隐藏层之间的权值矩阵W，
[vocab_size, hidden_size]
输出层为[vocab_size]大小的向量，每一个值代表着输出一个词的概率


Gensim工具（谷歌开源的单词训练工具）

 

