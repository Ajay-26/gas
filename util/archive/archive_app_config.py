# archive_config.py
#
# Copyright (C) 2011-2021 Vas Vasiliadis
# University of Chicago
#
# Set app configuration options for archive utility
#
##
__author__ = 'Vas Vasiliadis <vas@uchicago.edu>'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

  CSRF_ENABLED = True

  AWS_REGION_NAME = "us-east-1"

  # AWS DynamoDB table
  AWS_DYNAMODB_ANNOTATIONS_TABLE = "<CNetID>_annotations"

### EOF