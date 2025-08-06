The Truth Project: Labor Market and Population Forecasting Toolkit
=================================================================

**The Truth Project** is an open-source toolkit designed for labor market and population forecasting.  
This project is built using 100% Python (FastAPI + MongoDB) and is ready for deployment on Railway with seamless GitHub integration.

Features
--------

- FastAPI backend for high-performance APIs
- MongoDB integration for scalable data storage
- 100% Python stack (no Node/React)
- Ready-to-deploy with Docker and Railway
- Easy connection to GitHub for CI/CD

Project Links
-------------

- Live Documentation: https://TheStatsProject.github.io/finance-models-docs/
- Project Repository: https://github.com/TheStatsProject/LMPF

Getting Started
---------------

1. **Clone the repository:**

   ::

     git clone https://github.com/TheStatsProject/LMPF.git
     cd LMPF

2. **Configure environment variables:**

   Set your MongoDB URI in your Railway or local environment as ``MONGODB_URI``.

3. **Build and run with Docker:**

   ::

     docker build -t the-truth-project .
     docker run -d -p 8000:8000 -e MONGODB_URI="your_mongo_uri" the-truth-project

4. **Or run locally:**

   ::

     pip install -r app/requirements.txt
     export MONGODB_URI="your_mongo_uri"
     uvicorn app.main:app --reload

API Documentation
-----------------

Once running, access:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

Project Structure
-----------------

::

  LMPF/
  ├── app/
  │   ├── main.py
  │   └── requirements.txt
  ├── Dockerfile
  └── README.rst

Contributing
------------

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

License
-------

MIT License. See ``LICENSE`` for details.
