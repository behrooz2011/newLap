const express = require('express');
const app = express();
const members = require('./Members');

const path = require('path');

const logger = (req, res, next)=>{
    console.log(`hi guyssss! ${req.protocol}, ${req.get('host')}, ${req.statusCode}, ${res.statusCode}`);
    console.log(JSON.stringify(req));
    next()
};
app.use(logger);

app.get('/api/members',(req,res)=>{
    res.json(members)
});


app.use(express.static(path.join(__dirname,'public')));

const PORT = process.env.PORT || 5000;
app.listen(PORT,()=>console.log(`Listening to the port ${PORT}`));