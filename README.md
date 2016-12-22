# Project-E-commercial-Product-Recommendations
Recommendation System Using Spark and System G


There are three parts of code: 

(1). DataRetrieve.ipynb

It serves to preprocess the dataset. 

Put amazon-meta.txt(input dataset) in the same directory of DataRetrieve.ipynb

Run the program
The output will appear in the same directory with the name rater.txt



(2). spark_recommendation.py

It serves to do recommendation on spark. 

Copy the path of your inputfile rater.txt

Replace filename with the path copied and save
Run this python script with the command ./pyspark spark_recommendation.py
It will output MSE, as well as the ten top recommendation results. 

(3). system g part code(code is put in file 'step 3 systemg part code.pdf')

System G is used for item to item recommendation part by Colfilter function.

Using function analytic_colfilter, the analytic performs BFS for each vertex x up to --depth (must be an even number, default is 4), computes the number of paths N(x, y) from x to every vertex in Y, and ranks these vertices based on their N(x, y) values in a descending order. 

So in our example, we will recommend top 10 items for each item in part 2.


 
