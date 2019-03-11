import time
from concurrent import futures
import grpc

import sqlite3

import sat_score_pb2
import sat_score_pb2_grpc

_ONE_DAY_IN_SECONDS = 24 * 60 * 60


def get_one_score(request):
	t = (request.people, request.category, request.time)
	conn = sqlite3.connect('SAT_score.db')
	print("Database connected successfully")
	c = conn.cursor()
	c.execute("SELECT * FROM scores WHERE people=? AND category=? AND time=?", t)
	score = c.fetchone()
	if not score:
		return None
	else:
		return score[3]

def get_ave_score(request):
	t = (request.people, request.category)
	conn = sqlite3.connect('SAT_score.db')
	print("Database connected successfully")
	c = conn.cursor()
	i = 0
	total = 0
	for row in c.execute("SELECT * FROM scores WHERE people=? AND category=?",t):
		total += row[3]
		i += 1
	if i == 0:
		return None
	else:
		return (total/i)

class SATScoreInfo(sat_score_pb2_grpc.SATScoreInfoServicer):
	def __init__(self):
		print ("Initializing")

	def GetScore(self, request, context):
		score = get_one_score(request)
		return sat_score_pb2.Score(score=score)
	def AverageScore(self, request_iterator, context):
		for req in request_iterator:
			aveScore = get_ave_score(req)
			yield sat_score_pb2.AveScore(category=req.category, people=req.people, score=aveScore)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sat_score_pb2_grpc.add_SATScoreInfoServicer_to_server(SATScoreInfo(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
