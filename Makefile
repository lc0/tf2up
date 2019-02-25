
DOCKER_REPO=sergii/tf-ipynb
TAG=latest
# TODO: chart prefix
CHART := tf-ipynb

HELM := $(shell which helm)



.PHONY: build
build:
	docker build -t ${DOCKER_REPO}:${TAG} .

.PHONY: run
run:
	docker run -it -p 8080:80 \
		-e FOO=${BAR} ${DOCKER_REPO}

.PHONY: push
push:
	docker push ${DOCKER_REPO}:${TAG}

# TODO: add env here
.PHONY: deploy
deploy:
	${HELM} lint ${CHART}
	${HELM} upgrade --install ${CHART} ./${CHART} \
		--debug

.PHONY: deploy
purge:
	helm del --purge ${CHART}
