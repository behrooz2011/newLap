/*Events in Node.js
Every action on a computer is an event. Like when a connection is made or a file is opened.

Objects in Node.js can fire events, like the readStream object fires events when
 opening and closing a file: */

 var fs = require('fs');

var readStream = fs.createReadStream('./demo.txt');

/*Write to the console when the file is opened:*/
readStream.on('open', function () {
  console.log('The file is open');
});

//#######################################################################################
//######################## Events
//########################################################################################

/* Node.js has a built-in module, called "Events", where you can create-, fire-,
 and listen for- your own events.
To include the built-in Events module use the require() method. 
In addition, all event properties and methods are an instance of an EventEmitter object. 
To be able to access these properties and methods, create an EventEmitter object: */


// 
// The EventEmitter Object
/* You can assign event handlers to your own events with the EventEmitter object.
In the example below we have created a function that will be executed when a "scream" event is fired.
To fire an event, use the emit() method. */

var events = require('events');
var eventEmitter = new events.EventEmitter();

//Create an event handler:
var myEventHandler = function () {
  console.log('I hear a melody!');
}

//Assign the eventhandler to an event://listening = On
eventEmitter.on('melody', myEventHandler);

//Fire the 'scream' event:
eventEmitter.emit('melody');

// How to count the number of visiters with this mechanism ??
//Step 5 — Managing Events Listeners

/*Event emitters come with some mechanisms 
to monitor and control how many listeners are subscribed to an event. To get an overview of 
how many listeners are processing an event, we can use the listenerCount() method that’s included 
in every object.

The listenerCount() method accepts one argument: 
the event name you want the count for. Let’s see it in action in index.js. */

// function getEnvLocale(env) {
//     env = env || process.env;

//     return env.LC_ALL || env.LC_MESSAGES || env.LANG || env.LANGUAGE;
// }
// console.log(getEnvLocale());


const osLocale = require('os-locale');
 
(async () => {
    console.log(await osLocale());
    //=> 'en-US'
})();