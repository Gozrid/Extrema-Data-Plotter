- [Prerequisites](#prerequisites)<br>
- [Usage](#usage)<br>
- [Open and plot .mot file](#open-and-plot-mot-file)<br>
  - [Open a .mot file](#open-a-mot-file)<br>
  - [Create plot](#create-plot)<br>
  - [Changing analysis data](#changing-analysis-data)<br>

# Prerequisites

- [Python installed](https://www.python.org/downloads/)

# Usage

1. create a new virtual environment: `python -m venv ./venv` or `python3 -m venv ./venv`
2. install all requirements: `./venv/bin/pip install -r requirements.txt`
3. run the app: `./venv/bin/python main.py`

# Open and plot .mot file

## Open a .mot file

- In the menu press "File" -> "Open"
- Select the .mot file to open

## Create plot

1. Select the data column to be plotted against time<br>
   <small>Click on the dropdown menu (left to "Set")</small><br>
   *<u>After selecting press "Set"</u>*<br>
   ![Data column](./.github/README/data_column.png)

2. **(Optional)**<br>
   Change naming of the plot<br>
   *<u>After naming press "Set"</u>*<br>
   ![Plot naming](./.github/README/plot_naming.png)

3. Press "Plot!"<br>
   <small>At the bottom of the application</small><br>
   ![Plot](./.github/README/plot_button.png)

## Changing analysis data

1. Select the data column to be plotted against time<br>
   <small>Click on the dropdown menu (left to "Set")</small><br>
   *<u>After selecting press "Set"</u>*<br>
   ![Data column](./.github/README/data_column.png)

2. Press "Plot!"<br>
   <small>At the bottom of the application</small><br>
   ![Plot](./.github/README/plot_button.png)

3. Change the analysis data<br>
   ![Analysis data](./.github/README/analysis_data.png)

| variable                    | description                                                                                              | Example picture                                                             |
|-----------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| maxima_height               | The minimum height a maxima must have                                                                    | ![Maxima height](./.github/README/analysis_data/maxima_height.png)          |
| minima_height               | The maximum height a minima may have                                                                     | ![Minima height](./.github/README/analysis_data/minima_height.png)          |
| prominence                  | The minimum distance between minima maxima                                                               | ![Prominence](./.github/README/analysis_data/prominence.png)                |
| distance_between_extremas_x | The minimum distance between selected extremas                                                           | ![Distance](./.github/README/analysis_data/distance_between_extremas_x.png) |
| start_time                  | The start of the extrema analysis                                                                        | ![Start time](./.github/README/analysis_data/start_time.png)                |
| end_time                    | The end of the extrema analysis                                                                          | ![End time](./.github/README/analysis_data/end_time.png)                    |
| precision                   | The accuracy of the speed calculation from the extremes in the number of digits after the decimal point. |                                                                             |