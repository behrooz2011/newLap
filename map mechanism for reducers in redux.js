console.log('Hello, world!');
let data = [
      {id:1,name:'doo',last:'ss',q:3},
      {id:2,name:'ttt',last:'tttss',q:6},
      {id:3,name:'iiidoo',last:'iiiss', q:5},
      {id:4,name:'ioo',last:'jjs', q:2},
  ];
let added = {id:3,name:'add',last:'ezafeh', q:50};
let mapData = data.map(item=>{
            if(item.id==added.id){
              item.q-=1
            }
        return item
          });

console.log(mapData)