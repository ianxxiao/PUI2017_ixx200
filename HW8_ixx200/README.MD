# Overview
I try to provide interactive visual insights of building age, energy use, and building configuration using Local Law 84 from 2013-2016 and PLUTO datasets. 

# Visualization
![Alt text](./screenshot.png?raw=true)

Link to the Interactive Visualization on Carto
https://ianxxiao.carto.com/viz/0d56359f-68ec-4e61-ae6e-1ae8a8c9ee7e/public_map

# Code
Please see the ipython notebook attached. It includes the following steps that generate the visualization dataset:
- data integration and cleaning
- feature engineering
- modelling
- export to CSV for uploading to Carto

# Limitation
There are 9,852 samples in my integrated dataset. Only 400 of these samples were render due to limited Carto credit for geo-fencing. Additional locationing from building address to lat/long was required.

# Contributor
- NA
