
DOCKER_REPO=sergii/foursquare-dataviz
TAG=latest
# TODO: chart prefix
CHART := tf-ipynb

HELM := $(shell which helm)



.PHONY: build
build:
	docker build -t ${DOCKER_REPO}:${TAG} .

.PHONY: run
run:
	docker run -i -t -p 80:80 \
		-e FOURSQUARE_TOKEN=${FOURSQUARE_TOKEN} ${DOCKER_REPO}

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
