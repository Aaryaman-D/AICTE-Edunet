// synchronous to asynchronus js
//1.call back=not very much used recently
//-code complications so other methods==

//2.promises--dummy object creation
//
//async and awaited



//ARROW FUNCTION : anonymus function/ FAT Arrow Function
const sum_one =(a,b) =>{
    return a+b
}
console.log(sum_one(5,5))
//
const sumone=(a,b) => a+b
console.log(sumone(5,5))





function isEven(num){
    let promise= new Promise((resolve,reject)=>{
        setTimeout(()=>{
            if(num%2==0){
                resolve(`${num} is even`)
            }else{
            reject(`${num} is odd`)
            
        }
        },2000);
    });
    return promise
}
isEven(46).then(()=>{
    console.log("Number is Even");
}).catch(()=>{
    console.log("Number id odd"); 
})












function orderPizza(pizza){
    console.log(`${pizza} pizza please`);
    preparePizza(pizza)
    
}
function preparePizza(pizza){
    console.log(`Preparing ${pizza} pizza please`)
    servePizza(pizza)
}
function servePizza(pizza){
    console.log(`Serve ${pizza} pizza please`);   
}
// orderPizza("Veg")