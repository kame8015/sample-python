#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3


# class STSClient:
#     def __init__(self):
#         self.client = boto3.client("sts")

#     def get_account_id(self):
#         response = self.client.get_caller_identity()
#         account_id = response.get("Account")
#         return account_id


if __name__ == "__main__":
    # account_id = STSClient().get_account_id()
    # print(account_id)
    print("Invoked!!!!!!")