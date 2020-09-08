var el = document.getElementById("aa");
el.textContent="Hi blue moon"

var msg = '<p><h1>lorem ipsun</h1></p>';
msg +='<p> <h2> lorem ipsun</h2> </p>';
msg += '<p>Window height:' + window.innerHeight+'</p>'
var em = document.getElementById("bb");
em.innerHTML= msg;

var newmsg ='Window Width: '+ window.innerWidth;
fire();
function fire(){
    return document.getElementById('cc').innerHTML='Window Width: '+ window.innerWidth;
};
window.addEventListener('resize',function fire(){
    document.getElementById("cc").innerHTML=newmsg
});

// window.onresize = () => { msg = window.innerHeight } 
// look at this link:
//https://codepen.io/jondlm/pen/doijJ