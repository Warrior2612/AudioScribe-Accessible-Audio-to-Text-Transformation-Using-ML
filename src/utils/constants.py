from enum import Enum

APP_NAME = "AudioScribe"
APP_LANGUAGES = {"en": "English"}

# Code languages convention: ISO 639-1
AUDIO_LANGUAGES = {
    "en": "English",
    "gu": "Gujarati",
    "hi": "Hindi",
    "mr": "Marathi"
}


AUDIO_FILE_EXTENSIONS = [
    ".mp3",
    ".mpeg",
    ".wav",
    ".wma",
    ".aac",
    ".flac",
    ".ogg",
    ".oga",
    ".opus",
]

# fmt: off
VIDEO_FILE_EXTENSIONS = [
    ".mp4", ".m4a", ".m4v", ".f4v", ".f4a", ".m4b", ".m4r", ".f4b", ".mov",  # MP4
    ".avi",  # AVI
    ".webm",  # WebM
    ".flv",  # FLV
    ".mkv",  # MKV
    ".3gp", ".3gp2", ".3g2", ".3gpp", ".3gpp2",  # 3GP
    ".ogv", ".ogx",  # OGG
    ".wmv", ".asf"  # AIFF / ASF
]
