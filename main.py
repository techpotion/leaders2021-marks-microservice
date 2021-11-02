import grpc
from concurrent import futures
import time
import gen.pb.microservice_pb2 as pb2
import gen.pb.microservice_pb2_grpc as pb2_grpc


class Microservice(pb2_grpc.MicroserviceServicer):
    def __init__(self, *args, **kwargs):
        pass

    def GetMark(self, request, context):
        print(request)
        result = {
            'mark': 6.8
        }
        return pb2._MARKS_GETRESPONSE(**result)


def serve():
    print('Starting microservice on :3300')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MicroserviceServicer_to_server(Microservice(), server)
    server.add_insecure_port('[::]:3300')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()