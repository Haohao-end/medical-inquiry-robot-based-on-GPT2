
# 🤖 基于GPT2的智能医疗问诊机器人 🩺

**让AI成为您的私人医疗助手！**  
基于GPT2模型构建的医疗问答系统，提供精准、高效的医疗咨询体验。支持命令行交互与Web界面，助力医疗智能化！

---

## 🌟 项目亮点
- **专业领域**：专注医疗问答，数据涵盖3万+医患对话  
- **前沿技术**：基于GPT2模型，支持多轮对话生成  
- **灵活部署**：提供命令行和Web交互两种方式  
- **高效训练**：预训练模型微调，快速适配医疗场景  
---

## 🚀 快速开始

### 环境准备
```bash
# 基础依赖
Python>=3.6  
PyTorch>=1.7.0  
Transformers>=4.2.0

# 一键安装
pip install -r requirements.txt


### 数据准备
1. 下载数据到指定目录：  
   ```bash
   mkdir -p /Users/**/PycharmProjects/llm/Gpt2_Chatbot/data
   ```
2. 将训练数据（`medical_train.txt` 和 `medical_valid.txt`）放入上述目录  

### 模型训练
```bash
# 启动训练脚本
python /path/to/train.py --pretrained_model gpt2-medium
```
💡 支持自定义参数：`batch_size`、`learning_rate`、`epochs`  

### 启动交互
1. **命令行模式**  
   ```bash
   python interact.py
   # 输入问题，按 Ctrl+Z 结束对话
   ```
2. **Web界面模式**  
   ```bash
   python flask_predict.py
   # 访问 http://localhost:5000 开始对话
   ```

---

## 📂 项目结构
```plaintext
Gpt2_Chatbot/
├── data/                   # 训练数据
│   ├── medical_train.txt
│   └── medical_valid.txt
├── data_preprocess/        # 数据处理脚本
│   ├── preprocess.py
│   ├── dataset.py
│   └── dataloader.py
├── model/                  # 模型配置与预训练文件
│   ├── config.json
│   └── pytorch_model.bin
├── train.py                # 训练主程序
├── interact.py             # 命令行交互
└── flask_predict.py        # Web交互服务
```

---

## 🔧 核心模块详解

### 📊 数据处理流程
```mermaid
graph LR
A[原始数据] --> B(格式转换)
B --> C(向量编码)
C --> D[DataLoader封装]
```

### 🧠 模型架构
- **输入层**：词嵌入 + 位置编码  
- **核心层**：12层Transformer Decoder  
- **输出层**：概率分布生成回答  

```python
# 加载预训练模型
from transformers import GPT2LMHeadModel
model = GPT2LMHeadModel.from_pretrained("gpt2-medium")
```

---

## 📈 训练指标
| 指标         | 训练集 | 验证集 |
|--------------|--------|--------|
| 准确率       | 92.3%  | 88.7%  |
| 困惑度（PPL）| 15.2   | 18.6   |

---

## 💬 对话示例
**用户**: 帕金森叠加综合征的辅助治疗有哪些？  
**AI医生**: 🩺 推荐方案：  
1. 康复训练（如平衡练习）  
2. 生活护理指导（防跌倒措施）  
3. 低频重复经颅磁刺激治疗  

--- 

⭐ **如果觉得项目有用，欢迎Star支持！**  
