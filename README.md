# Mobility

The goal of this project is to draw maps that show the average number of 7-day incidence rate of Covid-19 cases per week in German, and to study and modelling the human’s mobility that how people travelled by public long-range transport, based on the data from two surveys: Mobility in Germany (MiD) and National Household Travel Survey (NHTS) datasets in the year of 2017

## Instructions on How to use these two code scripts  
1.  ***Covid19-cleaned.ipynb*** which helps to plotting maps with a certain colouring scheme.
- The script works with the original data files ***7-days incidences1.csv*** and  ***7-days incidences2.csv***, which are in the data folder.
- For plotting maps, you just need to look at the code block called “**Create map**”. It uses the data file  ***gis_incidences_nona.pkl*** used here. But this file was produced by  ***average 7-days incidences.csv*** and ***sehr_hoch.geo.json***. For simplicity, I removed the part where I processed and created this data file, but if you need it, please let  me know.

2.  ***Mobility_Levy-cleaned.ipynb*** is for studying and making models of the data in MiD17 and Nhts17.
