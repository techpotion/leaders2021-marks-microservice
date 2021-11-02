generate:
	rm -rf gen/pb/*.py
	mkdir -p gen/pb

	python -m grpc_tools.protoc -I=proto/ -I=${GOPATH}/src/ --python_out=./gen/pb --grpc_python_out=./gen/pb proto/microservice.proto