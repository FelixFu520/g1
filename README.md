# unitree G1 Robot Chat Library
本项目是宇树机器人G1的对话库

## 安装
```
sudo apt-get install portaudio19-dev
git clone https://github.com/FelixFu520/g1.git
cd g1
uv sync -p 3.8
```
## 配置
```
cd g1
cp g1.json ~/.config/
```
## 使用
### 源码测试
```
# 查找音频设备名
python 01_device_list.py

# 音频设备实时回环
python 02_test_AudioDevice.py

# 豆包ASR
python -m g1chat.tools.check_audio_device

# 豆包TTS
python 04_doubao_tts.py

# g1聊天
python g1.py

```
### ROS集成
`g1chat_node.py`是ros代码, 使用时需要修改集成