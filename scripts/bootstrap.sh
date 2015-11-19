#!/bin/bash
set -e
git submodule update --init --recursive
sudo apt-get install python-pip python-musicbrainz2 python-alsaaudio python-mysqldb mysql-server python-gst0.10 gstreamer0.10-plugins-base gstreamer0.10-plugins-good gstreamer0.10-plugins-ugly gstreamer0.10-plugins-bad python-virtualenv
python scripts/generate-virtualenv-bootstrap.py

if [ ! -d "ENV" ]; then
	python virtualenv-bootstrap.py ENV
fi

. "$(pwd)/ENV/bin/activate"
python scripts/setupdb.py
echo ""
echo "Bootstrapped successfully"
echo "Run 'python src/manage.py runserver' to start the development server"
