IMAGE_TAG := local/sswitch:latest

.PHONY: image
image:
	docker build -t $(IMAGE_TAG) .
