# unitree G1 Robot Chat Library
本项目是宇树机器人G1的对话库

## 安装
### 硬件连接
[硬件相关](install.md)
### 本项目环境配置
```
sudo apt-get install portaudio19-dev
git clone https://github.com/FelixFu520/g1.git
cd g1
uv sync -p 3.8
```
## 配置
```
cd g1
mkdir -p ~/.config/g1
cp g1.json ~/.config/g1
cp g1_system_prompt_en.txt ~/.config/g1
cp g1_system_prompt_zh.txt ~/.config/g1
```
## 使用
### 源码测试
```
# 查找音频设备名
python 01_device_list.py

# 音频设备实时回环
python 02_test_AudioDevice.py

# 豆包ASR
G1_SETTINGS_PATH=/home/unitree/.config/g1/g1.json python 03_doubao_asr.py

# 豆包TTS
G1_SETTINGS_PATH=/home/unitree/.config/g1/g1.json python 04_doubao_tts.py

# 豆包LLM
G1_SETTINGS_PATH=/home/unitree/.config/g1/g1.json python 05_doubao_llm.py

# g1聊天
G1_SETTINGS_PATH=/home/unitree/.config/g1/g1.json python g1.py

```
### ROS集成
`g1chat_node.py`是ros代码, 使用时需要修改集成