# Churn Predictor Sample Project

> This is a Dato sample for churn prediction. Explore the [gallery](https://dato.com/learn/gallery/) to see other examples.  

This sample code shows how to build, evaluate, and deploy a
model to predict customer churn. You could use this model to find
customers who are likely to stop using your product or service.


## Get started

1. Before you begin, make sure you have [installed GraphLab Create](https://dato.com/download/),
   a Python package for machine learning.

2. [Download and extract the example code](https://github.com/dato-code/sample-churn-predictor/archive/master.zip)
   to a directory on your machine, or clone it with the following command:

   ```bash
   git clone http://github.com/dato-code/sample-churn-predictor
   cd sample-churn-predictor
   ```

3. While in the `sample-churn-predictor` directory, run the following script
   to download the sample project data:

  ```bash
  python download_data.py
  ```

4. Make sure you are working in a Python environment with GraphLab Create installed
   (e.g. if you installed GraphLab Create using the Dato Launcher, you can use the Launcher to open a GraphLab Create Terminal).
   Then, run the `churn_predictor.py` script to build and explore the model on your machine:

   ```bash
   python -i churn_predictor.py
   ```

   The `-i` flag causes Python to drop into an interactive interpreter
   after the script executes.

   Alternatively, you can also run the provided IPython Notebook:

   ```bash
   ipython notebook churn_predictor.ipynb
   ```

   Once the model has been created, a browser window should open
   to let you explore and interact with your model.

## Learn More and Next Steps

Once you have the sample project running, you can try the following:

  - [Learn more about how the sample works](./LEARN_MORE.md#how-it-works)
  - [Try it on your own data set](./LEARN_MORE.md#use-your-own-data)

To find out more about building churn prediction models, check out the
[user guide](https://dato.com/learn/userguide/churn_prediction/quick-start.html)
or [API documentation](https://dato.com/products/create/docs/graphlab.toolkits.churn_predictor.html).


## Troubleshooting

If you are having trouble, please [create a Github Issue](https://github.com/dato-code/sample-churn-predictor/issues/new)
or start a discussion on the [user forum](http://forum.dato.com/).


## Acknowledgments

The online retail data set used in this sample was obtained from the [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Online+Retail).
