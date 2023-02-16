'''Script to generate the low resolution versions of the simulated data
for the first_level_fit_low_res_demo.ipynb example

run from the base directory of this repo:
    python reduce_res.py
'''

import numpy as np

from fsl_mrs.utils import mrs_io
from fsl_mrs.utils.preproc import nifti_mrs_proc as proc
from fsl_mrs.core import nifti_mrs as ntools


def block_average(data, indices):
    blocks = []
    for idx in indices:
        _, block = ntools.split(data, 'DIM_DYN', idx.tolist())
        blk_avg = proc.average(block, 'DIM_DYN')
        blocks.append(ntools.reorder(blk_avg, ['DIM_DYN', None, None]))
    return ntools.merge(blocks, 'DIM_DYN')


blk_indices = np.arange(0, 64).reshape(-1, 8)
print(blk_indices)

open_fullres = mrs_io.read_FID('simulated_data/sub0_stim.nii.gz')
block_average(open_fullres, blk_indices)\
    .save('simulated_data/low_res/lowres_stim.nii.gz')

closed_fullres = mrs_io.read_FID('simulated_data/sub0_ctrl.nii.gz')
block_average(closed_fullres, blk_indices)\
    .save('simulated_data/low_res/lowres_ctrl.nii.gz')
