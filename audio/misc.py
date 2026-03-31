import pyaudio
import wave
import uuid
import asyncio
import numpy as np
import websockets

from .logging import default_logger as logger
from .audio_device import AudioDevice


def list_audio_devices(device: str = "USB"):
    """返回匹配的音频设备列表。"""
    device_list = []

    p = pyaudio.PyAudio()
    try:
        for i in range(p.get_device_count()):
            dev = p.get_device_info_by_index(i)
            if device == "all":
                device_list.append(dev)
            elif device in dev["name"]:
                device_list.append(dev)
    finally:
        p.terminate()

    return device_list
