# Project Title

The Nature of Long-Distance Travel and Implications for Disease Spread

## Description

These are five scripts for the simulation and experiments in the [project](#project-title).

The executing scripts are listed belows:

- **long-distance-modelling.ipynb**
  
  This script is primarily used for long distance travel modeling in the dataset. The functionality can be divided into 3 main sections:
  1. **Datasets Reading**: Reading, extracting and preprocessing datasets from empirical(original) data files. <br> The datasets used here are from Mobility in Germany survey (MiD) and the American National Household Travel survey (NHTS). More details about the [datasets](#datasets) can be found below.
  2. **Modelling the amplified power-law to long distance data**: Simulate the model by generating a large number of sampling trip lengths using different combinations of parameters. By comparing the distance (error) between the empirical data and the sampled trip lengths in the two data sets, an optimal set of model parameters can be found, then the optimal results will be stored as "Best results of LR Modelling in MiD17.pkl" or "Best results of LR Modelling in NHTS17.pkl" in the folder **results_mobility**.
  3. **Finding and save the best parameters for truncated power-law fitting**: Calculate the properties of the truncated power-law, find the optimal combination of parameters for truncated power law fitting. Then save the optimal results as "Optimal truncated power-law in MiD.pkl" or "Optimal truncated power-law in NHTS.pkl" in the folder **results_mobility**.
  4. **Comparing the optimal model and truncated power-law in long-distance public transport trips**:
  Show the comparsion by plotting CCDF of the optimal model, the optimal truncated power-law, a hand-picked truncated power-law and the empirical data for
  the long-distance travel in MiD and NHTS respectively.
  
- **short-distance-modelling.ipynb**
   - Caculate the power-law properties, plot the CCDF of it, show the power-law properties of different short and medium-distance transportation modes (i.e., MiD Walking, MiD Driving, NHTS Driving, NHTS Short Distance Public Transportation) in comparison to the empirical data. Check if power-law existed or not in these transportation modes.
   
- **testing-distributions.ipynb**: 

   - The script is an attempt to fit commonly used distributions (i.e.,'beta','expon','gamma','lognorm','powerlaw') to German long-distance data.

- **covid-heatmap.ipynb**
  - The script is used to read and process the 7-day incidence numbers of COVID in Germany from the Robert Koch Institute (RKI).
  - It generates German maps with the covid data (7-days incidences1.csv and 7-days incidences2.csv), coloring the regions with a sustained increase in incidence of at least 20% in four consecutive weeks.

- **flu-heatmap.ipynb**
  - This script is used for analyzing the influenza incidence numbers per seasonal week in Germany from RKI.(Data_flu.xlsx)
  - Similar to Levy-Covid19.ipynb, it can also generate German maps with provided influenza incidence numbers.

## Getting Started

### Environment and Dependencies

* Python version 3.11.3.
* Jupyter notebook
* Libraries: Numpy, Pandas, Matplotlib, Scipy, Seaborn, Fitter, Pyreadstat, Json, Geojson, CSV, Natsort, PIL, Statsmodels, Geopandas, Requests, Plotly, Shapelyy

### Datasets

1. MiD 2017: MiD2017_Wege.csv 
   * Mobility in Germany survey (MiD) data which was conducted in the year 2017
2. Nhts 2017: trippub_2017NHTS.csv
   * the American National Household Travel survey (NHTS)data, it collects on travel behavior in the United States
* Note: the above datasets are used in the long-distance and short-distance modelling scripts. The NHTS data is publicly available at https://nhts.ornl.gov/downloads directly. The MiD data needs to be requested via form at https://daten.clearingstelle-verkehr.de/order-form.html#223.
  
3. 7-days incidences1.csv and 7-days incidences2.csv
   * These two docs are the 7-day incidence for Covid in Germany from 18.11.2020 to 31.10.2022. These were used in the script Levy-Covid19.ipynb.
  
4. Data_flu.xlsx
   *  This doc was required from RKI https://survstat.rki.de/Content/Query/Create.aspx. It is the incidence value of Influenza(saisonal) from xxx to xxx, split by Saisonwoche.

5. geo_germany.pkl
    * The file contains the information for seting up the German maps.

* Note: the above datasets of point 3 and 5 are used in covid19 an flu heatmaps. For convenience, this data is provided in the 'data' folder.


### Executing program

* Download the scripts and dataset folder, open it in the Juypter notebook.
* Note: Please note the file paths used in the script and change them to suit your situation.
* Note: The folder sir-simulation contains scripts used to simulate the SIR model on a random geometric graph built upon points generated on a play field. Please fined more details in the readme file located in that ordner.

## Contact
Gregor Bankhamer - gbank@cs.sbg.ac.at <br>
Huiran Liu - huiran.liu@campus.tu-berlin.de
