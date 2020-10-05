# -*- coding: utf-8 -*-
"""
Represents result of an operation.
"""

class OperationResponse:

    def __init__(self, result, message, status, commandId, *args, **kwargs):
        self.result = result
        self.message = message
        self.status = status
        self.command_id = commandId
        
    def success(self):
        return self.status