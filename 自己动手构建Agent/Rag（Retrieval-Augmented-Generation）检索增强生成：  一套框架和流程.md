RAG:全世界最流行的AI扫支术，也是AI领域最大的坑
Retrieval-Augmented Generation 检索增强生成(回答问题之前，先做一轮内部知识搜索)
1、构建可检索的==知识库==
2、模型调用知识库完成用户任务

知识切片   -->数学向量        在知识库里对比  相关性最高的 [0-1之间]

Query  
 
场景宽窄


RAG 的常见技术栈，可以按“分层”来理解。最核心的不是某个框架，而是这 6 层：
1. 数据接入层  
    把 PDF、网页、数据库、Notion、飞书、API 等内容读进来。  
    常用工具是 `LlamaIndex` 的 data connectors，或者 `LangChain` 的 document loaders。LlamaIndex 官方把这一步叫 `Loading`。  
    来源：[LlamaIndex RAG 介绍](https://developers.llamaindex.ai/python/framework/understanding/rag/)，[LangChain Knowledge Base](https://docs.langchain.com/oss/python/langchain/knowledge-base)
    
2. 文本处理层  
    把原始文档清洗、切块、加 metadata，比如 `title`、`source`、`page`、`time`。  
    这一步直接影响召回效果。切得太大，噪声多；切得太小，上下文不够。  
    来源：[LangChain Knowledge Base](https://docs.langchain.com/oss/python/langchain/knowledge-base)
    
3. 向量化层  
    把文本和用户问题转成 embedding。  
    常见做法是用 OpenAI 的 embeddings；官方文档说明了 embedding 用于语义相似度检索。  
    来源：[OpenAI Embeddings Guide](https://developers.openai.com/api/docs/guides/embeddings)
    
4. 检索层  
    把向量存进向量库，再按相似度取回相关片段。  
    常见向量库有 `Qdrant`、`Pinecone`、`Weaviate`、`Milvus`、`FAISS`。如果要自己掌控部署，`Qdrant` 很常见；它官方文档也明确支持 dense、sparse 和 hybrid retrieval。  
    来源：[Qdrant 文档首页](https://qdrant.tech/documentation/)，[Qdrant Hybrid Queries](https://qdrant.tech/documentation/search/hybrid-queries/)
    
5. 编排层  
    把“检索 -> 组装上下文 -> 调模型 -> 输出答案”串起来。  
    最常见的是 `LangChain` 和 `LlamaIndex`。  
    `LangChain` 更像通用编排框架；`LlamaIndex` 更偏数据接入、索引、查询这条链路。  
    来源：[LangChain Retrieval](https://docs.langchain.com/oss/python/langchain/retrieval)，[LlamaIndex Framework](https://developers.llamaindex.ai/python/framework/)
    
6. 生成与评估层  
    生成层就是 LLM，本质上是“把检索结果作为上下文喂给模型”。  
    评估层常用 `Ragas`、`LangSmith`，分别做离线评测和观测/实验管理。  
    来源：[OpenAI Retrieval Guide](https://developers.openai.com/api/docs/guides/retrieval)，[Ragas Docs](https://docs.ragas.io/en/stable/)，[LangSmith Evaluate RAG](https://docs.langchain.com/langsmith/evaluate-rag-tutorial)
    

一个典型 RAG 实现流程，通常是这样：

1. 收集数据  
    把知识库内容统一拉进系统。
    
2. 解析与切块  
    抽正文，去噪，按段落/标题/语义做 chunk（数据块），并保留 metadata（元数据）。
    
3. 生成 embeddings  （嵌入向量）
    给每个 chunk 生成向量。
    
4. 建索引并入库  
    写入向量数据库，必要时同时建关键词索引，做 hybrid search （混合搜索）。
    
5. 查询时检索  
    把用户问题也向量化，召回 Top-K 相关片段。（高相关性）
    
6. 可选重排  
    用 reranker （重新排名）对召回结果再排序，减少“看起来像但其实不对”的片段。
    
7. 组装 Prompt  （提示词）
    把问题、检索到的上下文、回答约束一起发给模型。
    
8. 生成答案  
    要求模型“仅依据给定资料回答”，最好附引用来源。
    
9. 评估与迭代  
    看召回率、答案忠实度、上下文利用率，再调整 chunk、检索策略、prompt 和 reranker。

本质就是 `数据接入 -> 切块 -> embedding -> 检索 -> 重排 -> 生成 -> 评估`
效果好不好，关键在 `chunk 策略`、`检索策略`、`metadata`、`reranking` 和 `evaluation`
