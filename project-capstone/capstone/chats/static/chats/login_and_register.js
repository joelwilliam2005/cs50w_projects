document.addEventListener('DOMContentLoaded', ()=>{

    login_view=document.querySelector('#login_div')
    register_view=document.querySelector('#register_div')

    login_view.style.display='none';
    register_view.style.display='block';

    register_view_height=getComputedStyle(register_view).height;

    let login_and_register_div=document.querySelector('#login_and_register_div');
    let login_and_register_div_height=getComputedStyle(login_and_register_div).height;
    
    login_and_register_switch_button=document.querySelectorAll('#login_and_register_switch_button');

    login_and_register_switch_button.forEach(button => {
        button.addEventListener('click',()=>{

            if (button.innerText==='Login Here'){
                login_view.style.display='block';
                register_view.style.display='none';
                login_view.style.height=register_view_height
                login_and_register_div.style.height=login_and_register_div_height
            }
    
            else{
                login_view.style.display='none';
                register_view.style.display='block';
            }
    
        });
    });

});