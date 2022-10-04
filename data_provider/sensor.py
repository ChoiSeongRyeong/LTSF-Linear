import os
from matplotlib import scale
import pandas as pd
import numpy as np

from dataclasses import dataclass
from pydantic import BaseModel
from torch.utils.data import Dataset

class SensorDataset_from_afile(BaseModel, Dataset):
    root_path: str
    data_path: str
    flag: str
    size: tuple
    features: str
    scale: bool
    timeenc: str
    freq: str

    def __post_init__(self):
        self._validate_init()
        type_map = {'train': 0, 'val': 1, 'test': 2}
        self.set_type = type_map[self.flag]
        self._read_data()
    
    def __len__(self):
        ...
    
    def __getitem__(self, idx):
        ...
    
    def _validate_init(self):
        assert self.flag in ['train', 'val', 'test']
        assert len(self.size) == 3
        assert self.features in ['M', 'S', 'MS']
    
    def _read_data(self):
        self.df = pd.read_csv(
            os.path.join(self.root_path, self.data_path)
        )
        ...