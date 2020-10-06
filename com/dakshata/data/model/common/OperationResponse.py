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
        
    def __str__(self):
        return "OperationResponse[Result = {0}, Status = {1}, Message = {2}, Command Id = {3}]".format( \
            self.result, self.status, self.message, self.command_id)
        