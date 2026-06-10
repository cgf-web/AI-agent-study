from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()#OpenAI兼容API接口

completion = client.chat.completions.create(
    model="glm-4-flash",#选择模型
    messages=[   #发送对话         这两个参数是必须的 最少两个参数
        {
            "role":"system",
            "content":"回复10个字" #系统设定
        },
        {
            "role": "user",
            "content": "你是谁"     #用户的问题
        }
    ],
    temperature=1,    #越小越保守   越大越发散
    stream=True,
)

#print(completion.choices[0].message.content)

#逐步、增量输出生成内容
for chunk in completion:
    print(chunk.choices[0].delta.content,end="|")