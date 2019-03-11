import grpc
import time

import sat_score_pb2
import sat_score_pb2_grpc

def get_one_score(stub, time=2013):
	category = 'mathematics'
	people = 'White'
	#time = 2000

	#category = input('Please input a category(mathematics/writing/reading)')
	#people = input('Please input people(White/Black/Asian/Mexican American/ Puerto Rican)')
	#time = int(input('Please input a year(from 2010-2014)'))

	score = stub.GetScore(sat_score_pb2.RequestScore(category=category, people=people, time=time))
	if not score.score:
		print ("No satisfied score in Server")
		return None
	else:
		print ("Score returned for %s in %s at %s is %s" % (people, category, time, score.score))
		return score.score

def get_score_difference(stub):
	response = stub.AverageScore(generateRequest())
	for re in response:
		if not re.score:
			print ("No satisfied score in Server")
		else:
			print ("Received message: The average score for %s people in %s is %s." % (re.people, re.category, "%.2f" % re.score))

def generateRequest():
	reqs = [sat_score_pb2.RequestScore(category='mathematics', people='White'), 
			sat_score_pb2.RequestScore(category='mathematics', people='a'),
			sat_score_pb2.RequestScore(category='mathematics', people='Asian'),]
	for req in reqs:
		yield req
		time.sleep(0.1)


def test_one():
	channel = grpc.insecure_channel('localhost:50051')
	stub = sat_score_pb2_grpc.SATScoreInfoStub(channel)
	assert get_one_score(stub, 2013) == 300

def test_two():
	channel = grpc.insecure_channel('localhost:50051')
	stub = sat_score_pb2_grpc.SATScoreInfoStub(channel)
	assert get_one_score(stub) == 300

def test_three():
	channel = grpc.insecure_channel('localhost:50051')
	stub = sat_score_pb2_grpc.SATScoreInfoStub(channel)
	assert get_one_score(stub, 2016) == 300
def test_four():
	channel = grpc.insecure_channel('localhost:50051')
	stub = sat_score_pb2_grpc.SATScoreInfoStub(channel)
	assert get_one_score(stub, 2000) == 300
def test_five():
	channel = grpc.insecure_channel('localhost:50051')
	stub = sat_score_pb2_grpc.SATScoreInfoStub(channel)
	assert get_score_difference(stub)

#if __name__ == '__main__':
#	run()