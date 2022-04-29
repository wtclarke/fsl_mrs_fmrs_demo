# FSL-MRS fMRS fitting demo for ISMRM 2022

## Installation
1. Install the development version of FSL-MRS. You will need a [conda installation and environment](https://open.win.ox.ac.uk/pages/fsl/fsl_mrs/conda.html#conda).
    ```
    git clone -b enh/v2_dynamic_update --single-branch https://git.fmrib.ox.ac.uk/wclarke/fsl_mrs.git
    cd fsl_mrs
    conda install -c conda-forge -c defaults \
                -c https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/public/ \
                --file requirements.txt
    pip install --no-deps -e .
    ```
2. Clone this repository
    ```
    git clone ...
    ```