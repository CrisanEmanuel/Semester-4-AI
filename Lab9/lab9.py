import csv
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from gensim.scripts.glove2word2vec import glove2word2vec
import gensim


def loadSomeData(fileName):
    data = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row  # header
            else:
                data.append(row)
            line_count += 1

    inputs = [data[i][0] for i in range(len(data))]
    outputs = [data[i][1] for i in range(len(data))]
    labelNames = list(set(outputs))

    return inputs, outputs, labelNames


def splitData(inputs, outputs):
    # prepare data for training and testing
    np.random.seed(5)
    # noSamples = inputs.shape[0]
    noSamples = len(inputs)
    indexes = [i for i in range(noSamples)]
    trainSample = np.random.choice(indexes, int(0.8 * noSamples), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    return trainInputs, trainOutputs, testInputs, testOutputs


def loadWordEmbeddingModel(model_path, modelType):
    model = None
    if modelType == 'word2vec':
        model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)
    elif modelType == 'fasttext':
        model = gensim.models.fasttext.load_facebook_model(model_path)
    elif modelType == 'glove':
        word2vec_output_file = model_path + '.word2vec'
        glove2word2vec(model_path, word2vec_output_file)
        model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
    return model

def featureComputation(model, data):
    features = []
    phrases = [phrase.split() for phrase in data]
    for phrase in phrases:
        # compute the embeddings of all the words from a phrase (words of more than 2 characters) known by the model
        # vectors = [model[word] for word in phrase if (len(word) > 2) and (word in model.vocab.keys())]
        vectors = [model[word] for word in phrase if (len(word) > 2) and (word in model.index_to_key)]
        if len(vectors) == 0:
            result = [0.0] * model.vector_size
        else:
            result = np.sum(vectors, axis=0) / len(vectors)
        features.append(result)
    return features

def featureComputationForFasttext(model, data):
    features = []
    phrases = [phrase.split() for phrase in data]
    for phrase in phrases:
        vectors = [model.wv.get_vector(word) for word in phrase if (len(word) > 2) and (word in model.wv.key_to_index)]
        if len(vectors) == 0:
            result = [0.0] * model.vector_size
        else:
            result = np.sum(vectors, axis=0) / len(vectors)
        features.append(result)
    return features

def unsupervisedClassification(trainFeatures, testFeatures, testInputs, testOutputs, labelNames, reviewFeature):
    unsupervisedClassifier = KMeans(n_clusters=2, random_state=0)
    unsupervisedClassifier.fit(trainFeatures)

    # testare model
    computedTestIndexes = unsupervisedClassifier.predict(testFeatures)
    computedTestOutputs = [labelNames[value] for value in computedTestIndexes]
    for i in range(0, len(testInputs)):
        print(testInputs[i], " -> ", computedTestOutputs[i])

    # compute accuracy
    print("acc: ", accuracy_score(testOutputs, computedTestOutputs))

    # Predict label for the new review
    reviewIndex = unsupervisedClassifier.predict(reviewFeature)
    predictedLabel = labelNames[reviewIndex[0]]
    print("Predicted label for the review:", predictedLabel)


def run():
    inputs, outputs, labelNames = loadSomeData("data/reviews_mixed.csv")
    trainInputs, trainOutputs, testInputs, testOutputs = splitData(inputs, outputs)

    word2vecModel300 = loadWordEmbeddingModel("models/GoogleNews-vectors-negative300.bin", modelType='word2vec')
    gloveModel = loadWordEmbeddingModel('models/glove.6B.100d.txt', modelType='glove')
    fasttextModel = loadWordEmbeddingModel('models/cc.ro.300.bin', modelType='fasttext')

    review = ("By choosing a bike over a car, I’m reducing my environmental footprint. Cycling promotes eco-friendly "
              "transportation, and I’m proud to be part of that movement.")

    reviewFeatureWord2Vec = featureComputation(word2vecModel300, [review])
    reviewFeatureGloVe = featureComputation(gloveModel, [review])
    reviewFeatureFastText = featureComputationForFasttext(fasttextModel, [review])

    trainFeatureWord2Vec = featureComputation(word2vecModel300, trainInputs)
    testFeatureWord2Vec = featureComputation(word2vecModel300, testInputs)

    trainFeatureGloVe = featureComputation(gloveModel, trainInputs)
    testFeatureGloVe = featureComputation(gloveModel, testInputs)

    trainFeatureFastText = featureComputationForFasttext(fasttextModel, trainInputs)
    testFeatureFastText = featureComputationForFasttext(fasttextModel, testInputs)

    # word2vec
    unsupervisedClassification(trainFeatureWord2Vec, testFeatureWord2Vec, testInputs, testOutputs, labelNames, reviewFeatureWord2Vec)
    # GloVe
    # unsupervisedClassification(trainFeatureGloVe, testFeatureGloVe, testInputs, testOutputs, labelNames, reviewFeatureGloVe)
    # FastText
    # unsupervisedClassification(trainFeatureFastText, testFeatureFastText, testInputs, testOutputs, labelNames, reviewFeatureFastText)
