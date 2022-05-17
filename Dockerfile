FROM brunneis/python:2.7.16-ubuntu

RUN apt-get update && \
	apt-get install --no-install-recommends -y gcc && \
	apt-get install --no-install-recommends -y python-dev && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip && \
	pip install pyinstaller==3.6 && \
	pip install vnc2flv

WORKDIR "/mnt"

ENTRYPOINT ["pyinstaller", "--onefile", "/usr/local/bin/flvrec.py", "--distpath", "./lib"]







