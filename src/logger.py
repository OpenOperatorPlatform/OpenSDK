#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# Copyright 2025-present by Software Networks Area, i2CAT.
# All rights reserved.
#
# This file is part of the Federation SDK
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Contributors:
#   - Sergio Giménez (sergio.gimenez@i2cat.net)
##
import logging
import sys

from colorlog import ColoredFormatter

APP_LOGGER_NAME = "edgecloud"
COLORED_FORMATERR = (
    "%(log_color)s%(levelname)s%(reset)s | "
    "[%(log_color)s%(name)s%(reset)s:%(log_color)s%(lineno)d%(reset)s] "
    "%(log_color)s%(message)s%(reset)s"
)
FILE_FORMATTER = "[%(asctime)s] {%(name)s: %(lineno)d} %(levelname)s - %(message)s"


def setup_logger(logger_name=APP_LOGGER_NAME, is_debug=True, file_name=None):

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG if is_debug else logging.INFO)

    colored_formatter = ColoredFormatter(COLORED_FORMATERR)
    file_formatter = logging.Formatter(FILE_FORMATTER)

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(colored_formatter)
    logger.handlers.clear()
    logger.addHandler(sh)

    if file_name:
        fh = logging.FileHandler(file_name)
        fh.setFormatter(file_formatter)
        logger.addHandler(fh)

    return logger


def get_logger(module_name):
    return logging.getLogger(APP_LOGGER_NAME).getChild(module_name)
