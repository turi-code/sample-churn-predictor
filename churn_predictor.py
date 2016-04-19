import graphlab as gl
import datetime
from dateutil import parser as datetime_parser


### Load Data ###

# Table of product purchases
purchases = gl.SFrame.read_csv('dataset/online_retail.csv')


### Prepare Data ###

# Convert InvoiceDate strings (e.g. "12/1/10 8:26") to datetimes
purchases['InvoiceDate'] = purchases['InvoiceDate'].apply(datetime_parser.parse)

# Create a TimeSeries
timeseries = gl.TimeSeries(purchases, 'InvoiceDate')


### Train the churn predictor model ###

# Split the data into train and validation
train, valid = gl.churn_predictor.random_split(timeseries, user_id='CustomerID', fraction=0.8, seed = 1)

# A churn forecast requires a time boundary and a churn period.
# Activity before the boundary is used to train the model.
# After the boundary, activity (or lack of activity)
# during the churn period is used to define whether the
# user churned.

# Train the model using data before August
churn_boundary_oct = datetime.datetime(year = 2011, month = 8, day = 1)
# Define churn as "inactive for 30 days after August 1st 2011"
churn_period = datetime.timedelta(days = 30)

model = gl.churn_predictor.create(train, user_id='CustomerID',
                                  features = ['Quantity'],
                                  churn_period = churn_period,
                                  time_boundaries = [churn_boundary_oct])


### Explore the Model ###

# Interactively explore churn predictions
view = model.views.overview(exploration_set = timeseries,
                            validation_set = valid,
                            exploration_time = churn_boundary_oct, 
                            validation_time = churn_boundary_oct)
view.show()
