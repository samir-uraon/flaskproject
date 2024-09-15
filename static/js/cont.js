let name="Hope you intrastated to visited my portfolio.";
let index =1;
 let a=0;
let type=()=>{

if(index>name.length){
index=1;
}
// if(a<15 && index<=name.length){
else{
console.log("a")
let new_text=name.slice(0,index)

document.querySelector("h3").innerHTML=new_text;
index++;
a++;
setTimeout(()=>type(),100)
}
}
setTimeout(()=>{type()},3000)

setTimeout(() => {
  document.querySelector("#icon").style.opacity=1
  
  document.querySelector("#icon").style.transform="scale(1) translateY(78px)"
  
},9000);
setTimeout(() => {
  document.querySelector(".content").style.opacity=1
  
  document.querySelector(".content").style.transform="scale(1) translateY(0px)"
  
},11000);
