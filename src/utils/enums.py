from enum import Enum


class AudioSource(Enum):
    FILE = "file"
    MIC = "mic"


class TranscriptionMethod(Enum):
    WHISPERX = 0
    GOOGLE_API = 1


class Color(Enum):
    LIGHT_RED = "#D30000"
    DARK_RED = "#8b0000"
    HOVER_LIGHT_RED = "#BF0000"
    HOVER_DARK_RED = "#610000"

    LIGHT_BLUE = "#3B8ED0"
    DARK_BLUE = "#1F6AA5"
    HOVER_LIGHT_BLUE = "#36719F"
    HOVER_DARK_BLUE = "#144870"


class ComputeType(Enum):
    INT8 = "int8"
    FLOAT16 = "float16"
    FLOAT32 = "float32"


class ModelSize(Enum):
    TINY = "tiny"
    BASE = "base"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE_V1 = "large-v1"
    LARGE_V2 = "large-v2"
    LARGE_V3 = "large-v3"
