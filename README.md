# Dockerized-Genotype-Phenotype-Relational-Graph-Generator

Technologies used: Docker v24.0.7, python v3.10

The Dockerized-Gene-Phenotype-Relational-Graph-Generator takes a gene or disease phenotype as input(e.g. "colorectal cancer" or "BARD1")
and a degree number. The graph generator then reads in disease phenotypes and their associated genes of proliferation. The generator then
connects the starting disease phenotypes or gene to all to nodes of its related genes or disease phenotypes, or vice versa. This process is then
repeated for all the nodes added in the previous iteration for the number of degrees specified.

Example input:
![image](https://github.com/user-attachments/assets/c40b11ee-9e17-4912-93cd-7545ce2efb4b)

Example output:
![image](https://github.com/user-attachments/assets/b1a9321b-70b8-4b28-9838-a3a126392056)
