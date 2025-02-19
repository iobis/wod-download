from siphon.catalog import TDSCatalog
import requests
import os
import logging


def download_datasets_from_catalog(catalog: TDSCatalog, output_path: str):
    logging.info(f"Downloading datasets from {catalog.catalog_name}...")

    for dataset_name, dataset in catalog.datasets.items():
        dataset_url = dataset.access_urls["HTTPServer"]

        if dataset_url:
            logging.info(f"Downloading {dataset_name}...")
            response = requests.get(dataset_url, stream=True)

            file_path = os.path.join(output_path, dataset_name)
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            logging.info(f"Saved: {file_path}")

    for catalog_ref_name, catalog_ref in catalog.catalog_refs.items():
        download_datasets_from_catalog(catalog_ref.follow(), output_path)


logging.basicConfig(level=logging.INFO)
output_path = "wod_data"
catalog_url = "https://www.ncei.noaa.gov/thredds-ocean/catalog/ncei/wod/catalog.xml"
catalog = TDSCatalog(catalog_url)
os.makedirs(output_path, exist_ok=True)
download_datasets_from_catalog(catalog, output_path)
