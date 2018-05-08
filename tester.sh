#!/bin/bash

#Test using vagrant
vagrant ssh-config > .vagrant/ssh-config
py.test --hosts=default --ssh-config=.vagrant/ssh-config ./tests/tests.py
