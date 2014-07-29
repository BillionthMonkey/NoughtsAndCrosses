NoughtsAndCrosses
==================

A [test-driven development](http://en.wikipedia.org/wiki/Test-driven_development) kata inspired by ["Test-driven development as if you mean it"](http://www.infoq.com/presentations/TDD-as-if-You-Meant-It) carried out with [Mark Withall](https://github.com/MarkWithall).

Before we started; we roughly noted down our goals:

 * Moves are provided to [it]
   - checks the move's legal
 * [it] then says if:
   - player that played last move won
   - "board" full (implies draw)

Development Environment Set-up
-------------------------------

Get **pip** and **virtualenv**
 * `easy_install pip`
 * `pip install virtualenv`

Go to the **NoughtsAndCrosses** directory and create and activate the virtual environment
 * `virtualenv venv`
 * `. venv/bin/activate`

Install/update packages
 * `pip install -r requirements.txt`
 * or `pip install --upgrade -r requirements.txt`

Running the Tests
------------------

The tests can be run continuously with `py.test --looponfail nac.py` or `py.test -f nac.py`
