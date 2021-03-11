console.log('Hello, world!')
let obj1 = { "foo": 'baruuu', x: 42 };
let obj2 = { y: 13,z:1000 };
let obj3 ={j:66}

let cl = { ...obj1 };
// Object { foo: "bar", x: 42 }

console.log(cl);
let merj = { ...obj1, ...obj2 };
console.log(merj)
console.log({ ...obj1,obj2 })
console.log({ ...obj1,quantity:99})