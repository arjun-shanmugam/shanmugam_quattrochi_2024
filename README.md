# Replication Instructions

## Setup
1. Clone this GitHub repository to your local machine
2. Create an empty directory called "data" in the repository on your local machine. Inside of this directory, create three directories: "raw", "intermediate", and "cleaned".
3. Create an empty directory called "output" in the repository on your local machine. Inside of this directory, create two directories: "figures" and "tables".

## Obtain Data
1. Download [Census Tract Shapfiles](https://bostonopendata-boston.opendata.arcgis.com/api/download/v1/items/4a8eb4fb3be44ed5a1eec28551b9f3b2/shapefile?layers=0)
2. Download [Opportunity Insights Census Tract Characteristics](https://opportunityinsights.org/data). You will need to visit this link and then search for 
3. Download [BPD Crime Incident Reports](https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system). You will need to visit this link and then filter by "Neighborhood Characteristics by Census Tract." Then, download the dataset as a CSV by clicking the "Excel" link.
4. Request and obtain Eviction Data: The underlying source dataset is public at MassCourts.org. It is however not downloadable from that domain in a research-ready way. Our research-ready dataset was produced by manually downloading case dockets over a period of several years. Massachusetts law makes it clear that names and addresses at MassCourts.org are not protected, but case law and pending legislation make it unclear whether our concentrated list of names and addresses suddenly would become protected. For this reason, out of an abundance of caution, we are limiting distribution to researchers with research intent. All reasonable applications will be accepted. We will facilitate transmission of addresses for reproduction. Please email hello@masslandlords.net to apply.

## Run Code
1. Create a Python virtual environment
2. Activate it and install the packages listed in the requirements.txt
3. In order, run 1_clean_evictions.py, 2_clean_census_tract_characteristics.py, 3_merge.ipynb, 4_summary_statistics.ipynb, 5_main_results.ipynb, being sure to set paths before running each file.



