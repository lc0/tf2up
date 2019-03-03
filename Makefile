
DOCKER_REPO=gcr.io/brainscode-140622/tf-ipynb
TAG=v34
# TODO: chart prefix
CHART := tf-ipynb

HELM := $(shell which helm)



.PHONY: build
build: lint
	docker build -t ${DOCKER_REPO}:${TAG} .

.PHONY: run
run:
	docker run -it -p 8080:80 \
		-v /tmp/notebooks:/notebooks \
		-e FOO=${BAR} ${DOCKER_REPO}:${TAG}

.PHONY: push
push:
	gcloud docker -- push ${DOCKER_REPO}:${TAG}

# TODO: add env here
.PHONY: deploy
deploy:
	${HELM} lint ${CHART}
	${HELM} upgrade --install ${CHART} ./${CHART} \
		--debug #--dry-run

.PHONY: purge
purge:
	helm del --purge ${CHART}

# ====== nbdime part

.PHONY: nbbuild
nbbuild:
	docker build -t ${DOCKER_REPO}.nbdime:${TAG} -f Dockerfile.nbdime .

.PHONY: nbrun
nbrun:
	docker run -it -p 8080:81 \
		-v /tmp/tft:/notebooks \
		-e FOO=${BAR} ${DOCKER_REPO}.nbdime:${TAG}

.PHONY: nbpush
nbpush:
	gcloud docker -- push ${DOCKER_REPO}.nbdime:${TAG}

# ===== lint
.PHONY: lint
lint:
	mypy --config-file=configs/mypy.ini src/main.py