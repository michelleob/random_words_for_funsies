var http = require('http');
var server = http.Server(app);

app.set('view engine', 'ejs');


app.get('/', function(req,res){

	res.render('index');
});

server.listen(8000, function(){
	console.log('listening on 8000');
});

