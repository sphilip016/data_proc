import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import scipy.stats as stats


def get_rows(dtset):
    return(len(dtset.index))

def get_columns(dtset):
    return(len(dtset.columns))

def get_number_of_classes(dtset):
    return (len(dtset.iloc[:, len(dtset.columns)-1].unique()))

def get_perc_of_classes(dtset):
    classes= dtset.iloc[:, len(dtset.columns)-1].unique()
    percentage_per_class=dtset[dtset.columns[len(dtset.columns)-1]].value_counts(classes[1])
    return percentage_per_class


def get_number_of_nans(dtset):
    return(dtset.isnull().sum().sum())

def get_nans_per_row(dtset):
    return(dtset.isnull().sum(axis=1))

def get_nans_per_column(dtset):
    return(dtset.isnull().sum(axis=0))

def get_numerical_features(dtset):
    return(dtset.select_dtypes(include=np.number).columns.tolist())

def get_range_of_numerical_values(dtset):
    numerical_features=dtset.select_dtypes(include=np.number).columns.tolist()
    return (dtset[numerical_features].max()-dtset[numerical_features].min())

def check_for_datetime_feat(dtset):
    return(dtset.select_dtypes('datetime64').columns)

def get_all_feature_types(dtset):
    return(dtset.dtypes)

def box_plot(dtset,feature_to_plot):
    fig = px.box(dtset, y=feature_to_plot)
    fig.show()

def get_feature_variance(dtset):
    return (dtset.var())

def get_feature_statistics(dtset):
    #dtset['age'].describe()
    return(dtset.describe())

#This is the main entry point of this script
if __name__ == "__main__":

    dtset = pd.read_csv("bankadditionalfull.csv", delimiter=';') #read data frame

    #num_rows = get_rows(dtset) #get number of rows

    #num_columns = get_columns(dtset) # get number of columns

    #num_classes = get_number_of_classes(dtset) #get number of classes

    #all_nans = get_number_of_nans(dtset) #get number all nans in the data frame

    #percentage_per_class = get_perc_of_classes(dtset) #get percentage per class

    #nans_per_row = get_nans_per_row(dtset) #get nans per row

   #nans_per_column = get_nans_per_column(dtset)  # get nans per row

    #numerical_features=get_numerical_features(dtset) #get the numerical features of the data frame

    #range_of_values=get_range_of_numerical_values(dtset) #get the value range of numerical values

    #datetime_features=check_for_datetime_feat(dtset) #get features of type datetime64

    #features_types= get_all_feature_types(dtset) #get feature types

    #fetaures_variance= get_feature_variance(dtset)

    #feature_statistics = get_feature_statistics(dtset)

    #feature_to_plot="age"
    #box_plot(dtset,feature_to_plot)
    numerical_features = dtset.select_dtypes(include=np.number).columns.tolist()
    sk_dtset=dtset[numerical_features].skew()
    sk_dtset=sk_dtset.apply(np.log)
    sk_dtset.plot.hist(alpha=0.5, bins=10, grid=True, legend=None)
    param = stats.norm.fit(sk_dtset)  # Fit a normal distribution to the data
    x = np.linspace(0, 20, 100)  # Linear spacing of 100 elements between 0 and 20.
    pdf_fitted = stats.norm.pdf(x, *param)  # Use the fitted paramters to create the y datapoints
    plt.plot(x, pdf_fitted, color='r')
    plt.xlabel("Feature value")
    plt.title("Histogram")
    plt.show()
    #print(fetaures_variance)