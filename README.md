# RAPID - v3.2

## Inputs

All the inputs can be found in the folder called 'inputs'

Compatibility : 

1. **OPERATIONAL DATA:** Operational_data.csv
2. **INPUT FILE:** Input_File_RAPID_v3.0
3. **SCHEDULE:** Schedule_File_RAPID_v3.0

**Make sure the utility folder contains:**

- actual_speed_profile.csv (for the version when the actual speed profiles filtering is not available)
- RECAT_EU_separation.csv
- RECAT_PWS.csv
- RECAT20_separation.csv
- UK_wake_separation.csv
- wake.csv

## Outputs

1. utility/AROTDROT_distributions.csv
2. Input_File_RAPID_v3.0_ + (time) + .xlsx
3. OUTPUT_RAPID_v3.0_ + str(output_extension) +  '.xlsx'

## Developer Notes

### 1. Install miniconda

See https://conda.io/projects/conda/en/latest/user-guide/install/index.html

### 2. Setup conda environment

Open the Anaconda Prompt and enter the following to create a new conda environment exclusively for RAPID:

```
conda create --name rapid python==3.7.6
```

Enter the new environment:

```
conda activate rapid
```

Install the packages listed in requirements.txt (make sure you are in the correct directory):

```
conda install --file requirements.txt
```

### Misc

To generate requirements.txt type in console:
```
pip freeze > requirements.txt
```

To check duplicate code blocks using CPD:
```
cd /d/pmd-bin-6.35.0/bin

./cpd.bat --minimum-tokens 75 --files /d/Bonobo\ Git\ Server/RAPID/RAPID_v3.1_resize.py --language python > /d/Bonobo\ Git\ Server/RAPID/duplicates.txt
```

## References

Useful guide for openpyxl here: https://automatetheboringstuff.com/chapter12/
