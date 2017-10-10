# Overview
This is a peer review of hypothesis exercise from HW3 CitiBike project.

# Comment on Prince Abunku's Submission (Git ID: princeaker) 
**Alternative Hypothesis**: Men and Women ride city bike for different average durations

**NULL Hypothesis**: Men and Women ride for equal duration

**Comments**:
I think Prince can reposition the hypothesis to have a more meaningful analysis. One way is to test if the average trip duration is shorter for male compare to the ones by female riders.
Testing if the average duration is exactly the same may be too specific.

**Data Validation**:
Prince created a dataset that includes "Trip Duration" and "Gender". This data provides sufficient information to test the hypothesis.

**Choice of Statistical Test**:
I'd choose a t-test because: 
- 1 independent variable with 2 levels ('male', 'female')
- 1 depenent variable (avg. trip duration) that is interval & normal

# Comments on Lingyi Zhang's Submission (Git ID: lz1714)
**Key Question**:
'Customer' are more likely than 'Subscriber' to use Citibike during working time (9a.m - 5p.m).

**NULL Hypothesis**:
The ratio of the 'Subscriber' biking during working hour over the whole day is the same or higher than the ratio of 'Customer' during working hour over the whole day.

**Alternative Hypothesis**:
Lingyi did not specify this. The alternative hypothesis can be "The ratio of the 'Subscriber' biking during working hour over the whole day is slower than the ratio of 'Customer' during working hour over the whole day."

**Data Validation**:
Lingyi provided absolute counts of trips by Substriber and customer of each hour. This is a good start. I think the following column is required to suppor the test:
- Hour (categorical: '9-5', 'other hours') 
- Ratio (trip count of subscriber / trip count of customer) 

**Choice of Statistical Test**:
I'd choose the t-test because: 
- 1 independent variable with 2 levels ('9-5', 'other hours')
- 1 depenent variable that is interval & normal

