# Copyright (c) 2024, NVIDIA CORPORATION & AFFILIATES
#
# SPDX-License-Identifier: BSD-3-Clause

import glob
import os

import pytest

from ..test_utils import run_sample

samples_path = os.path.join(
    os.path.dirname(__file__), '..', '..', '..', 'samples', 'densitymat')
sample_files = glob.glob(samples_path+'/**/*.py', recursive=True)


@pytest.mark.parametrize("sample", sample_files)
class TestcuDensityMatSamples:

    def test_sample(self, sample):
        run_sample(samples_path, sample)
