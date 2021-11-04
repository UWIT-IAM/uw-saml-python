FROM ghcr.io/uwit-iam/uw-saml-poetry:latest AS dependency-image
WORKDIR build/
RUN pip uninstall -y uw-saml
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction --no-root

FROM dependency-image AS test-image
COPY uw_saml2 ./uw_saml2
COPY tests/ ./tests
RUN poetry install --no-interaction
