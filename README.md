# EDA and Hypothesis Testing

## Overview
In this part of the project, I analyzed the merged football player dataset for the 2019 season. The dataset brings together player market values, league information, performance statistics, and FIFA player attributes.

## Data Preparation
Before starting the analysis, I cleaned the dataset so it would be easier to work with.

The main steps were:
- removing unnamed columns that appeared during export,
- converting the **market value** column from text format (such as `€120.00m`) into numeric format,
- checking and cleaning league labels,
- and removing missing values only when they caused problems for specific tests.

After cleaning, the final dataset had **244 rows** and **155 columns**.

## Exploratory Data Analysis

### Market Value Summary
First, I looked at the basic summary statistics of the **market value** variable.

- **Count:** 244  
- **Mean:** 33.15  
- **Standard deviation:** 20.01  
- **Minimum:** 16.00  
- **Median:** 25.25  
- **Maximum:** 120.00  

These numbers show that market values are spread out quite a lot. There are many players with moderate values, while a smaller number of very expensive players pull the average upward.

### Average Market Value by League
Then I compared the average market value across leagues.

- **La Liga:** 44.46  
- **Premier League:** 36.75  
- **Bundesliga:** 33.97  
- **Serie A:** 27.67  
- **Ligue 1:** 25.34  

From these averages, La Liga had the highest player values in this dataset, followed by the Premier League. Ligue 1 had the lowest average among the leagues included here.

### Visual Exploration
To support the analysis, I created several graphs:
- a histogram of market value,
- a bar chart showing average market value by league,
- a boxplot comparing market value distributions across leagues,
- a scatter plot of age versus market value,
- and a scatter plot of goals scored versus market value.

These graphs were useful for seeing the overall distribution of values and spotting possible patterns between player characteristics and market value.

## Hypothesis Testing 1

### Research Hypothesis
For the first test, I focused on league differences.

- **Null hypothesis (H0):** There is no statistically significant difference between the average market values of Premier League players and players in other leagues.  
- **Alternative hypothesis (H1):** There is a statistically significant difference between the average market values of Premier League players and players in other leagues.  

### Test Method
I used an **independent two-sample t-test** to compare:
- players from the **Premier League**
- and players from **all other leagues combined**

### Test Results
- **Premier League sample size:** 75  
- **Other leagues sample size:** 169  
- **t-statistic:** 1.6568  
- **p-value:** 0.1004  

### Interpretation
Since the p-value (**0.1004**) is greater than **0.05**, I could not reject the null hypothesis.

So, based on this dataset, there is no statistically significant difference between the average market values of Premier League players and players in other leagues.

Even though Premier League players seem to have relatively high market values on average, the difference is not strong enough to be statistically significant at the 5% level.

## Hypothesis Testing 2

### Research Hypothesis
The second test looked at age.

- **Null hypothesis (H0):** There is no statistically significant relationship between player age and market value.  
- **Alternative hypothesis (H1):** There is a statistically significant relationship between player age and market value.  

### Test Method
I used a **Pearson correlation test** to measure the relationship between:
- **player age**
- and **player market value**

This test is suitable because both variables are numerical.

### Test Results
- **Sample size:** 196  
- **Correlation coefficient:** 0.1089  
- **p-value:** 0.1285  

### Interpretation
Since the p-value (**0.1285**) is greater than **0.05**, I could not reject the null hypothesis.

This means that there is no statistically significant relationship between player age and market value in this dataset.

The correlation coefficient is positive, but it is very weak, so age by itself does not seem to explain market value very well in this sample.

## Hypothesis Testing 3

### Research Hypothesis
The third test focused on goal scoring.

- **Null hypothesis (H0):** There is no statistically significant relationship between goals scored and market value.  
- **Alternative hypothesis (H1):** There is a statistically significant relationship between goals scored and market value.  

### Test Method
Again, I used a **Pearson correlation test**, this time for:
- **goals scored**
- and **player market value**

### Test Results
- **Sample size:** 194  
- **Correlation coefficient:** 0.4219  
- **p-value:** 8.94e-10  

### Interpretation
Since the p-value (**8.94e-10**) is much smaller than **0.05**, I rejected the null hypothesis.

This means there is a statistically significant relationship between goals scored and market value.

The correlation coefficient (**0.4219**) shows a moderate positive relationship, which suggests that players who score more goals generally tend to have higher market values. Compared to the age analysis, this relationship is clearly stronger.

## Limitations
There are still some limitations in this analysis.

First, the dataset only covers **one season (2019)**, so it does not show how players move between leagues over time. If the data included multiple seasons such as 2017, 2018, and 2019, it would be possible to study league changes in a more complete way.

Second, player market value is affected by many things that are not fully included here, such as injuries, contracts, popularity, and club transfer strategies.

## Conclusion
Overall, the EDA showed that player market values differ across leagues, with La Liga and the Premier League having the highest averages in this dataset.

However, the hypothesis tests gave mixed results:
- the Premier League vs. other leagues comparison was **not statistically significant**,
- the relationship between age and market value was also **not statistically significant**,
- but the relationship between goals scored and market value was **statistically significant and positive**.

So, based on this dataset, league and age alone are not enough to explain market value clearly, while goal-scoring performance seems to be a more useful indicator.


## Machine Learning - Predicting Market Value

In this part of the project, we tried to predict players’ market value using their performance statistics.

We tested two different models:
- Linear Regression
- Random Forest

To evaluate the models, we used:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² score

Here are the results:

| Model              | MAE   | RMSE  | R²   |
|-------------------|------|-------|------|
| Linear Regression | 9.75 | 12.06 | 0.39 |
| Random Forest     | 9.60 | 12.65 | 0.33 |

From the results, Linear Regression performs slightly better, especially in terms of R² and RMSE.

However, both models have relatively low R² scores. This means that performance stats alone are not enough to fully explain a player’s market value.

So, market value is probably influenced by other factors as well, like popularity, the league they play in, or transfer market conditions.

Overall, the models provide a basic understanding of market value prediction, but further improvements could be made by including more features such as player position, team performance, and historical transfer data.