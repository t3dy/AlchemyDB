import os
import yaml
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG_PATH = Path("config/settings.yaml")

class Config:
    def __init__(self, data: Dict[str, Any]):
        self.corpus_path = data.get("corpus_path", "./pdf")
        self.db_path = data.get("db_path", "./data/archive.db")
        self.exports_path = data.get("exports_path", "./exports")
        self.chunk_size = data.get("chunk_size", 1000)
        self.chunk_overlap = data.get("chunk_overlap", 150)
        self.enable_entity_extraction = data.get("enable_entity_extraction", False)
        self.enable_topic_extraction = data.get("enable_topic_extraction", False)
        
        self._validate()

    def _validate(self):
        """Simple validation for the configuration paths and values."""
        if not isinstance(self.chunk_size, int) or self.chunk_size <= 0:
            raise ValueError(f"chunk_size must be a positive integer, got {self.chunk_size}")
        if not isinstance(self.chunk_overlap, int) or self.chunk_overlap < 0:
            raise ValueError(f"chunk_overlap must be a non-negative integer, got {self.chunk_overlap}")
        if self.chunk_overlap >= self.chunk_size:
            raise ValueError("chunk_overlap must be less than chunk_size")

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

def load_config(config_path: str = None) -> Config:
    path = Path(config_path) if config_path else DEFAULT_CONFIG_PATH
    
    if not path.exists():
        print(f"Warning: Configuration file {path} not found. Using defaults.")
        return Config({})
        
    with open(path, "r") as f:
        try:
            data = yaml.safe_load(f) or {}
            return Config(data)
        except yaml.YAMLError as e:
            print(f"Error parsing configuration file {path}: {e}")
            raise
