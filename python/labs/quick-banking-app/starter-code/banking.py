#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code
import time

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance

    def __str__(self):
        return('The label of your bank account is {l} and the balance is {b}'.format(l=self.label, b=self.balance))

    def withdraw(self, withd):
        if withd > self.balance or withd <= 0:
            print("You are trying to withdraw more than you have. Maybe try withdrawing a smaller amount.")
            self.balance = self.balance
        else:
            self.balance = self.balance - withd
            print("Your new balance is {w}".format(w=self.balance))

    def deposit(self, depo):
        if depo <= 0:
            print("You can't withdraw a negative amount or a zero amount.")
        else:
            self.balance += depo
            print("Your new balance is {d}".format(d=self.balance))

    def rename(self, label2):
        if label2 == '' or label2 == ' ':
            print("You need a label for your bank account. Try again with a non-empty word.")
        else:
            self.label = label2
            print("The new label of your bank account is {a}".format(a=self.label))

    def transfer(self, dest_object, amount):
        if amount > self.balance or amount <= 0:
            print("You are trying to transfer more money than is in your account or you are transferring a non-positive amount.")
        else:
            dest_object.balance += amount
            self.balance -= amount

class Transaction(object):
    def __init__(self, time, type, amount, dest_account):
        self.time = time.time()
        self.type = type
        self.amount = amount
        self.dest_account = dest_account

    def __str__(self):
        if self.amount < 0:
            return('withdraw {a}'.format(a=self.amount))
        if self.amount > 0:
            return ('deposit {b}'.format(b=self.amount))
