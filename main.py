import grpc
from concurrent import futures
import gen.pb.microservice_pb2 as pb2
import gen.pb.microservice_pb2_grpc as pb2_grpc
from src.svm import SVM

class Microservice(pb2_grpc.MicroserviceServicer):
    def __init__(self, *args, **kwargs):
        self.__svm = SVM()

    def GetMark(self, request, context):
        self.__svm.get_mark(request)
        result = {
            'mark': self.__svm.get_mark(request)
        }
        return pb2.Marks.GetResponse(**result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MicroserviceServicer_to_server(Microservice(), server)
    server.add_insecure_port('[::]:3300')
    print('Started microservice on :3300')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

