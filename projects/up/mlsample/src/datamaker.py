# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:12:40 2021

@author: USER
"""
import os
import pandas as pd
import numpy as np
import csv
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

FILE_NAME = 'data'+os.sep+'cars.csv'


class datamaker(object):
    """
    Datamaker  helperClass.

        Initialise

    """

    def __init__(self):
        super()

    def getdataviap(self, fn):
        """
        Read Data from file usind Dataframee.

        Parameters
        ----------
        fn : TYPE
            File Name.

        Returns
        -------
        TYPE
        Dataframe.

        """
        return pd.read_csv(fn)

    def getdataviacsv(self, fn):
        """
        Read Data from file usind CSV.

        Parameters
        ----------
        fn : TYPE
            File Name.

        Returns
        -------
        TYPE
        data Dictionary list

        """
        with open(fn, 'r') as f:
            return list(csv.DictReader(f))

    def usepandaforreg(self, fn):
        """
        Read Calculate and display car's Hoursepower vs Torque.

        Get data using pandas from csv
        CValculate Regression between HP and Torque
        Display Torque Car Hoiurce power relation.

        Parameters
        ----------
        fn : String
           Data File.

        Returns
        -------
        None.

        """
        data = self.getdataviap(fn)
        trq = data[data.columns[-1]]
        hp = data[data.columns[-2]]
        TRQ = np.array(trq).reshape(-1, 1)
        HP = np.array(hp).reshape((-1, 1))
        lnrRegressor = LinearRegression()
        lnrRegressor.fit(HP, TRQ)
        TRQ_PRED = lnrRegressor.predict(HP)
        fig, ax = plt.subplots()
        alpha = str(round(lnrRegressor.intercept_[0], 5))
        beta = str(round(lnrRegressor.coef_[0][0], 5))
        ax.set_title(f"Alpha - {alpha}, Beta - {beta}")
        ax.scatter(HP, TRQ)
        ax.plot(HP, TRQ_PRED, c='y')

    def usecsvforreg(self, fn):
        """
        Get data from CSV and Display Torque Car Hoiurce power relation.

        Parameters
        ----------
        fn : String
           Data File.

        Returns
        -------
        None.

        """
        data = self.getdataviacsv(fn)
        hp = [int(i['Horsepower']) for i in data]
        trq = [int(i['Torque']) for i in data]
        TRQ = np.array(trq).reshape(-1, 1)
        HP = np.array(hp).reshape((-1, 1))
        lnrRegressor = LinearRegression()
        lnrRegressor.fit(HP, TRQ)
        TRQ_PRED = lnrRegressor.predict(HP)
        fig, ax = plt.subplots()
        alpha = str(round(lnrRegressor.intercept_[0], 5))
        beta = str(round(lnrRegressor.coef_[0][0], 5))
        ax.set_title(f"Alpha - {alpha}, Beta - {beta}")
        ax.scatter(HP, TRQ)
        ax.plot(HP, TRQ_PRED, c='y')


if __name__ == '__main__':

    dm = datamaker()
    dm.usepandaforreg(FILE_NAME)
    dm.usecsvforreg(FILE_NAME)
