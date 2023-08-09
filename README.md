# PDF 本地知识库

## 项目说明
基于 FastAPI 快速开发框架，整合了 LangChain、OpenAI、FAISS等技术链，实现了基于PDF文档构建问答知识库
### 


## 如何使用

### 环境配置
* 使用 python3 版本，测试通过版本为3.10.x

### OpenAI
修改项目下的 `.env` 文件，项目中使用到 api-key 和 api-base 代理，如果不需要使用代理，可以注释 `main.py` 下的相应配置


### 创建虚拟环境
```python
#当前目录创建虚拟环境
python3 -m venv .

#激活虚拟环境
source venv/bin/activate

#安装依赖
pip3 install -r requirements.txt

```

### 项目启动
```python
#其中python为虚拟环境bin目录下的
python -m uvicorn main:app --reload 
```

### 接口调用
详情可查看 `chat.py` 文件
```javascript
# 调用初始化pdf向量化接口
http://127.0.0.1:8000/chat/init_pdf
```
```javascript
# 调用问答接口
http://127.0.0.1:8000/chat/question
```
