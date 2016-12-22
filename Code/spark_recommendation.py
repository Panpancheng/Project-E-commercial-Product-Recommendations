from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark import SparkContext
sc =SparkContext()

# Load and parse the data
filename = "/home/joanna/dataset/rater.txt"
data = sc.textFile(filename)
ratings = data.map(lambda l: l.split('\t'))\
.map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))

# Build the recommendation model using Alternating Least Squares
rank = 10
numIterations = 10
model = ALS.train(ratings, rank, numIterations)

# Evaluate the model on training data
testdata = ratings.map(lambda p: (p[0], p[1]))
predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
print("Mean Squared Error = " + str(MSE))

# Save and load model
model.save(sc, "/home/joanna/dataset/myCollaborativeFilter")
sameModel = MatrixFactorizationModel.load(sc, "/home/joanna/dataset/myCollaborativeFilter")

#List top ten recommendation result
predictions.take(10)