# Project 2: Predicting Soccer Transfer Prices <u></u>
###### 

## Using information about player and league attributes, I built a model to predict player transfer prices into top European leagues.

I started by scraping all transfer data from Transfermarkt from 1997 until 2020 using scrapy. I then cleaned the data and combined with the FIFA kaggle data matching on name and date. This restricted the data years to those in the FIFA set. 

### Data:

 * **acquisition**:  I used data from 3 sources for my model
   1. **<u>Transfermarkt</u>**:  time and amount for over 100,000 transfers from 1997 to present
   2.  **<u>UEFA:</u>**  historic data for country club coefficients
   3.  **<u>Kaggle:</u>** player FIFA attribute data set
 * **storage**: JSON, CSV, sqlite database

### Skills:

 * `Beautiful Soup` and `Selenium` for UEFA data
 * `Scrapy` for Transfermarkt data
 * `numpy` and `pandas`
 * `statsmodels`, `scikit-learn`
 * `sqlite` 


### Analysis:

![image-20201012195251944](C:\Users\Meehir\AppData\Roaming\Typora\typora-user-images\image-20201012195251944.png)