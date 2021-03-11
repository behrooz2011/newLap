// const fs = require('fs').promises;
// async function listFile(){
//     try{
//         console.log("hii");
//         const files = await fs.readdir('C:/Resume');
//         for (const file of files){
//             console.log(file)
//         }

//     }
//     catch(err){
//         console.log("Error here: ",err)
//     }
// }
// listFile()

////////////////////////////////////////////////////////////////////////
// async function listFile(){
//     try{
//         console.log("hii");
//         var dir = '.';
//         if (process.env[2]){
//             console.log("this is process.env[1] :",process.env[2]);
//             dir=process.env[2];
//         }
//         ;
//         const files = await fs.readdir(dir);
//         for (const file of files){
//             console.log(file)
//         }

//     }
//     catch(err){
//         console.log("Error here: ",err)
//     }
// }
// listFile()
///////////////////////////////////////////////////////////////////////////////
const fs = require('fs');
const fs_reader = dir =>{
    return new Promise((resolve,reject)=>{
        fs.readdir(dir,(err,fileList)=>{
           
            if(err) reject(err);
            else{ console.log("prmise!");
            resolve(fileList)
        } 
        });
    });
};

async function listFiles(){
    try{
        let dir ='.';
        const files = await fs_reader(dir);
        console.log("started!");
        for (let fn of files){
            console.log(fn);
        }
    }catch(err){
        console.log(err)
    }
}
listFiles();