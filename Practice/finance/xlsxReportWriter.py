# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:22:34 2021

@author: Ashok Kumar JHa
"""
import pandas as pd
import ReadYFinance as ryf
from configparser import RawConfigParser


class xlsxReportWriter:
    DATA_FILE = "data/AAPL.csv"
    DATA_OUTFILE = "data/AAPLTechnicalAnalisis.xlsx"
    ticker = 'AAPL'
    
    '''
        Financial Technical Analysis
    '''
    def __init__(self, cfg=None):
        '''
            Initialize with configuration
        '''
        self.config = cfg
        # Approx Number of Trading Day In Year
        self.NUMOFTD = 252
        print(self.config)

        if cfg is None:
            '''
                Example used csv file
            '''
            self.data = pd.read_csv(self.DATA_FILE, index_col=0,
                                    parse_dates=True)
        else:
            '''
            Load the data as per configuration
            '''
            self.data = ryf.getYFData(self.config)
            self.ticker = self.config['ticker']

        self.DATA_OUTFILE = self.DATA_OUTFILE.replace("AAPL", self.ticker)
        '''
            XLSX Writer and Fornat creation
        '''
        self.writer = pd.ExcelWriter(
            self.DATA_OUTFILE,
            engine="xlsxwriter",
            date_format='YYYY-MM-DD',
            datetime_format='YYYY-MM-DD')
        # Create Format
        self.green_cell = self.writer.book.add_format({
                'bg_color': '#C6EFCE', 'font_color': '#006100'})
        self.red_cell = self.writer.book.add_format({
                'bg_color': '#FFC7CE', 'font_color': '#9C0006'})

    def resizeData(self):
        # Reduce Data Volume for Charting
        self.data = (self.data.iloc[len(self.data)//2:])[::-1]

    def createData(self):

        def addMav():
            # Create MAV Data
            self.data['MA10'] = self.data['Close'].rolling(10).mean()

        def addmacddata():
            # Create MACD and Signal Data
            exp1 = self.data['Close'].ewm(span=12, adjust=False).mean()
            exp2 = self.data['Close'].ewm(span=26, adjust=False).mean()
            MACD = exp1-exp2
            self.data['MACD'] = MACD
            self.data['Signal Line'] = self.data['MACD'].ewm(
                    span=9, adjust=False).mean()

        def addsochasticData():
            # Sochastic oscillator Data
            high14 = self.data['High'].rolling(14).max()
            low14 = self.data['Low'].rolling(14).min()
            self.data['%K'] = (self.data['Close']-low14)*100/(high14-low14)
            self.data['%D'] = self.data['%K'].rolling(3).mean()

        addMav()
        addmacddata()
        addsochasticData()

    def createma10Chart(self):
        '''
             MA10 : Moving Average Chart
        '''
        sheetname = "MA10"
        self.data[['Close', 'MA10']].to_excel(
                self.writer, sheet_name=sheetname)
        worksheet = self.writer.sheets[sheetname]
        worksheet.set_column(0, 0, 15)

        # Adding Formating
        for col in range(1, 3):
            # Create Conditional formated Type formula for green cell
            worksheet.conditional_format(1, col, len(self.data), col, {
                    "type": "formula",
                    "criteria": "=B2>=C2",
                    "format": self.green_cell
                    })
            # Create Conditional formated Type formula for red cell
            worksheet.conditional_format(1, col, len(self.data), col, {
                    "type": "formula",
                    "criteria": "=B2<C2",
                    "format": self.red_cell
                    })

        # Create a new chart
        chart1 = self.writer.book.add_chart({'type': 'line'})

        # add series to chart
        chart1.add_series({
                "name": self.ticker,
                "categories": [sheetname, 1, 0, len(self.data), 0],
                "values": [sheetname, 1, 1, len(self.data), 1],
                })

        # Create a new chart
        chart2 = self.writer.book.add_chart({'type': 'line'})
        # Create series to chart
        chart2.add_series({
                "name": sheetname,
                "categories": [sheetname, 1, 0, len(self.data), 0],
                "values": [sheetname, 1, 2, len(self.data), 2],
                })

        # Combine Chart
        chart1.combine(chart2)

        chart1.set_title({"name": sheetname+" "+self.ticker})
        chart1.set_x_axis({"name": "Date"})
        chart1.set_y_axis({"name": "Price"})

        # Insert Chart,
        worksheet.insert_chart('E2', chart1)

    def createmacdChart(self):
        '''
            MACD Chart
        '''
        sheetname = "MACD"
        self.data[['Close', 'MACD', 'Signal Line']].to_excel(
                self.writer, sheet_name=sheetname)
        worksheet = self.writer.sheets[sheetname]
        worksheet.set_column(0, 0, 15)

        # Adding Formating
        for col in range(1, 4):
            # Create Conditional formated Type formula for green cell
            worksheet.conditional_format(1, col, len(self.data), col, {
                    "type": "formula",
                    "criteria": "=C2>=D2",
                    "format": self.green_cell
                    })
            # Create Conditional formated Type formula for red cell
            worksheet.conditional_format(1, col, len(self.data), col, {
                    "type": "formula",
                    "criteria": "=C2<D2",
                    "format": self.red_cell
                    })

        # Create a new chart
        chart1 = self.writer.book.add_chart({'type': 'line'})

        # add series to chart
        chart1.add_series({
                "name": "MACD",
                "categories": [sheetname, 1, 0, len(self.data), 0],
                "values": [sheetname, 1, 2, len(self.data), 2],
                })

        # Create a new chart
        chart2 = self.writer.book.add_chart({'type': 'line'})
        # Create series to chart
        chart2.add_series({
                "name": "signal line",
                "categories": [sheetname, 1, 0, len(self.data), 0],
                "values": [sheetname, 1, 3, len(self.data), 3],
                })

        # Combine Chart
        chart1.combine(chart2)

        chart1.set_title({"name": sheetname+" "+self.ticker})
        chart1.set_x_axis({
                "name": "Date",
                'label_position': 'low',
                'num_font': {'rotation': 45}})
        chart1.set_y_axis({"name": "Value"})

        # Insert Chart,
        worksheet.insert_chart('F2', chart1)

    def createsochasticChart(self):
        '''
            SOCHASTIC : Moving Average Chart
        '''
        sheetname = "Stocastic"
        self.data[['Close', '%K', '%D']].to_excel(
                self.writer, sheet_name=sheetname)
        worksheet = self.writer.sheets[sheetname]
        worksheet.set_column(0, 0, 15)

        # Adding Formating
        for col in range(1, 4):
            # Create Conditional formated Type formula for green cell
            worksheet.conditional_format(1, col, len(self.data), col, {
                    "type": "formula",
                    "criteria": "=C2>=D2",
                    "format": self.green_cell
                    })
            # Create Conditional formated Type formula for red cell
            worksheet.conditional_format(1, col, len(self.data), col, {
                    "type": "formula",
                    "criteria": "=C2<D2",
                    "format": self.red_cell
                    })

        # Create a new chart
        chart1 = self.writer.book.add_chart({'type': 'line'})

        # add series to chart
        chart1.add_series({
                "name": "%K",
                "categories": [sheetname, 1, 0, len(self.data), 0],
                "values": [sheetname, 1, 2, len(self.data), 2],
                })

        # Create a new chart
        chart2 = self.writer.book.add_chart({'type': 'line'})
        # Create series to chart
        chart2.add_series({
                "name": "%D",
                "categories": [sheetname, 1, 0, len(self.data), 0],
                "values": [sheetname, 1, 3, len(self.data), 3],
                })

        # Combine Chart
        chart1.combine(chart2)

        chart1.set_title({"name": sheetname+" "+self.ticker})
        chart1.set_x_axis({
                "name": "Date",
                'label_position': 'low',
                'num_font': {'rotation': 45}})
        chart1.set_y_axis({"name": "Value"})

        # Insert Chart,
        worksheet.insert_chart('F2', chart1)

    def clean(self):
        self.writer.close()


if __name__ == "__main__":
    config = RawConfigParser()
    config.read('fin.properties')
    xrw = xlsxReportWriter(cfg=dict(config.items('FIN')))
    xrw.createData()
    print(xrw.data.tail())
    xrw.resizeData()
    print(xrw.data.tail())
    xrw.createma10Chart()
    xrw.createmacdChart()
    xrw.createsochasticChart()
    xrw.clean()
