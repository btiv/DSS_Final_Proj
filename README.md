# About the project 
This project is part of the Data Science for Sustainability class at Tufts University. 

Deforestation of the Amazon rainforest, the largest rainforest in the world, poses a multitude of adverse effects on a local and global scale. However, these effects can be mitigated with public policy, which is often driven by novel academic research. In this project, we aim to answer the following question:

***RQ1:*** Do research articles focused on the Brazilian Amazon published by domestic (Brazilian) authors result in a greater reduction in the deforestation rate compared to articles published by solely international authors?

***RQ2:*** Additionally, does global collaboration (between Brazilian and non-Brazilian authors) result in the greatest reduction in deforestation?

In order to answer these questions, we use various statistical models to uncover these relationships. We perform two case studies, the first analyzing research and deforestation in the Brazilian Amazon and the second broadening the scope to encompass research on deforestation of all Brazilian primary forests. 

Our results suggest that domestic and collaborative research have a quicker impact on reducing deforestation in the Brazilian Amazon than research performed by international authors. However, the results of the second case study on deforestation of all Brazilian primary forests were less conclusive and require additional analysis.

## File descriptions
1. [Data](https://github.com/btiv/DSS_Final_Proj/tree/main/data) is being kept in the data folder. This folder contains 2 sub folders, each sub folder contains data for each case study: the [Brazilian Amazon](https://github.com/btiv/DSS_Final_Proj/tree/main/data/Amazon_research), and all [Brazilian primary forests](https://github.com/btiv/DSS_Final_Proj/tree/main/data/Brazil_research). We provided both raw and cleaned data. 
2. Notebook file contains all the code used for data preprocessing and run the model 
   1. [amazon_casestudy.ipynb](https://github.com/btiv/DSS_Final_Proj/blob/main/notebook/amazon_casestudy.ipynb): notebook will all model created for all Brazilian Amazon case study.
   2. [brazil_casestudy.ipynb](https://github.com/btiv/DSS_Final_Proj/blob/main/notebook/brazil_casestudy.ipynb): notebook will all model created for all Brazilian primary forests case study.
   3. [WoS_data_cleaning.ipynb](https://github.com/btiv/DSS_Final_Proj/blob/main/notebook/WoS_data_cleaning.ipynb): notebook to filtering data.

(README as of 4/10/22)