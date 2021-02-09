const express = require('express');
const app = express();
app.get('/',(req,res)=>{
    res.send("hello wwwworld")
});

app.get('/api/course',(req,res)=>{
  res.send([1,2,3])  
})
console.log("before");
hh("bozi",(user)=>console.log(user));

function hh(x,cb){
    setTimeout(()=>{
        console.log("hello!",x);
        cb({x:x,girhubb:"soli"})
},2000);
}
console.log("after");
//once we have the user objects,we want the repo
//it takes time to get the user objects from the server
//setTimeout simulates a real life situation
// getUser("Joe",repo())
// function getUser(user,cb){
//     setTimeout(()=>{
//         console.log("User is :",user);
//         cb({})
// },5000)
// };

function repo(username,cb){
    setTimeout(()=>{
        console.log("connecting to the server...");
        cb(['repo1','repo2'])
    }),7000
    
}
repo("hi",(x)=>console.log(x))


app.listen(3005,()=>console.log("listening to port 3005.."));