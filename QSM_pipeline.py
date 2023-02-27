import os
import numpy as np
import pydicom
import nibabel as nib
import medpy.filter.smoothing as medpy_smooth

# define input and output directories
input_dir = '/path/to/input/dicom/folder'
output_dir = '/path/to/output/nifti/folder'

# define QSM to T2star to SWI pipeline functions
def qsm_to_t2star(input_file):
    # read DICOM file
    dicom = pydicom.dcmread(input_file)

    # extract QSM data from DICOM file
    qsm_data = dicom.pixel_array

    # convert QSM data to T2star data
    t2star_data = np.sqrt(qsm_data)

    return t2star_data

def t2star_to_swi(input_data):
    # smooth T2star data using a median filter
    smoothed_data = medpy_smooth.median(input_data)

    # compute SWI data
    swi_data = np.power(smoothed_data, 2)

    return swi_data

# iterate through DICOM files in input directory
for filename in os.listdir(input_dir):
    # skip non-DICOM files
    if not filename.endswith('.dcm'):
        continue

    # construct input and output file paths
    input_file = os.path.join(input_dir, filename)
    output_file = os.path.join(output_dir, filename.replace('.dcm', '.nii.gz'))

    # apply QSM to T2star to SWI pipeline
    t2star_data = qsm_to_t2star(input_file)
    swi_data = t2star_to_swi(t2star_data)

    # save SWI data to NIFTI file
    nifti_image = nib.Nifti1Image(swi_data, np.eye(4))
    nib.save(nifti_image, output_file)

print('Pipeline is completed!')