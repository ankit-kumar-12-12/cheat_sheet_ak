const express = require("express")

const app=express()

// function isOldEnough(age){
//   if(age>=18){
//     return true
//   }else{
//     return false
//   }
// }

function isOldEnoughMiddleware(req,res,next){
  const age=req.query.age
  if(age>=18){
    next()
  }else{
    res.json({
        msg:"Big no"
      })  
  }
}

app.use(isOldEnoughMiddleware) //no need to mention explicity in ever function call all below it will use this middle ware
app.get("/ride1",function(req,res){
  
    res.json({
      msg:"ok you can ride"
    })
  
})

//app.get("/ride2",isOldEnoughMiddleware,function(req,res){
app.get("/ride2",function(req,res){
  
    res.json({
      msg:"ok you can ride2"
    })
  
})


app.listen(3000,function(){

  console.log("app is listening on port 3000")
})