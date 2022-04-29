"""This script carries out the first level single-subject fMRS fits.
The script iterates over each of the 13 subjects, either in series
(warning slow!) or in parrallel using a cluster queue submission syntax.
Fits are carried out for both the eyes-open and eyes-closed data identically.

W T Clarke, University of Oxford, April 2022.
"""

import argparse
from subprocess import check_call
from pathlib import Path

parser = argparse.ArgumentParser(
    description='Run first-level dynamic fMRS fitting.')
parser.add_argument('--parallel', action='store_true',
                    help='Run in cluster job submission mode')
args = parser.parse_args()

if not args.parallel:
    print('This will take a long time run like this!')


def cmd_series(path, output):
    return ['fsl_dynmrs',
            '--data', str(path),
            '--basis', 'basis',
            '--dyn_config', 'fmrs_model.py',
            '--time_variables', 'designmat.csv',
            '--baseline_order', '0',
            '--metab_groups', 'Mac',
            '--output', str(output),
            '--report',
            '--overwrite']


def cmd_parallel(pathin, output):
    return ['fsl_sub', '-q', 'short.q'] + cmd_series(pathin, output)


base_path = Path('simulated_data')
our_dir = Path('first_level_results')
our_dir.mkdir(exist_ok=True)

for sub in range(10):
    sub_str = f'sub{sub:0.0f}'
    path_stim = base_path / (sub_str + '_stim.nii.gz')
    path_ctrl = base_path / (sub_str + '_ctrl.nii.gz')

    (our_dir / sub_str).mkdir(exist_ok=True)
    out_stim = our_dir / sub_str / 'stim'
    out_closed = our_dir / sub_str / 'ctrl'

    if args.parallel:
        check_call(
            cmd_parallel(path_stim, out_stim))
        check_call(
            cmd_parallel(path_ctrl, out_closed))
    else:
        check_call(
            cmd_series(path_stim, out_stim))
        print(f'Subject {sub}: stim done.')
        check_call(
            cmd_series(path_ctrl, out_closed))
        print(f'Subject {sub}: ctrl done.')
        print(f'Subject {sub+1}/10 done.')
