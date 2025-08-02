WORKDIR /app
COPY app/ ./
COPY pyproject.toml .
COPY README.rst .
RUN ls -l /app
RUN cat /app/__init__.py
RUN python -m pip install --no-cache-dir --upgrade pip flit
RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
