# FSL-MRS fMRS fitting demo for ISMRM 2022

This is the GitHub repository that accompanies the [FSL-MRS](https://open.win.ox.ac.uk/pages/fsl/fsl_mrs/) presentation given in the Member Initiated Symposium [_Functional MRS: Current Challenges & Cutting-Edge Methods_](https://submissions.mirasmart.com/ISMRM2022/Itinerary/ConferenceMatrixEventDetail.aspx?ses=MIS-08)
on Wednesday afternoon at [ISMRM 2022 (in London)](https://www.ismrm.org/22m/). This demo __Using all the Information: Fitting Functional MRS with a GLM__ is scheduled to start at 15:50.

The demo covers how to fit a set of (simulated) fMRS data, modelled on single voxel, visual stimulation experiments, using a GLM model and FSL-MRS's "dynamic fitting" tools.

The repository is an accompaniment to the talk given by Saad Jbabdi. The repo contains far more information / content about the setup of the demo than will be covered in the talk, for instance how the simulated data was created.

Saad and I (Will) had hopped to make this more polished, but family commitments for both of us has curtailed this ambition. We hope that as these tools mature in the future we can also have a more succinct demonstration of them here. The main casualty has been that the fMRS tools of FSL-MRS remain in a development version, hence the convoluted install instructions below. This should be resolved in the near future and in the meantime please get in touch for help installing either using the [issues page](https://github.com/wtclarke/fsl_mrs_fmrs_demo/issues) on this repo or on the [FSL JISC mailing list](mailto:FSL@JISCMAIL.AC.UK).

## Installation
_How to install FSL-MRS (dev version) and get the contents of this repo._
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
    git clone https://github.com/wtclarke/fsl_mrs_fmrs_demo.git
    ```

## Where to start
After installing the required FSL-MRS version (above), we'd recommend starting by looking at __main_demo.ipynb__ which follows the talk most closely.

Then if you want to try running the fitting for yourself take a look at __first_level_fit_low_res_demo.ipynb__ then __first_level_fit.py__. 

Finally, if you want to understand how the second level results are generated (in gory detail) see __second_level_analysis.ipynb__.

`.ipynb` files can be opened using Jupyter notebooks in a browser or e.g. VScode. Note that these use plotly plots for interactive elements, which sometimes needs some extra setup.

## What's in the repository
This is a summary of each file and directory in the repository. 

1. __Basis__ - the basis spectrum for fitting and used to simulate the data. This is a 36 ms sLASER basis.
2. __simulated_data/__ - simulated data of 10 subkects, each with a stimulated condition and a control condition (no stimulation). Each dataset contains 64 single-voxel spectra (in [NIfTI-MRS](https://github.com/wtclarke/mrs_nifti_standard) format). The 64 spectra are subdivided into 16-spectra blocks in a pattern of REST-STIM-REST-STIM (for stimulation condition) or REST-REST-REST-REST (no stimulation condition). This data is created by _generate_data.ipynb_. True simulation values are in true_values.csv in this directory.
3. __generate_data.ipynb__ - Generates the simulated data using a fixed random seed. See below for more information on the data generation.
4. __bednarik_table_1.csv__ - Summarises the main results (Table 1) of [Bednarik et al (2015)](https://journals.sagepub.com/doi/10.1038/jcbfm.2014.233). These results are used to inform the responses in the simulated data.
5. __gen_and_fit_window_avg_data.ipynb__ - This notebook simulates the Applies a windowed average (5 spectra) to the first subjects data, fits it and then saves the results to windowed_avg_results
6. __first_level_fit_low_res_demo.ipynb__ - Contains a complete demonstration of the single subject data using deliberately reduced resolution data (for speed of execution).This demo shows the user how to run the analysis using the interactive python code and the command line script packaged with FSL-MRS.
7. __first_level_fit.py__ Runs the first level analysis (as demonstrated in _first_level_fit_low_res_demo_) for all subjects, at full temporal resolution (i.e. 64 spectra). The results of this fit are saved in __first_level_results/__.
The design matrix and model for that are generated in _full_fit_setup.ipynb_.
8. __full_fit_setup.ipynb__ - Creates the design matrix and model file for the _first_level_fit.py_.
9. __second_level_analysis.ipynb__ -  Carries out the second level group analysis. This contains extensive code segments to pass the MRS fitting results through FSL's `FLAME` tool.
10. __main_demo.ipynb__ ...

## Data model
The simulated data was created according to the following recipe:

- All metabolite concentrations were set to the mean ± SD values reported in [Bednarik et al (2015)](https://journals.sagepub.com/doi/10.1038/jcbfm.2014.233), see _bednarik_table_1.csv_.
- Spectra were simulated using linewidths and SNRs to match the spectra in [Ip et al (2017)](https://doi.org/10.1016/j.neuroimage.2017.04.030).
- The 64 spectra of each dataset were subdivided into 16-spectra blocks in a pattern of REST-STIM-REST-STIM (for stimulation condition) or REST-REST-REST-REST (no stimulation condition)
- During stimulation blocks a HRF model was used to reduce the Gaussian linewidth component by 0.5 Hz.
- A HRF was used to model changes in Glu, Lac, Glc and Asp according to the results of [Bednarik et al (2015)](https://journals.sagepub.com/doi/10.1038/jcbfm.2014.233). The HRF of Asp is deliberately temporally delayed to simulate a (somewhat) unknown model.
- All other metabolites have no change during stimulation, but a random small linear drift is included.