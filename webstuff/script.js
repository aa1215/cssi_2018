console.log('Hello World!');

const name = 'Akshara'
console.log('Hello' + ' ' + name + '!')
console.log(`Hello ${name}!`)

const age = 17
console.log('You are' + ' ' + age + ' years old.')
console.log(`You are ${age} years old.`)

const animal = 'corgi'
console.log('Your favorite animal is a ' + animal + '.')

//line comment
/* block comment */
/** documentation */

if (age >= 15){
  console.log('Yep, you are eligible for your driver\'s permit!');
} else {
  console.log('Try again when you\'re 15!');
}


// function time!
function makeGreet(name1, name2){
  if (name2 != null){
  return 'Hello ' + name1 + ' and you too ' + name2;
}
else{
  return 'Hello ' + name1;
}
}



function greet(name1, name2){
  if (name2 != null){
  console.log('Hello' + ' ' + name + ' and hello to you too ' + name2 + '.');
}
else{
  console.log('Hello' + ' ' + name + '.')
}
}

greet("Akshara");
greet("Akshara", "Cheddar")
makeGreet("Akshara")
makeGreet("Akshara", "Cheddar")

const multiplyBy3 = (x) => x ** 3;
console.log(multiplyBy3(2))

// setInterval(() => {
 // console.log(new Date());
// }, 1000);

//array names should be plural so people know when they see the variable it's an array
const names = ['Alice', 'Bob', 'Charlie', 'Dave']
for (let i = 0; i < 4; i++){
  console.log(names[i]);
}


let count = 0;
while(count < 5) {
  count ++;
  console.log(count);
}

for (x in names){
  console.log(names[x]);
}
names.forEach((name) => {
  console.log(`forEach: ${name}`);
});

//object literal
const article = {
  name: 'Dog family gives birth to litter of 10 puppies',
  views: 1234,
  datePublished: '03/05/2018',
  author: 'Akshara',
  dogAuthor: {
    name: 'Cheddar the Corgi',
    breed: 'corgi',
    title: 'Senior Canine Editor'
  }
}



article.name = 'Cheddar';
article['name'] = 'Jake';
article.dogAuthor.breed = 'corgi pup';

const pup = {
  pups: [{
    name: 'Tyrone',
    breed: 'terrier',
    sex: 'm',
  },
  {
    name: 'Pesto',
    breed: 'pug',
    sex: 'm',
  },
{
    name: 'Timothy',
    breed: 'corgi',
    sex: 'm',
  }],
}

document.addEventListener('DOMContentLoaded', () => {
  const floatingBox = document.querySelector('.floatingBox');
  let boxTop = 100;
  let boxLeft = 100;
document.addEventListener('keydown', (event) => {
  const key = event.key;
  //top left coordinate is (0,0)
  if (key == 'ArrowDown'){
    boxTop += 5;
  }
  else if (key == 'ArrowUp'){
    boxTop -= 5;
  }
  else if (key == 'ArrowRight'){
    boxLeft += 5;
  }
    else if (key == 'ArrowLeft'){
      boxLeft -= 5;
  } else {
    return;
  }

  floatingBox.style.top = boxTop + 'px';
  floatingBox.style.left = boxLeft + 'px';
  console.log(event);
});
});
