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

// Use querySelector to store the div in a variable.

//red button
let redButton = document.querySelector('#red');

redButton.addEventListener('click', e => {
  console.log("You clicked the red button!");
})

redButton.addEventListener('click', e => {
  responseBox.style.backgroundColor = "red";
})

redButton.addEventListener('click', e => {
  responseBox.innerText = "red";
})

// green button (e is the same thing as having (), nothing but a placeholder)

let greenButton = document.querySelector('#green');

greenButton.addEventListener('click', e => {
  console.log("You clicked the green button!");
})

greenButton.addEventListener('click', e => {
  responseBox.style.backgroundColor = "green";
})

greenButton.addEventListener('click', e => {
  responseBox.innerText = "green";
})

//blue button

let blueButton = document.querySelector('#blue');

blueButton.addEventListener('click', e => {
  console.log("You clicked the blue button!");
})

blueButton.addEventListener('click', e => {
  responseBox.style.backgroundColor = "blue";
})

blueButton.addEventListener('click', e => {
  responseBox.innerText = "blue";
})

blueButton.addEventListener('onmouseover', e => {
  responseBox.innerText = "powderblue";
})

// function makeGreetingMessage(n1, n2){
//   n1 = "Alice";
//   n2 = "Bob";
//   if (name2 != null){
//     return 'Hello ' + n1 + ' and ' + n2;
//   } else {
//     return 'Hello ' + n1
//   }
// }
