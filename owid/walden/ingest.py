"""Tools to inges to Walden and Catalog."""


from .catalog import Dataset
from .ui import log


def add_to_catalog(metadata: dict, filename: str, upload: bool = False):
    """Add metadata to catalog.

    Additionally, it computes the md5 hash of the file, which is added to the metadata file.

    TODO: Add checks of fields.

    Args:
        metadata (dict): Dictionary with metadata.
        local_path (str): Path to local data file. Used to compute the md5 hash.
    """
    # checksum happens in here, copy to cache happens here
    dataset = Dataset.copy_and_create(filename, metadata)

    if upload:
        # add it to our DigitalOcean Space and set `owid_cache_url`
        dataset.upload(public=True)

    # save the JSON to the local index
    dataset.save()

    log("ADDED TO CATALOG", f"{dataset.relative_base}.json")
