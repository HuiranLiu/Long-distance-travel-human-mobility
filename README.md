# Project Title

The Nature of Long-Distance Travel and Implications for Disease Spread

## Description

These are scripts for the simulation and experiments in the [project](#project-title).

The executing scripts are listed belows:

- **Levy-Mobility.ipynb**
  - This script is mainly for coping with data sets of trips in the German MiD and the American NHTS. The function of this script can be separted in 4 main parts:
  1. **Datasets Reading**: Used to reading four datasets, analyse the datasets simply, like extract and preprocess datasets from original data files, plotting the complementary cumulative distribution function (CCDF) of data sets itself, etc. <br> Four datasets used here are from Mobility in Germany survey (MiD) and the American National Household Travel survey (NHTS). More details about the [datasets](#datasets) can be found below.
  2. **Modelling**: Simulate the model by generating a large number of sampling trip lengths using different combinations of parameters. By comparing the distance (error) between the empirical data and the sampled trip lengths in the two data sets, an optimal set of model parameters can be found for our project.
  3. **Comparison with power-law properties**: Show the distance distributions of trips from Germany (MiD) and the U.S. (NHTS) for different transport mode. Comparing these distributions with a power-law model $F (x) = b(\frac{1}{x} )^{α−1}$.
  4. **Comparison with truncated power-law properties**: Calculate the properties of the truncated power-law and generate truncated power law lines for different configurations to find the best fit. Then compare it to long-distance travel in MiD and NHTS,i.e., the original distance distribution and modeling results from our work.
  5. **Finding possible distributions in MiD 2017 that fit the long distance of the data**: In this script, you can also find an attempt to find fitting commonly used distributions to German long distance data.

- **Levy-Covid19.ipynb**
  - The script is used to read and process the 7-day incidence numbers of COVID in Germany from the Robert Koch Institute (RKI).
  - It generates German maps with the covid data (7-days incidences1.csv and 7-days incidences2.csv), coloring the regions with a sustained increase in incidence of at least 20% in four consecutive weeks.

- **Levy-Flu.ipynb**
  - This script is used for analyzing the influenza incidence numbers per seasonal week in Germany from RKI.(Data_flu.xlsx)
  - Similar to Levy-Covid19.ipynb, it can also generate German maps with provided influenza incidence numbers.

## Getting Started

### Environment and Dependencies

* Python version 3.11.3.
* Jupyter notebook
* Libraries: Numpy, Pandas, Matplotlib, Scipy, Seaborn, Fitter, Pyreadstat, Json, Geojson, CSV, Natsort, PIL, Statsmodels, Geopandas, Requests, Plotly, Shapelyy

### Datasets

1. MiD 2008: MiD2008_PUF_Wege.sav 
   * Mobility in Germany survey (MiD) data which was conducted in the year 2008
2. MiD 2017: MiD2017_Wege.csv 
   * Mobility in Germany survey (MiD) data which was conducted in the year 2017
3. Nhts 2009: DAYV2PUB_2009NHTS.csv
   * the American National Household Travel survey (NHTS)data, it collects on travel behavior in the United States
4. Nhts 2017: trippub_2017NHTS.csv
   * the American National Household Travel survey (NHTS)data, it collects on travel behavior in the United States
* Note: the above four datasets are used in the script Levy-Mobility.ipynb, since it's a bit too large,  you can get the NHTS data from  https://nhts.ornl.gov/downloads directly. Regarding MiD data, you need ask from https://daten.clearingstelle-verkehr.de/order-form.html#223.
  
5. 7-days incidences1.csv and 7-days incidences2.csv
   * These two docs are the 7-day incidence for Covid in Germany from 18.11.2020 to 31.10.2022. These were used in the script Levy-Covid19.ipynb.
  
6. Data_flu.xlsx
   *  This doc was required from RKI https://survstat.rki.de/Content/Query/Create.aspx. It is the incidence value of Influenza(saisonal) divided by Saisonwoche. 

7. sehr_hoch.geo.json
    * json file contains the information for seting up the German maps.

* Note: the above datasets 5,7 and 6,7 are used in the script Levy-Mobility.ipynb and Levy-Flu.ipynb separately, you can find them in the folder 'data'.


### Executing program

* Download the scripts and dataset folder, open it in the Juypter notebook. Just executing each block is fine.
* Note: Please note the file paths used in the script and change them to suit your situation.
* Note: the folder **sir-simulation** contains scripts used to simulate the SIR model on a random geometric graph built upon points generated on a play field. Please find more details over there.

## Contact
Gregor Bankhamer - gregor_stefan.bankhamer@stud.sbg.ac.at <br>
Huiran Liu - huiran.liu@campus.tu-berlin.de
