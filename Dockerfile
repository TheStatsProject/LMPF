FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY README.rst .
COPY app/ ./app/

RUN python -m pip install --no-cache-dir --upgrade pip flit

# Debug: show what got copied
RUN echo "---- /app ----" && ls -l /app
RUN echo "---- /app/app ----" && ls -l /app/app
RUN echo "---- /app/app/__init__.py ----" && cat /app/app/__init__.py
RUN echo "---- /app/pyproject.toml ----" && cat /app/pyproject.toml
RUN echo "---- /app/README.rst ----" && cat /app/README.rst

# This will show logs if Flit fails
RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink || (echo "------ FLIT INSTALL ERROR ------" && false)

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
