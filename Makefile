
DOCKER_REPO=gcr.io/brainscode-140622/tf-ipynb
TAG=v1
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
	gcloud docker -- push ${DOCKER_REPO}:${TAG}

# TODO: add env here
.PHONY: deploy
deploy:
	${HELM} lint ${CHART}
	${HELM} upgrade --install ${CHART} ./${CHART} \
		--debug

.PHONY: deploy
purge:
	helm del --purge ${CHART}
