from tkinter import simpledialog

import pandas as pd
import numpy as np
import plotly.express as px

import tkinter as tk
import DataPreprocessingMain
from tkinter import*



def btn_rows_handle(dtset,txtbox_results):
    txtbox_results.delete('1.0',END)
    #txtbox_results.update()
    output = DataPreprocessingMain.get_rows(dtset)
    txtbox_results.insert(tk.END, "Number of rows: "+str(output))
def btn_columns_handle(dtset, txtbox_results):
        txtbox_results.delete('1.0', END)
        # txtbox_results.update()
        output = DataPreprocessingMain.get_columns(dtset)
        txtbox_results.insert(tk.END, "Number of rows: " + str(output))
def btn_classes_handle(dtset, txtbox_results):
    txtbox_results.delete('1.0', END)
    # txtbox_results.update()
    output = DataPreprocessingMain.get_number_of_classes(dtset)
    txtbox_results.insert(tk.END, "Number of classes: " + str(output))
def btn_clear_handle(txtbox_results):
    txtbox_results.delete('1.0', END)
def btn_nans_handle(dtset, txtbox_results):
    txtbox_results.delete('1.0', END)
    # txtbox_results.update()
    output = DataPreprocessingMain.get_number_of_nans(dtset)
    txtbox_results.insert(tk.END, "Number of classes: " + str(output))


def btn_classes_perce_handle(dtset, txtbox_results):
    txtbox_results.delete('1.0', END)
    # txtbox_results.update()
    output = DataPreprocessingMain.get_perc_of_classes(dtset)
    txtbox_results.insert(tk.END, str(output))


def btn_nans_row_handle(dtset, txtbox_results):
    txtbox_results.delete('1.0', END)
    # txtbox_results.update()
    output = DataPreprocessingMain.get_nans_per_row(dtset)
    txtbox_results.insert(tk.END, "Number of nans per row: " + str(output))


def btn_nans_columns_handle(dtset, txtbox_results):
    txtbox_results.delete('1.0', END)
    # txtbox_results.update()
    output = DataPreprocessingMain.get_nans_per_column(dtset)
    txtbox_results.insert(tk.END, "Number of nans per column: " + str(output))


def btn_numericalF_handle(dtset, txtbox_results):
    txtbox_results.delete('1.0', END)
    # txtbox_results.update()
    output = DataPreprocessingMain.get_numerical_features(dtset)
    txtbox_results.insert(tk.END, str(output))


def btn_Frange_handle(dtset, txtbox_results):
    txtbox_results.delete('1.0', END)
    # txtbox_results.update()
    output = DataPreprocessingMain.get_range_of_numerical_values(dtset)
    txtbox_results.insert(tk.END, str(output))


def btn_datetimeF_handle(dtset, txtbox_results):
    txtbox_results.delete('1.0', END)
    # txtbox_results.update()
    output = DataPreprocessingMain.check_for_datetime_feat(dtset)
    txtbox_results.insert(tk.END, "Number of datetime features: " + str(output))

#Discription:Get type of each features
#Input: Dataframe, Result 's textbox
#Output: Features types
def btn_Ftypes_handle(dtset, txtbox_results):
    txtbox_results.delete('1.0', END)#clear result's textbox
    output = DataPreprocessingMain.get_all_feature_types(dtset)#get geatures types
    txtbox_results.insert(tk.END, str(output))#show results on result's textbox

#Discription:Get variance of features
#Input: Dataframe, Result 's textbox
#Output: Features variance
def btn_var_handle(dtset, txtbox_results):
    txtbox_results.delete('1.0', END)#clear result's textbox
    output = DataPreprocessingMain.get_feature_variance(dtset)#get features variance
    txtbox_results.insert(tk.END, str(output))#show results on result's textbox

#Discription:Get general statistic valus for numerical features
#Input: Dataframe, Result 's textbox
#Output: Numerical features statistics
def btn_statistics_handle(dtset, txtbox_results):
    txtbox_results.delete('1.0', END)#clear result's textbox
    output = DataPreprocessingMain.get_feature_statistics(dtset) #get general statistics on numerical features
    txtbox_results.insert(tk.END,str(output))#show results on result's textbox

#Discription: Plot box-plot for the selected feature
#Input: Dataframe, Result 's textbox
#Output: Plot box-plot
def btn_boxplot_handle(dtset, txtbox_results):
    txtbox_results.delete('1.0', END) #clear result's textbox
    feature_name = simpledialog.askstring("Input", "Feature name?") #get from the user the feature to plot
    #check if is not none
    if feature_name is not None:
        DataPreprocessingMain.box_plot(dtset,feature_name)#plot

#Discription: Update screen with the dataframe
#Input: Textboxes for displayin dataframe, dataframe
#Output: Screen is Updated wiith the new dataframe 
def update_screen(txtbox_display1,txtbox_display2,txtbox_display3,txtbox_display4,dtset):
    #clear textboxes
    txtbox_display1.delete('1.0', END)
    txtbox_display2.delete('1.0', END)
    txtbox_display3.delete('1.0', END)
    txtbox_display4.delete('1.0', END)
    #update textboxes with new text
    txtbox_display1.insert(tk.END, str(dtset[dtset.columns[0:6]]))
    txtbox_display2.insert(tk.END, str(dtset[dtset.columns[7:14]]))
    txtbox_display3.insert(tk.END, str(dtset[dtset.columns[15:20]]))
    txtbox_display4.insert(tk.END, str(dtset[dtset.columns[20:21]]))

#Discription: Change a specific value in the dataframe and update the screen. Get users inputs; row,column,new value; and chanhge the value in the df
#Input: Textboxes for displayin dataframe, dataframe
#Output: Screen is Updated wiith the new dataframe 
def change_value(dtset,txtbox_display1,txtbox_display2,txtbox_display3,txtbox_display4):
    #get input from user: row, column, new value
    row = simpledialog.askstring("Input", "Row?")
    while int(row)<0 and int(row)>len(dtset.index):
        row = simpledialog.askstring("Input", "No row named: "+str(row)+". Correct Row?")
    column = simpledialog.askstring("Input", "Column?")
    while not str(column) in dtset.columns:
        column = simpledialog.askstring("Input", "No column named: "+str(column)+". Correct Column?")
    value = simpledialog.askstring("Input", "New Value?")
    #check if input value for rows and column is empty to avoid error
    if row is not None and column is not None:
        dtset.at[int(row), str(column)] = value #update df
        update_screen(txtbox_display1,txtbox_display2,txtbox_display3,txtbox_display4,dtset)#update screen


if __name__ == '__main__':

    r = tk.Tk()
    r.state('zoomed')#set full screen for gui window
    r.title('Data Preprocesing')#set window title
    pd.set_option('display.max_rows', None)#specified no restriction for displaying rows of the datadet
    pd.set_option('display.max_columns', None)#specified no restriction for displaying rows of the datadet
    dtset = pd.read_csv("bankadditionalfull.csv", delimiter=';')  # read data frame with seting the dilimeter to seperate the columns



    #define the textbox in the gui for displaying the dataframe
    txtbox_display1 = Text()
    txtbox_display2 = Text()
    txtbox_display3 = Text()
    txtbox_display4=Text(width=12)
    update_screen(txtbox_display1,txtbox_display2,txtbox_display3,txtbox_display4,dtset) #update the screen to display the datafame
    #set the postions of the textbox
    txtbox_display1.grid(column = 0, row = 0)
    txtbox_display2.grid(column = 1, row = 0)
    txtbox_display3.grid(column=2, row=0)
    txtbox_display4.grid(column=0, row=1, sticky="w")
    
    # define the textbox in the gui for displaying the results
    txtbox_results = tk.Text(background="light grey")
    txtbox_results.insert(tk.END, str(""))

    # define the buttons for the gui 
    btn_rows = tk.Button(r, text='Number of Rows', width=15, command=lambda: btn_rows_handle(dtset,txtbox_results))
    btn_columns = tk.Button(r, text='Number of Columns', width=15, command=lambda: btn_columns_handle(dtset, txtbox_results))
    btn_classes = tk.Button(r, text='Number of Classes', width=15, command=lambda: btn_classes_handle(dtset, txtbox_results))
    btn_nans = tk.Button(r, text='Number of NaN ', width=15, command=lambda: btn_nans_handle(dtset, txtbox_results))
    btn_classes_perce = tk.Button(r, text='Classes Percentage', width=15, command=lambda: btn_classes_perce_handle(dtset, txtbox_results))
    btn_nans_row = tk.Button(r, text='NaN per Row', width=15, command=lambda: btn_nans_row_handle(dtset, txtbox_results))
    btn_nans_columns = tk.Button(r, text='NaN per Column', width=15, command=lambda: btn_nans_columns_handle(dtset, txtbox_results))
    btn_numericalF = tk.Button(r, text='Numerical Features', width=15, command=lambda: btn_numericalF_handle(dtset, txtbox_results))
    btn_Frange = tk.Button(r, text='Feature Value Range', width=17, command=lambda: btn_Frange_handle(dtset, txtbox_results))
    btn_datetimeF = tk.Button(r, text='Features of Type DateTime', width=20, command=lambda: btn_datetimeF_handle(dtset, txtbox_results))
    btn_Ftypes = tk.Button(r, text='Feature Types', width=15, command=lambda:btn_Ftypes_handle(dtset, txtbox_results))
    btn_var = tk.Button(r, text='Feature Variance', width=15, command=lambda: btn_var_handle(dtset, txtbox_results))
    btn_statistics = tk.Button(r, text='Feature Statistics', width=15, command=lambda: btn_statistics_handle(dtset, txtbox_results))
    btn_boxplot = tk.Button(r, text='Plot BoxPlot', width=15, command=lambda: btn_boxplot_handle(dtset, txtbox_results))
    btn_replace=tk.Button(r, text="Replave Value", width=15, command=lambda :change_value(dtset,txtbox_display1,txtbox_display2,txtbox_display3,txtbox_display4))
    btn_clear = tk.Button(r, text='Clear', width=5,command=lambda: btn_clear_handle(txtbox_results))

    # set the postions of the result's textbox and buttons
    txtbox_results.grid(column = 1, row = 1)
    btn_rows.place(bordermode=OUTSIDE,relx=0, rely=0.8, anchor="sw")
    btn_columns.place(bordermode=OUTSIDE,relx=0.1, rely=0.8, anchor="sw")
    btn_classes.place(bordermode=OUTSIDE,relx=0.2, rely=0.8, anchor="sw")
    btn_nans.place(bordermode=OUTSIDE,relx=0.3, rely=0.8, anchor="sw")
    btn_classes_perce.place(bordermode=OUTSIDE,relx=0.4, rely=0.8, anchor="sw")
    btn_nans_row.place(bordermode=OUTSIDE,relx=0.5, rely=0.8, anchor="sw")
    btn_nans_columns.place(bordermode=OUTSIDE,relx=0.6, rely=0.8, anchor="sw")
    btn_numericalF.place(bordermode=OUTSIDE,relx=0.7, rely=0.8, anchor="sw")
    btn_Frange.place(bordermode=OUTSIDE,relx=0, rely=0.85, anchor="sw")
    btn_datetimeF.place(bordermode=OUTSIDE,relx=0.1, rely=0.85, anchor="sw")
    btn_Ftypes.place(bordermode=OUTSIDE,relx=0.2, rely=0.85, anchor="sw")
    btn_var.place(bordermode=OUTSIDE,relx=0.3, rely=0.85, anchor="sw")
    btn_statistics.place(bordermode=OUTSIDE,relx=0.4, rely=0.85, anchor="sw")
    btn_boxplot.place(bordermode=OUTSIDE,relx=0.5, rely=0.85, anchor="sw")
    btn_replace.place(bordermode=OUTSIDE,relx=0.6, rely=0.85, anchor="sw")
    btn_clear.place(bordermode=OUTSIDE,relx=0.7, rely=0.85, anchor="sw")
    
    #main loop for the gui
    r.mainloop()
