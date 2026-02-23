let student_info={
    name : "Aaryaman",
    email :"aaryaman@gmailcom"
}
let studentsList=[
    {name:"aaryaman",email:"aaryamandiwate2329@gmail.com",age:20},
    {name:"aaryn",email:"aaryndiwate2329@gmail.com",age:22},
    {name:"rhutika",email:"rhukmini@gmail.com",age:29},
    {name:"aa",email:"aa@gmail.com",age:10}
]
// // console.log(studentsList[1].email);
// for(let i=1;i<4;i++){
//     console.log("My name is "+studentsList[i].name+"my email is"+studentsList[i].email+"and age is "+studentsList[i].age); 
// }

studentsList.forEach(function(student){
     console.log("My name is ",student.name,"my email is ",student.email,"and age is ",student.age)
})