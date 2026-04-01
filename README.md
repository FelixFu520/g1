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
export SETTINGS_PATH=/path/of/g1.json # 导入g1.json的路径到环境变量中
python 03_doubao_asr.py

# 豆包TTS
export SETTINGS_PATH=/path/of/g1.json # 导入g1.json的路径到环境变量中
python 04_doubao_tts.py

# g1聊天
export SETTINGS_PATH=/path/of/g1.json # 导入g1.json的路径到环境变量中
python g1.py

```
### ROS集成
`g1chat_node.py`是ros代码, 使用时需要修改集成