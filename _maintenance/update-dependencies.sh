#!/usr/bin/env bash

maintenance=$(realpath $(dirname $0))
cd ${maintenance}/..


echo "Updating Webis commons.."
git submodule update --recursive --remote

cd ${maintenance}
