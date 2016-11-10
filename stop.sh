#!/bin/bash
ps aux | grep python | grep recommend | awk '{print $2}' | xargs kill -9
