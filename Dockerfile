FROM python:3.10

COPY . /testapp
WORKDIR /testapp

RUN pip install -r requirements/base.pip

RUN chmod +x /testapp/testing_test.py

CMD [ "pytest", "/testing_test.py", "--dist=loadscope", "--tx", "9*popen//python=python3.10", "-n", "9", "--reruns", "1", "--only-rerun", "JavascriptException", "--only-rerun", "ElementClickInterceptedException"  ]
