.PHONY: sources clean spec

DIST    ?= epel-6-x86_64

VENV    ?= .venv
PIP     ?= $(VENV)/bin/pip
PYTHON  ?= $(VENV)/bin/python
PYVER   ?= python2.7
PROGRAM ?= pyscaleio
PACKAGE := python-scaleio
GIT     := $(shell which git)

VERSION = $(shell rpm -q --qf "%{version}\n" --specfile $(PACKAGE).spec | head -1)
RELEASE = $(shell rpm -q --qf "%{release}\n" --specfile $(PACKAGE).spec | head -1)


HEAD_SHA := $(shell git rev-parse --short --verify HEAD)
TAG      := $(shell git show-ref --tags -d | grep $(HEAD_SHA) | \
                    git name-rev --tags --name-only $$(awk '{print $2}'))

BUILDID := %{nil}
ifndef TAG
BUILDID := .$(shell date --date="$$(git show -s --format=%ci $(HEAD_SHA))" '+%Y%m%d%H%M').git$(HEAD_SHA)
endif

spec: ## create spec file
	@git cat-file -p $(HEAD_SHA):$(PACKAGE).spec | sed -e 's,BUILDID,$(BUILDID),g' > $(PACKAGE).spec

sources: clean spec
	@git archive --format=tar --prefix=$(PROGRAM)-$(VERSION)/ $(HEAD_SHA) | \
	     gzip > $(PROGRAM)-$(VERSION).tar.gz

clean:
	@rm -rf .coverage .coverage-report .venv/ build/ dist/ \
			.tox/ *.egg* .eggs/ rpms/ srpms/ *.tar.gz *.rpm
