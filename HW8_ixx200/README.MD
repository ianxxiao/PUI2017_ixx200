# Overview
This visualization provide insights about building age, energy use, and building configuration using Local Law 84 from 2013-2016 and PLUTO datasets. 

# Visualization
![Alt text](./screenshot.png?raw=true)

**Caption**: This is a map of 400 NYC buildings from Local Law 84. It highlights areas with older buildings using color coding. Many older buildings scatter near Central Park, midtown Manhattan, and core areas in Bronx, Queens, and Brooklyn. Additional information about energy consumption behaviour and building configuration can be found when hover over each sample. 

Link to the Interactive Visualization on Carto

https://ianxxiao.carto.com/viz/0d56359f-68ec-4e61-ae6e-1ae8a8c9ee7e/public_map

# Limitation
There are 9,852 samples in my integrated dataset. However, additional locationing to convert building address to latitude/longtitude was needed. This required paid Carto feature. Only 400 of these samples were rendered due to limited Carto credit for geo conversion.

# Code
Please see the ipython notebook attached. It includes the following steps that generate the visualization dataset:
- data integration and cleaning
- feature engineering
- modelling
- export to CSV for uploading to Carto

# Contributor
- NA

-----

# Dana's Comments for Ian's plot, HW9:

Overall, the plot is esthetic and the colors are clear and accessible also to blind-color people. The plot has no title, which would have been helpful to better understand it. Few more thoughts of how to improve the plot:
- **Clarity:** The frame with the explenation of what does the map say is somewhat problematic; First, it bothers the map, in the static + interactive view (and when openning the link in small chrome window it overlaps the data observed - see [appendix A](https://github.com/danachermesh/PUI2017_dcr346/blob/master/HW9_dcr346/Screen%20Shot%202017-11-19%20at%2019.54.54.png)). Then, it is misleading - the **graphics** do not contain all the information that is reported, it is only delivered to the viewer as plain text. The graphics itself only tell us about the **age** of the buiilding.<br>
In this sense, it could have been better to write this information in the caption.
interactive map the quantities being visualized ambiguous?
- **Esthetic:** The plot is esthetic and clear. Though, using _dots_ as the graphic elements conects in my head to incidents / observations and not to a geographical entity such as buildings. It could have been better to color the lots of the buildings in the dataset, as in [appendix B](https://github.com/danachermesh/PUI2017_dcr346/blob/master/HW9_dcr346/Screen%20Shot%202017-11-19%20at%2018.47.51.png) (screenshot was taken from [New York City Energy 
& Water Performance Map](https://serv.cusp.nyu.edu/projects/evt/). The red color map selected is a good and reasonable choice when representing building age data, the continious legend is a good choice as well and honesty represents the data.

### Appendix A: overlapping text frame
![alt text](https://github.com/danachermesh/PUI2017_dcr346/blob/master/HW9_dcr346/Screen%20Shot%202017-11-19%20at%2019.54.54.png)

### Appendix B: Refference to lot-colored map
![alt text](https://github.com/danachermesh/PUI2017_dcr346/blob/master/HW9_dcr346/Screen%20Shot%202017-11-19%20at%2018.47.51.png)
