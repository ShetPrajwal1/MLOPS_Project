import os
import ssl
import urllib.request as request
import zipfile
from pathlib import Path
from src.ML_PROJECT.entity.config_entity import (DataIngestionConfig)

from src.ML_PROJECT import logger
from src.ML_PROJECT.utils.common import get_size


ssl._create_default_https_context = ssl._create_unverified_context

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(
                f"{filename} download completed with following info: \n{headers}"
            )
        else:
            logger.info(
                f"File already exists of size: "
                f"{get_size(Path(self.config.local_data_file))}"
            )

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
