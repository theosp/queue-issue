// Listener.js
//
// Original Developer: Daniel Chcouri <333222@gmail.com>
//
// Dependencies:
// $ npm install cli-color

var http = require('http'),
    url = require('url'),
    clc = require('cli-color');

var module_c = clc.magenta,
    message_c = clc.blue,
    date_c = clc.white,
    property_c = clc.green,
    value_c = clc.yellow;

//var no_color = function (s) {return s;}
//    module_c = no_color,
//    message_c = no_color,
//    date_c = no_color,
//    property_c = no_color,
//    value_c = no_color;

var messages_count = 0;

var dateStamp = function () {
    var now = new Date();
    return now.getUTCFullYear() + "-" + now.getUTCMonth() + "-" + now.getUTCDate() + " " + now.getUTCHours() + ":" + now.getUTCMinutes() + ":" + now.getUTCSeconds();
};

http.createServer(function (req, res) {
    messages_count += 1;

    var parsed_url = url.parse(req.url, true);
    var path = parsed_url.pathname.split("/");

    var module, message;
    if (path.length > 2) {
        module = path[1];
        message = module_c("[" + module + "] ") + message_c(path.slice(2).join("/"));
    }
    else {
        module = "";
        message = message_c(path[1]);
    }

    var params = [];
    for (var param in parsed_url.query) {
        if (parsed_url.query.hasOwnProperty(param)) {
            params.push(property_c(param + ": ") + value_c(parsed_url.query[param]));
        }
    }

    message += " " + params.join(", ");

    console.log(date_c(messages_count + " " + dateStamp()) + " " + message);
    
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end("");
}).listen(81, "theosp.no-ip.org");
