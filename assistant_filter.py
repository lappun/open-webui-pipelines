"""
title: Assistant Filter Pipeline
author: Andrew Tait Gehrhardt
date: 2024-06-15
version: 1.0
license: MIT
description: A pipeline for controlling Assistant entities based on their easy names. Only supports lights at the moment.
requirements: pytz, difflab
"""
import requests
from typing import Literal, Dict, Any
from datetime import datetime
import pytz
from difflib import get_close_matches

from blueprints.function_calling_blueprint import Pipeline as FunctionCallingBlueprint

class Pipeline(FunctionCallingBlueprint):

    class Tools:
        def __init__(self, pipeline) -> None:
            self.pipeline = pipeline

        def get_current_time(self) -> str:
            """
            Get the current time in Hong Kong.

            :return: The current time in Hong Kong.
            """
            now_hk = datetime.now(pytz.timezone('Asia/Hong_Kong'))  # Get the current time in Hong Kong
            current_time = now_hk.strftime("%I:%M %p")  # %I for 12-hour clock, %M for minutes, %p for am/pm
            return f"ONLY RESPOND 'Current time is {current_time}'"

        def get_current_date(self) -> str:
            """
            Get the current date in Hong Kong.
            :return: The current date in Hong Kong.
            """
            now_hk = datetime.now(pytz.timezone('Asia/Hong_Kong'))   # Get the current time in Hong Kong
            current_date = now_hk.strftime("%A, %B %d")    # Get the current date in Hong Kong
            return f"ONLY RESPOND 'Current date is {current_date}'"

    def __init__(self):
        super().__init__()
        self.name = "My Tools Pipeline"
        self.valves = self.Valves(
            **{
                **self.valves.model_dump(),
                "pipelines": ["*"],  # Connect to all pipelines
            },
        )
        self.tools = self.Tools(self)