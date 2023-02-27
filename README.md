# BF-QSM
## This is a Sequence pipeline which takes Dicom files as input and converts those into NIFTI files involving the below steps.

### It includes use of Packages like pydicom,nibabel, medpy.filter.smoothing

Steps :-

  Step 1 : Setting paths to input and output directories. 
  Step 2 : Defining qsm_to_t2star function which takes DICOM files as inputs.  
  Step 3 : Defining t2_star to SWI function which takes t2star data as input. 
  Step 4 : Now iterate through all the DICOM files and call the step2, step3 respectively  
  Step 5 : Store the SWI data files which is of the format NIFTI. 
  Step 6: Pipeline is finished
  
    
  Note : Suggestions and changes are encouraged if it is necessary
