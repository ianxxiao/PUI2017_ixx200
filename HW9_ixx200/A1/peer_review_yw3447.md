# Overview
This is a peer review of YuKun's visualization submission provided by Ian Xiao (ixx200). This review includes the following:
- CLARITY: is the plot easy to read? is it clear or confusing, are the quantities being visualized ambiguous?
- ESTHETIC: beautiful is a subjective judgment: you should not judge the plot on the basis of whether you think it is "beautiful", but you should judge whether its esthetic is functional to what it is meant to communicate. Are the colors chosen appropriately? Are the graphical elements used appropriate to represent the quantities being visualized? Are the graphical choices allowing you to focus on the right elements or are they distracting you?
- HONESTY: is the plot honestly reproducing the data or is it deforming it, perhaps to emphasize a point?

# Original Visualization

![Alt text](./yw3447_plot.png?raw=true)

# Clarity
YuKun's plot is easy to read overall. It is obvious that she's trying to show the different energy consumption behaviour and efficiency across regions in NYC. 

There are two improvements Yukun can make. One is to align the color palette between the graph and legend. For example, the black in the legend is showing up as grey in the graph. I was wonder what grey stands for. It took me a moment to realize the color grading difference. Secondly, she can add the Latitude and Longtitude labels to the axis.

# Esthetic
YuKun can consider using a different color palette, such as red for high EUI and green for the low ones. I believe the underlying message Yukun wants to carry out is that some areas have more concerning energy efficiency issues. Red usually signals "problems" while green stands for "normal". 

# Honesty
Yukun removed outliers by selecting samples with EUI between 0 and 1000 (not inclusive). This is a good preliminary approach for quick exploration and developing an end-to-end working script. However, more justification of this cut off should be discussed. Another approach to remove outliers that Yukun can consider is by clipping the dataset using percentiles. For example, she can remove samples, on an EUI basis, that are in the bottom 5 and top 95 percentiles.

In addition, some sort of normalization should be considered when comparing EUI on a Zip level. The number of reporting buildings vary largely by Zip Code. The average EUI may be only represented by a few buildings, which is under-representing, in some Zip area. 

There are two simple workarounds: one is to visualize the actual EUI on a building level, instead of Zip area level, considering the amount of buildings in this analysis is still managable. Creating and displaying new labels of sample sizes in each Zip area is the second option. This provides readers have all the information so that they can avoid any misleading conclusions.
