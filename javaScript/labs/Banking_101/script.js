// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let customer_name;
let balance;
let pass;

// initializes global variables
function openAccount(name, passwd){
  balance = 0;
  // Set the value for customer_name equal to name below
 customer_name = name;
 pass = passwd;
  return name + " has opened a new account with a balance of " + balance//write the statment you need to return here
}

function deposit(value){
  // update the value of balance
  balance = balance + value;
  //return the correct statement
  if (logged_in == false){
    return "You can't deposit without being logged in. Try logging in again.";
  }
  else {
    return customer_name + " has deposited $" + value + "." + " " + customer_name + "\'s total balance is $" + balance + ".";
  }
}

function withdraw(amt){
  //update the value of balance
  difference = balance - amt;
  more = amt - balance;
  if (logged_in == false){
    return "You can't withdraw without being logged in. Try logging in again.";
  }
  else if (difference < 0){
    return "Sorry " + customer_name + " but the amount you're trying to withdraw is greater than your balance. You need $" + more + " more.";
  }
  //return the correct statement
  else if (difference >= 0){
    balance = balance - amt
    return customer_name + " has withdrawn $" + amt + "." + " " + customer_name + " has $" + balance + " remaining."
}
}

function login(name, pwd){
  if (name == customer_name && pwd == pass){
    logged_in = true;
    return name + " has logged in."
  }
  else{
    logged_in = false;
    return "Incorrect log in, " + name + ". Try again."
  }
}

function logout(){
  logged_out = false;
  return customer_name + " has logged out."
}

// Write your script below
console.log(openAccount("Akshara", "Cheddar"));
console.log(login("Aksh", "Cheddar"));
console.log(deposit(4000));
console.log(withdraw(500));
