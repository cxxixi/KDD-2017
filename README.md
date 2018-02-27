## KDD-2017 TASK I
This project is for 2017 KDD CUP TASKI. Ranked top 4% at last.

## Prerequisites.
Env: Win10, Python 3
To run the files successfully on your own, you should install XGBoost on your environment.

## installing
#### Install XGBoost(win 10 in Python3)
`pip install xgboost`
[See more](http://blog.csdn.net/zyghs/article/details/50897716)

## Task prescription
#### Tasks
Available datasets are: the road network topology in the target area (Figures 1, 3, and 4, Tables 3 and 4), vehicle trajectories (Table 5), historical traffic volume at tollgates (Table 6), and weather data (Table 7).  The contest consists of two tasks with the details below.

#### Task 1:
To estimate the average travel time from designated intersections to tollgates. For every 20-minute time window, please estimate the average travel time of vehicles for a specific route (shown in Figure 1).  
   a. Routes from Intersection A to Tollgates 2 & 3;  
   b. Routes from Intersection B to Tollgates 1 & 3;  
   c. Routes from Intersection C to Tollages 1 & 3.  
Note: the ETA of a 20-minute time window for a given route is the average travel time of all vehicle trajectories that enter the route in that time window. Each 20-minute time window is defined as a right half-open interval, e.g., [2016-09-18 23:40:00, 2016-09-19 00:00:00).

#### Submission Format (see Table 1)
The data types used in all tables in this document are int, float, string, date and datetime.  The date and datetime comply with the formats “yyyy-MM-dd” and “yyyy-MM-dd HH:mm:ss”.  The time_window field consists of two datetime types separated by a comma without any blank, e.g., “2016-09-18 08:40:00,2016-09-18 09:00:00”.


![](https://img.alicdn.com/tps/TB1Mx8MPVXXXXbpXFXXXXXXXXXX-975-174.png)
Table 1. Travel Time from Intersections to Tollgates


## Running the files


## Acknowledgement
It's very grateful of GuoQiang Gong for his invaluable help in accomplishing the work






