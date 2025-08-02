WORKDIR /app
COPY app/ ./app/
COPY pyproject.toml .
COPY README.rst .
RUN echo "---- /app ----" && ls -l /app
RUN echo "---- /app/app ----" && ls -l /app/app
RUN echo "---- /app/app/__init__.py ----" && cat /app/app/__init__.py
RUN echo "---- /app/pyproject.toml ----" && cat /app/pyproject.toml
RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink || (echo "------ FLIT INSTALL LOG ------" && cat /root/.cache/pip/log/debug.log && false)
RUN python -m pip install --no-cache-dir --upgrade pip flit
RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
