#!/usr/bin/python3

import sys
import glob
import os
import numpy as np
import operator
import math

trainingDigits = sys.argv[1]
testDigits = sys.argv[2]

def trainDataSet():
  groupData = []
  labels = []
  for trainingDigits_file in glob.glob(os.path.join(trainingDigits, '*.txt')):
    try:
      f = open(trainingDigits_file, "rt")
      labels.append(int(trainingDigits_file.split('/')[1][0]))
      data = []
      for line in f:
        if line[-1] == '\n':
          temp = list(line[: -1])
        else:
          temp = list(line)
        temp = list(map(int, temp))
        data.extend(temp)
      groupData.append(data)
    except FileNotFoundError: # 만약 파일이 없다면 이 예외가 발생
      print("파일이 없습니다.")
    finally:
      f.close()
  group = np.array(groupData)

  return group, labels

def testDataSet():
  groupData = []
  labels = []
  for testDigits_file in glob.glob(os.path.join(testDigits, '*.txt')):
    try:
      f = open(testDigits_file, "rt")
      labels.append(int(testDigits_file.split('/')[1][0]))
      data = []
      for line in f:
        if line[-1] == '\n':
          temp = list(line[: -1])
        else:
          temp = list(line)
        temp = list(map(int, temp))
        data.extend(temp)
      groupData.append(data)
    except FileNotFoundError: # 만약 파일이 없다면 이 예외가 발생
      print("파일이 없습니다.")
    finally:
      f.close()

  group = np.array(groupData)

  return group, labels

def classify0(inX, dataSet, labels, k):
  dataSetSize = dataSet.shape[0]
  diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
  sqDiffMat = diffMat ** 2
  sqDistances = sqDiffMat.sum(axis = 1)
  distances = sqDistances ** 0.5
  sortedDistIndicies = distances.argsort()
  classCount = {}
  for i in range(k):
    voteIlabel = labels[sortedDistIndicies[i]]
    classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
  sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
  return sortedClassCount[0][0]

trainGroup, trainLabels = trainDataSet()
testGroup, testLabels = testDataSet()

error = 0
for k in range(1, 21): 
  for i in range(testGroup.shape[0]):
    if testLabels[i] != classify0(testGroup[i], trainGroup, trainLabels, k):
      error += 1
  print(math.trunc(error / testGroup.shape[0] * 100))
  error = 0