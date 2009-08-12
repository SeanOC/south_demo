=======================
Django NYC - South Demo
=======================

This is a demo application used in Sean O'Connor's talk from 8/11/09 at Django NYC.

Getting Started
===============
Run the following commands to get up and running with the demo app::

	git clone git://github.com/SeanOC/south_demo.git
	cd south_demo
	virtualenv --no-site-packages env
	source env/bin/activate
	pip install -r requirements.txt
	cd south_demo
	./manage.py runserver
	
Talk Video
==========

To see a recording of the talk you can check it out at http://vimeo.com/6059269.


Talk Summary
============

* `South <http://south.aeracode.org/>`_ is an awesome tool for tracking and automating database schema and data changes.
* The South website at http://south.aeracode.org/ is a great resource for documentation and tutorials.
* Automating migrations eases team based development, deployment, and makes continuous integration possible.
* Don't start using a schema migration tool until you have data that you care about.  Start with db resets and test data generation scripts.
* Schema changes and data changes need to contained in separate migrations.
* Automated migrations are great but always check their results and don't be afraid to change things.
* Something still suck (i.e. doing major changes with table inheritance) but these are nasty corner cases no matter how you handle them.
* Always use the ORM freezer for data migrations.
* Always declare dependencies when making changes which reference data outside the current app.
