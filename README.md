# Churn Predictor Sample Project

> This is a Turi sample for churn prediction. Explore the [gallery](https://turi.com/learn/gallery/) to see other examples.  

This sample code shows how to build, evaluate, and deploy a
model to predict customer churn. You could use this model to find
customers who are likely to stop using your product or service.


## Get started

1. Before you begin, make sure you have [installed GraphLab Create 1.9](https://turi.com/download/),
   a Python package for machine learning.

2. [Download and extract the example code](https://github.com/turi-code/sample-churn-predictor/archive/master.zip)
   to a directory on your machine, or clone it with the following command:

   ```bash
   git clone http://github.com/turi-code/sample-churn-predictor
   cd sample-churn-predictor
   ```

3. While in the `sample-churn-predictor` directory, run the following script
   to download the sample project data:

  ```bash
  python download_data.py
  ```

4. Making sure you are working in a Python environment with GraphLab Create installed,
   run the `churn_predictor.py` script to build and explore the model on your machine:

   ```bash
   python -i churn_predictor.py
   ```

   The `-i` flag causes Python to drop into an interactive interpreter
   after the script executes.

   Once the model has been created, a browser window should open
   to let you explore and interact with your model.

   Alternatively, you can also run the provided IPython Notebook:

   ```bash
   ipython notebook churn_predictor.ipynb
   ```


## Troubleshooting

If you are having trouble, please [create a Github Issue](https://github.com/turi-code/sample-churn-predictor/issues/new)
or start a discussion on the [user forum](http://forum.turi.com/).
