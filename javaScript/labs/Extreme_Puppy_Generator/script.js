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

console.log(dataObject);

// need .firstButton because it's a class
let firstButton = document.querySelector('.firstButton');
let firsturl;
let img1;

firstButton.addEventListener('click', () => {
  firsturl = dataObject.data["0"].images.original.url;
  console.log(firsturl);
  img1 = document.createElement('img');
  img1.src = firsturl;
  console.log(img1);
  document.body.appendChild(img1);
})
