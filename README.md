# Dockerized-Genotype-Phenotype-Relational-Graph-Generator

Dependency versions: Docker v24.0.7, mongoDB v8.0.4, python v3.10.12



This Graph generator reads in diseases/phenotypes and genes from a json file that must be formatted as follows:
phenotype/disease(string):related genes (array). Example provided below.
![image](https://github.com/user-attachments/assets/734d02a3-b941-402b-b9e8-45b12972f23e)

The user is then prompted and specifies what gene or phenotype/disease they would like to begin with and 
how many degrees of relation from the original target they would like to display, followed by the file name to
save the graph to. Example below:
![image](https://github.com/user-attachments/assets/8b38b5a5-ce3b-4819-9376-5cec99ecd8ea)


The program then creates and presents a graph showing potential relationships of interest between the diseases/phenotypes and
their associated genes:
![BARD1Degree4](https://github.com/user-attachments/assets/9dc7839e-7012-428a-b7f0-be7d9daa6ad8)

