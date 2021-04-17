# Problem Statement:

## A company that flips houses has hired me to to analyze housing data in Ames, IA to determine the most cost-effective remodeling targets to quickly build equity in houses. They want me to specifically identify features to look for in buying houses (that typically lower a house's sale price) and what exactly to improve before selling to get the best return on their investment.

### Half of this project aims to answer the above problem statement, the other half was concerned with a Kaggle competition


## Datasets Used

* [`train.csv`](./datasets/train.csv): Ames housing data, training set
* [`test.csv`](./datasets/test.csv): Ames housing data, test set
* [`train_cleaned.csv`](./datasets/train_cleaned.csv): Initial cleaning/feature engineering attempt for Kaggle submission (train data)
* [`test_cleaned.csv`](./datasets/test_cleaned.csv): Initial cleaning/feature engineering attempt for Kaggle submission (test data)
* [`train_clean_2.csv`](./datasets/train_clean_2.csv): Second attempt cleaning/feature engineering for Kaggle
* [`train_clean_3.csv`](./datasets/train_clean_3.csv): Third iteration of cleaning, specifically for problem statement satisfaction
* [`prediction_1.csv`](./datasets/prediction_1.csv): First submission to Kaggle
* [`prediction_2.csv`](./datasets/prediction_2.csv): Second submission to Kaggle


## [Data Dictionary](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)


## Preliminary findings from our modeling are as follows:

#### Firstly, this model had an RMSE of 32,287. That means all of our findings will be +-$32,287

These were our highest-correlated features:

1. Wood siding vs. Hardboard siding

    -*All else being equal*, we can reasonably expect that wood siding will reduce the sale price of a home (compared to hardboard siding) by about \$9354
    
2. Composite shingle roof vs. other

    -This one is kinda tough to interpret. Only ~1\% of our dataset was not composite shingles, so I think it's safe to assume that we have an outlier somewhere with a non-shingled roof, worth about $6711 more than our average composite shingled house
    
3. Enclosed porch

    -*All else being equal*, we can reasonably expect that a house with an enclosed porch is worth about $5415 less than a house with no porch at all.
    
4. Plywood siding

    -*All else being equal*, we can reasonably expect that plywood siding will reduce the sale price of a home (compared to hardboard siding) by about \$5160
    
5. Stone masonry veneer vs. common brick
    
    -*All else being equal*, we can reasonably expect that a house with stone masonry on the exterior will sell for about $26283 more than a house with common brick veneer
    
6. No masonry vs. common brick

    -*All else being equal*, and interestingly, we can expect that a house with no masonry at all will sell for about $19024 more than a house with common brick veneer
    
7. Forced air

    -*All else being equal*, we can reasonably expect that adding forced air heating to a house that previously did not have forced air will increase sale price by about \$12637
    
8. Vinyl siding vs hardboard

    -*All else being equal*, we can reasonably expect that a house with vinyl siding will sell for about $10926 more than a house with hardboard siding
 

# Conclusion

### Ultimately, I'm not sure how useful this model would be in satisfying my problem statement, as my RMSE was ~32,000. This margin of error is more than double my most valuable feature, so take these top three recommendations with 32,000 grains of salt:

   1. Siding -- Vinyl siding added the most value to a house of any other siding (compared to hardboard). Wood siding subtracted the most value. Recommendation: Look for houses with outdated/otherwise gross siding and slap some vinyl on that bad boy.
    
    
   2. Furnace -- Having a standard forced-air furnace added a whopping 12,000 USD (*cp*) to sale price. On average, installing a furnace costs (apparently) about 2,000 USD. Recommendation: Buy houses with old/outdated/underperforming/inefficient furnaces, and replace them with nice ones.
   
   
   3. Kitchen -- Kitchen remodelling is anecdotally one of the best ways to add equity to your home. However, there is a lot of disagreement on what the average kitchen remodel costs. This statistical murkiness, coupled with the arcane rating system used by the assessor's office, make it hard to say for sure if kitchens are a good target for flipping houses. Recommendation: Take kitchens on a case-by-case basis. If a kitchen is crappy enough, and you can upgrade it economically enough, you can add significant equity to a house.
