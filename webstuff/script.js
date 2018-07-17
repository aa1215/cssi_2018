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
