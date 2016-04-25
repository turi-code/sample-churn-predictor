# Churn Predictor: Learn More

This document provides more detail about the sample churn predictor.
You can learn more about building churn predictors with GraphLab Create in
the [user guide](https://dato.com/learn/userguide/churn_prediction/quick-start.html).

## How it works

The `churn_predictor.py` script performs the following actions:

```
Load Data -> Prepare Data -> Train Model -> Explore Model
```

### Load Data

This sample uses a table of product purchase data (541909 product purchases):

| InvoiceNo | StockCode |          Description           | Quantity | InvoiceDate  | UnitPrice | CustomerID |    Country     |
| --------- | --------- | ------------------------------ | -------- | ------------ | --------- | ---------- | -------------- |
|   536365  |   85123A  | WHITE HANGING HEART T-LIGH...  |    6     | 12/1/10 8:26 |    2.55   |   17850    | United Kingdom |
|   536365  |   71053   |      WHITE METAL LANTERN       |    6     | 12/1/10 8:26 |    3.39   |   17850    | United Kingdom |
|   536365  |   84406B  | CREAM CUPID HEARTS COAT HANGER |    8     | 12/1/10 8:26 |    2.75   |   17850    | United Kingdom |
|   536365  |   84029G  | KNITTED UNION FLAG HOT WAT...  |    6     | 12/1/10 8:26 |    3.39   |   17850    | United Kingdom |
|   536365  |   84029E  | RED WOOLLY HOTTIE WHITE HEART. |    6     | 12/1/10 8:26 |    3.39   |   17850    | United Kingdom |


### Prepare Data

Once the data is loaded, you typically want to clean it up or transform it in various ways.
The Churn Prediction toolkit uses GraphLab Create's TimeSeries data structure.
The sample code parses the `InvoiceDate` text column and converts
it to Python datetime objects. From this dataset, we create a TimeSeries.


### Train Churn Predictor Model

Next, we randomly split the data into a training set and validation set,
and define the churn period and boundary. These settings define time
after which a user will be considered "churned". To learn more,
check out the [user guide](https://dato.com/learn/userguide/churn_prediction/quick-start.html#how-is-churn-defined).

We use [`gl.churn_predictor.create`](https://dato.com/products/create/docs/generated/graphlab.churn_predictor.create.html)
to build the prediction model on the training set.


### Explore the Model

Once you've trained the model, you can use it to make churn forecasts.
The sample script launches an interactive web-based view for exploring
and evaluating the model:

![Screenshot of Exploration](/assets/churn-explore.png)

![Screenshot of Evaluation](/assets/churn-evaluate.png)

Find more information about how to use your model
in the [user guide](https://dato.com/learn/userguide/churn_prediction/using-a-trained-model.html).


## Use your own data

You can replace the sample data provided in this project with your own
dataset. At minimum, your data must contain a time column, a user id column, and a feature column.

You will need to replace the file name and column names in the
`churn_predictor.py` script to refer to your own data set.

For more information about setting up a churn predictor model,
check out the [user guide](https://dato.com/learn/userguide/churn_prediction/quick-start.html).
