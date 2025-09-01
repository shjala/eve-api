.DEFAULT_GOAL := help

help:
	@echo "Available targets:"
	@echo "  help              Show this help message"
	@echo "  proto             Build protobuf files (default target)"
	@echo "  swagger           Generate Swagger/OpenAPI documentation"

proto-container:
	docker build -f .devcontainer/Dockerfile -t eve-api-builder .

proto-diagram:
	protodot -inc /usr/local/include -src ./proto/config/devconfig.proto -output devconfig -generated ./images
	dot ./images/devconfig.dot -Tpng -o ./images/devconfig.png
	dot ./images/devconfig.dot -Tsvg -o ./images/devconfig.svg
	echo generated ./images/devconfig.*

.PHONY: proto-api-% proto proto-container proto-local swagger swagger-local

proto: proto-container
	docker run --rm --env HOME=/tmp -v $(PWD):/src -w /src -u $$(id -u) eve-api-builder make proto-local

proto-local: go go-vet python proto-diagram
	@echo Done building protobuf, you may want to vendor it into your packages, e.g. pkg/pillar.
	@echo See ./go/README.md for more information.

go: PROTOC_OUT_OPTS=paths=source_relative:
go: proto-api-go
go-vet:
	go mod tidy -C go/
	go vet -C go ./...

python: proto-api-python

proto-api-%:
	rm -rf $*/*/; mkdir -p $* # building $@
	protoc -I./proto --$(*)_out=$(PROTOC_OUT_OPTS)./$* proto/*/*.proto

swagger: proto-container
	docker run --rm --env HOME=/tmp -v $(PWD):/src -w /src -u $$(id -u) eve-api-builder make swagger-local

swagger-local:
	rm -rf swagger/ && mkdir -p swagger
	protoc -I./proto --openapiv2_out=swagger/ proto/*/*.proto
