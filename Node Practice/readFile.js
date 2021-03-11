const fs = require('fs');
(async ()=>{
    // try{

    // const al = await fs.readFile('readdir.js','utf8');
    // console.log("Data frpm fs.readFile: ",al.length)
    
    // }catch(err){
    //     console.log(err)
    // }
    fs.readFile('readdir.js',(err,data)=>{
        if(err) throw err;
        console.log("this is the result :\n",data.length)
    })

})();


/////////////////////////////////////////////////////////////////