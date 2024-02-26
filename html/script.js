// function validateEmail(email) {
//     const regex =/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
//     return regex.test(email);
    
//   }
  
//   function validateForm() {
//     const uname=document.getElementById('uname').value;
//     if(uname!=""){
//     const emailInput = document.getElementById("emailid").value; 

//     if (validateEmail(emailInput)) {
      
//       if(checkpwd()==true)
//       {
//         alert('Account cereated successfully');
//         // // return false;
//         window.location.href('login.html');
//       }
//       else{
//         alert("Password should be same !!!");
//       }
     
//     } else {
//       alert("Please enter a valid email address!");
      
//     }

//     document.getElementById('input-box').reset();
//   }
// else{
//     alert('Enter username');
//     return true;
// }}

//   function checkpwd(){
//     var pwd1=document.getElementById('newpwd').value;
//     var pwd2=document.getElementById('re-enter-newpwd').value;
//     if(pwd1==pwd2)
//     {
//       return true;
//     }
//     return false;
//   }
