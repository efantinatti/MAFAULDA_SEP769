# MAFAULDA_SEP769

This is a work based on the [MAFAULDA](http://www02.smt.ufrj.br/~offshore/mfs/page_01.html) project.

The main dataset files shall be found on [Kaggle - Machinery Fault Dataset](https://www.kaggle.com/uysalserkan/fault-induction-motor-dataset) 

## Description:

Based on the [MAFAULDA](http://www02.smt.ufrj.br/~offshore/mfs/page_01.html) project datased available also on [ Kaggle - Machinery Fault Dataset](https://www.kaggle.com/uysalserkan/fault-induction-motor-dataset), this project's main idea is to create a Deep Neural Network which will classify when the machine is running on its normal status or imbalanced status.

This database comprises on samples taken from a rate of 50 kHz scanning A/D device using the SpectraQuest Inc. Alignment/Balance Vibration Trainer (ABVT) Machinery Fault Simulator (MFS) as shown below:

![Machinery Fault Simulator](https://spectraquest.com/spectraquest/images/products/main/MFS.jpg)
Source: [Machine Fault Simulator](https://spectraquest.com/machinery-fault-simulator/details/mfs/)

For more details, reach the MAFAULDA project as mentioned on the link above.

## Dataset format:

This database is composed of 1951 multivariate time-series acquired by sensors on a SpectraQuest's Machinery Fault Simulator (MFS) Alignment-Balance-Vibration (ABVT). The 1951 comprises six different simulated states: normal function, imbalance fault, horizontal and vertical misalignment faults and, inner and outer bearing faults. This section describes the database.

The database is composed by several CSV (Comma-Separated Values) files, each one with 8 columns, one column for each sensor, according to:

* column 1 - tachometer signal that allows to estimate rotation frequency;

* columns 2 to 4 - underhang bearing accelerometer (axial, radiale tangential direction);

* columns 5 to 7 - overhang bearing accelerometer (axial, radiale tangential direction);

* column 8 - microphone.

And making a simple exploratory analysis, that is what the data extract from the columns 2 to 7 looks like:

![Dataset](https://fantinatti.com/ds/Dataset.gif)


## Group:

|Name*|email|
|----|-----|
|Amir Kamaleddine|kamaleda@mcmaster.ca|
|Ernani Fantinatti|fantinae@mcmaster.ca|
|Mohammed Ibraheem|ibraheem@mcmaster.ca|

##### *Names are sorted alphabetically.