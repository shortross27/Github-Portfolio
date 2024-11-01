# Exploratory Data Analysis of NYC TLC Data
## EXECUTIVE SUMMARY | COMMISSION PREPARED BY AUTOMATIDATA 


## Overview
The NYC Taxi & Limousine Commission has contracted with Automatidata to build a regression model that predicts taxi cab ride fares. In this part of the project, the data needs to be analyzed, explored, cleaned, and structured prior to any modeling.

## The Problem
After running initial exploratory data analysis (EDA) on a sample of the data provided by New York City TLC, some of the data will prove an obstacle for accurate ride fare prediction.
Namely, trips that have a total cost entered, but a total distance of “0.” At this point, our analysis indicates these to be anomalies or outliers that need to be factored into the algorithm or removed completely.

## The Solution
After analysis, I recommend removing outliers with a total distance recorded of 0. Highlights
As a result of the conducted exploratory data analysis, I considered trip distance and total amount as key variables to depict a taxicab ride. 
The provided scatter plot shows the relationship between the two variables. This scatter plot was created in Tableau to enhance the provided visualization.

<p align="center">
    <img width="200" src="https://github.com/user-attachments/assets/948e78d0-2387-49ab-ac6a-1b57f804f298"
 alt="Graph displaying New York City TLC data plotting variables for total distance and total amount.">
</p>
