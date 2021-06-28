# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:22:34 2021

@author: Ashok Kumar JHa
"""
import pandas as pd


# Read Data

def addMav(data):
    # Create MAV Data
    data['MA10'] = data['Close'].rolling(10).mean()


def addmacddata(data):
    # Create MACD and Signal Data
    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()
    MACD = exp1-exp2
    data['MACD'] = MACD
    data['Signal Line'] = data['MACD'].ewm(span=9, adjust=False).mean()


def addsochasticData(data):
    # Sochastic oscillator Data
    high14 = data['High'].rolling(14).max()
    low14 = data['Low'].rolling(14).min()
    data['%K'] = (data['Close']-low14)*100/(high14-low14)
    data['%D'] = data['%K'].rolling(3).mean()


def getwriter():
    return pd.ExcelWriter(
        "Technical.xlsx",
        engine="xlsxwriter",
        date_format='YYYY-MM-DD',
        datetime_format='YYYY-MM-DD')


def getformat(workbook):
    green_cell = workbook.add_format({
            'bg_color': '#C6EFCE', 'font_color': '#006100'})
    red_cell = workbook.add_format({
            'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
    return green_cell, red_cell


def createma10Chart(writer,data, green_Cell, red_Cell):
    sheetname = "MA10"
    data[['Close', 'MA10']].to_excel(writer, sheet_name=sheetname)
    worksheet = writer.sheets[sheetname]
    worksheet.set_column(0, 0, 15)

    # Adding Formating
    for col in range(1, 3):
        # Create Conditional formated Type formula for green cell
        worksheet.conditional_format(1, col, len(data), col, {
                "type": "formula",
                "criteria": "=B2>=C2",
                "format": green_Cell
                })
        # Create Conditional formated Type formula for red cell
        worksheet.conditional_format(1, col, len(data), col, {
                "type": "formula",
                "criteria": "=B2<C2",
                "format": red_Cell
                })

    # Create a new chart
    chart1 = writer.book.add_chart({'type': 'line'})

    # add series to chart
    chart1.add_series({
            "name": "AAPL",
            "categories": [sheetname, 1, 0, len(data), 0],
            "values": [sheetname, 1, 1, len(data), 1],
            })

    # Create a new chart
    chart2 = writer.book.add_chart({'type': 'line'})
    # Create series to chart
    chart2.add_series({
            "name": sheetname,
            "categories": [sheetname, 1, 0, len(data), 0],
            "values": [sheetname, 1, 2, len(data), 2],
            })

    # Combine Chart
    chart1.combine(chart2)

    chart1.set_title({"name": sheetname+" AAPL"})
    chart1.set_x_axis({"name": "Date"})
    chart1.set_y_axis({"name": "Price"})

    # Insert Chart,
    worksheet.insert_chart('E2', chart1)


def createmacdChart(writer, data, green_Cell, red_Cell):
    sheetname = "MACD"
    data[['Close', 'MACD', 'Signal Line']].to_excel(
            writer, sheet_name=sheetname)
    worksheet = writer.sheets[sheetname]
    worksheet.set_column(0, 0, 15)

    # Adding Formating
    for col in range(1, 4):
        # Create Conditional formated Type formula for green cell
        worksheet.conditional_format(1, col, len(data), col, {
                "type": "formula",
                "criteria": "=C2>=D2",
                "format": green_Cell
                })
        # Create Conditional formated Type formula for red cell
        worksheet.conditional_format(1, col, len(data), col, {
                "type": "formula",
                "criteria": "=C2<D2",
                "format": red_Cell
                })

    # Create a new chart
    chart1 = writer.book.add_chart({'type': 'line'})

    # add series to chart
    chart1.add_series({
            "name": "MACD",
            "categories": [sheetname, 1, 0, len(data), 0],
            "values": [sheetname, 1, 2, len(data), 2],
            })

    # Create a new chart
    chart2 = writer.book.add_chart({'type': 'line'})
    # Create series to chart
    chart2.add_series({
            "name": "signal line",
            "categories": [sheetname, 1, 0, len(data), 0],
            "values": [sheetname, 1, 3, len(data), 3],
            })

    # Combine Chart
    chart1.combine(chart2)

    chart1.set_title({"name": sheetname+" AAPL"})
    chart1.set_x_axis({
            "name": "Date",
            'label_position': 'low',
            'num_font': {'rotation': 45}})
    chart1.set_y_axis({"name": "Value"})

    # Insert Chart,
    worksheet.insert_chart('F2', chart1)


def createsochasticChart(writer, data, green_Cell, red_Cell):
    sheetname = "Stocastic"
    data[['Close', '%K', '%D']].to_excel(writer, sheet_name=sheetname)
    worksheet = writer.sheets[sheetname]
    worksheet.set_column(0, 0, 15)

    # Adding Formating
    for col in range(1, 4):
        # Create Conditional formated Type formula for green cell
        worksheet.conditional_format(1, col, len(data), col, {
                "type": "formula",
                "criteria": "=C2>=D2",
                "format": green_Cell
                })
        # Create Conditional formated Type formula for red cell
        worksheet.conditional_format(1, col, len(data), col, {
                "type": "formula",
                "criteria": "=C2<D2",
                "format": red_Cell
                })

    # Create a new chart
    chart1 = writer.book.add_chart({'type': 'line'})

    # add series to chart
    chart1.add_series({
            "name": "%K",
            "categories": [sheetname, 1, 0, len(data), 0],
            "values": [sheetname, 1, 2, len(data), 2],
            })

    # Create a new chart
    chart2 = writer.book.add_chart({'type': 'line'})
    # Create series to chart
    chart2.add_series({
            "name": "%D",
            "categories": [sheetname, 1, 0, len(data), 0],
            "values": [sheetname, 1, 3, len(data), 3],
            })

    # Combine Chart
    chart1.combine(chart2)

    chart1.set_title({"name": sheetname+" AAPL"})
    chart1.set_x_axis({
            "name": "Date",
            'label_position': 'low',
            'num_font': {'rotation': 45}})
    chart1.set_y_axis({"name": "Value"})

    # Insert Chart,
    worksheet.insert_chart('F2', chart1)


data = pd.read_csv("data/AAPL.csv", index_col=0, parse_dates=True)


addMav(data)
addmacddata(data)
addsochasticData(data)

print(data.tail())

# Reduce Data Volume for Charting
data = (data.iloc[data.shape[0]//2:])[::-1]

# Excel Writer
writer = getwriter()

# Format for green cell
green_Cell, red_Cell = getformat(writer.book)
# **
#  MA10 : Moving Average Chart
# **
createma10Chart(writer, data, green_Cell, red_Cell)

# **
#  MACD
# **
createmacdChart(writer, data, green_Cell, red_Cell)

# **
#  SOCHASTIC : Moving Average Chart
# **
createsochasticChart(writer, data, green_Cell, red_Cell)
# Close
writer.close()
