const express =require("express");
const redis = require("redis");

const app = express();
const client = redis.createClient({
    host: "redis-server",  //name specified in the docker-compose.yml
   
    //what about port? -> maybe default
    port: 6379
});
client.set("visits",0); //just to initialize the number of visits to be zero

app.get('/',(req,res)=>{
    //process.exit(0);
    //process.exit(5);
    client.get('visits',(err,visits)=>{
        res.send("Number of visits is "+visits);
        client.set('visits',parseInt(visits)+1);
    });
})
app.listen(8081,()=>{
    console.log("Listening on port 8081");
})



