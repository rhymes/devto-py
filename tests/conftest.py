# coding: utf-8

from pathlib import Path

import pytest
from vcr import VCR


@pytest.fixture(scope="session")
def vcr():
    return VCR(
        cassette_library_dir=str(Path(__file__).parent.joinpath("fixtures/cassettes")),
        decode_compressed_response=True,
        path_transformer=VCR.ensure_suffix(".yaml"),
        record_mode="once",
        filter_headers=["authorization"],
    )
