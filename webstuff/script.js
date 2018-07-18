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
