from abc import ABC, abstractmethod

class Bank:
    def __init__(self):
        pass
    def account(self,account_no,name):
        self.account_no = account_no
        self.name=name