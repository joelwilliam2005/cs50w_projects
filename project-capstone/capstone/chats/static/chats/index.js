document.addEventListener('DOMContentLoaded', ()=>{

    const find_people_button=document.querySelector('#find_people');
    const my_contacts_button=document.querySelector('#my_contacts');

    const div_all_users=document.querySelector('#div_all_users');

    const contact_user_box=document.querySelector('#contact_user_box');
    const messaging_box=document.querySelector('#messaging_box');

    const index_div_2=document.querySelector('#index_div_2');
    const index_div_1=document.querySelector('#index_div_1');

    const welcome_text=document.createElement('text');

    const current_user=document.querySelector('#current_user').innerText;

    const back_button=document.querySelector('#back_button');

    let isSendMessageButtonSet = false;

    if(window.innerWidth<=600){
        index_div_1.style.display='block';
        index_div_2.style.display='none';

        back_button.addEventListener('click',()=>{
            index_div_1.style.display='block';
            index_div_2.style.display='none';

            all_user_cards=document.querySelectorAll('.user_card');

            reciever=document.querySelector('#contact_user_box_username').innerText;

            all_user_cards.forEach(element=>{
                element.style.backgroundColor='white';
                element.style.color='black';
                clearInterval(current_interval);
            })

        })

    }

    welcome_text.innerText='Click on a contact to start a CHAT.';

    contact_user_box.style.display='none';
    messaging_box.style.display='none';

    index_div_2.append(welcome_text);

    my_contacts_button.style.backgroundColor='white';
    my_contacts_button.style.color='black';

    find_people_button.style.backgroundColor='white';
    find_people_button.style.color='black';

    find_people_button.addEventListener('mouseover',()=>{
        if (find_people_button.style.backgroundColor!='black'){
            find_people_button.style.backgroundColor='#ededed';
        }
    })
    find_people_button.addEventListener('mouseout',()=>{
        if (find_people_button.style.backgroundColor!='black'){
            find_people_button.style.backgroundColor='white';
        }
    })

    my_contacts_button.addEventListener('mouseover',()=>{
        if (my_contacts_button.style.backgroundColor!='black'){
            my_contacts_button.style.backgroundColor='#ededed';
        }
    })
    my_contacts_button.addEventListener('mouseout',()=>{
        if (my_contacts_button.style.backgroundColor!='black'){
            my_contacts_button.style.backgroundColor='white';
        }
    })

    my_contacts_button.addEventListener('click',()=>{

        fetch('api/return_all_contacts')
        .then(response => response.json())
        .then(data => {

            div_all_users.innerText=``;

            console.log(data)

            let all_users=data;

            all_users.forEach(userElement => {

                if (userElement.username!='chats_admin_user' &&  userElement.username!=document.querySelector('#current_user').innerText){
                    user_card=document.createElement('div')
                    user_card.className+='user_card'
                    user_card.append(`${userElement.first_name} ${userElement.last_name} (${userElement.username})`);

                    div_all_users.append(user_card);

                    my_contacts_button.style.backgroundColor='black';
                    my_contacts_button.style.color='white';
                
                    find_people_button.style.backgroundColor='white';
                    find_people_button.style.color='black';

                    user_card_hover(user_card);

                    user_card.addEventListener('click', ()=>{

                        if(window.innerWidth<=600){
                            index_div_1.style.display='none';
                            index_div_2.style.display='block';

                            current_interval=setInterval(()=>{
                    
                                fetch(`api/get_conversation?contact_user=${reciever}`,{
                                    method: 'GET',
                                    headers: { 'Content-Type':'application/json'},
                                })
                                .then(response=>response.json())
                                .then(conversation=>{
                                    load_conversation_in_message_box(conversation, current_user, userElement.username);
                                    console.log('Conversation fetched')
                                })
                        
                        
                            }, 1000);

                        }



                        fetch(`api/get_conversation?contact_user=${userElement.username}`,{
                            method: 'GET',
                            headers: { 'Content-Type':'application/json'},
                        })
                        .then(response=>response.json())
                        .then(conversation=>{
                            console.log(conversation)
                            load_conversation_in_message_box(conversation, sender=current_user, reciever=userElement.username);
                        })

                        welcome_text.style.display='none';
                        contact_user_box.style.display='block';
                        messaging_box.style.display='block';
                        document.querySelector('#contact_user_box_only_fullname').innerText=`${userElement.first_name} ${userElement.last_name}`;
                        document.querySelector('#contact_user_box_only_username').innerText=`${userElement.username}`;

                        send_message_button=document.querySelector('#send_message');
                        send_message_button_hover(send_message_button)

                        if (!isSendMessageButtonSet) {
                            send_message_button_on_click_functionality(send_message_button);
                            isSendMessageButtonSet = true;
                        }

                        user_card_selected(sender=current_user);
                        
                    })

                }
                
            });
        })

    })

    find_people_button.addEventListener('click',()=>{
        fetch('api/return_all_users')
        .then(response=>response.json())
        .then(data=>{

            div_all_users.innerText=``;

            console.log(data)

            let all_users=data;

            fetch('api/return_all_contacts')
            .then(response => response.json())
            .then(contactsData=>{

                let users_in_contacts = contactsData.map(contact => contact.username);

                console.log(users_in_contacts);

                all_users.forEach(userElement => {
                    if (userElement.username!='chats_admin_user' &&  userElement.username!=document.querySelector('#current_user').innerText){
                        user_card=document.createElement('div')
                        user_card.className+='user_card'
                        user_card.append(`${userElement.first_name} ${userElement.last_name} (${userElement.username})`);
                        add_to_contact_button=document.createElement('button')
                        add_to_contact_button.className+='add_to_contact_button';

                        if (users_in_contacts.includes(userElement.username)){
                            add_to_contact_button.innerText='✓';
                            console.log(userElement);
                        }
                        else{
                            add_to_contact_button.innerText='ADD';
                            
                        }
                        add_to_contact_button.value=userElement.username;
                        user_card.append(add_to_contact_button);
    
                        div_all_users.append(user_card);
    
                        my_contacts_button.style.backgroundColor='white';
                        my_contacts_button.style.color='black';
                    
                        find_people_button.style.backgroundColor='black';
                        find_people_button.style.color='white';
    
                        user_card_hover(user_card);
                        add_to_contact_button_hover(add_to_contact_button);
                        
                    }
                    
                });

                                //Add to contact button functionality

                let add_to_contact_button_all=document.querySelectorAll('.add_to_contact_button');

                add_to_contact_button_all.forEach(button=>{
                    button.addEventListener('click',()=>{
                        if(add_to_contact_button.innerText!='✓'){
                            fetch('api/add_contact',{

                                method: 'POST',
                                headers: { 'Content-Type':'application/json'},
                                body: JSON.stringify({contact_user:button.value})
        
                            })
                            .then(response => response.json())
                            .then(data => {
                                if (data.success){
                                    button.innerText='✓';
                                    button.style.backgroundColor='white';
                                    button.style.color='black';
                                }
                                else{
                                    button.innerText='Error!';
                                }
                            })
                        }

                    })
                })

            })


        })

        

    })
    
});

function user_card_hover(user_card){
    user_card.addEventListener('mouseover',()=>{
        if (user_card.style.backgroundColor!='black'){
            user_card.style.backgroundColor='#ededed';
        }
    })
    user_card.addEventListener('mouseout',()=>{
        if (user_card.style.backgroundColor!='black'){
            user_card.style.backgroundColor='white';
        }
    })
}

function add_to_contact_button_hover(add_to_contact_button){
    add_to_contact_button.addEventListener('mouseover',()=>{
        if (add_to_contact_button.innerText!='✓'){
            add_to_contact_button.style.backgroundColor='black';
            add_to_contact_button.style.color='white';
        }
    })
    add_to_contact_button.addEventListener('mouseout',()=>{
        if (add_to_contact_button.innerText!='✓'){
            add_to_contact_button.style.backgroundColor='white';
            add_to_contact_button.style.color='black';
        }
    })
}

function send_message_button_hover(send_message_button){

    send_message_button.addEventListener('mouseover',()=>{

        send_message_button.style.backgroundColor='black';
        send_message_button.style.color='white';

    })
    send_message_button.addEventListener('mouseout',()=>{

        send_message_button.style.backgroundColor='white';
        send_message_button.style.color='black';

    })

}

function send_message_button_on_click_functionality(send_message_button){

    let isSendMessageButtonSet = false;
    reciever=document.querySelector('#contact_user_box_only_username').innerText;

    send_message_button.removeEventListener('click',send_message_handler);

    function send_message_handler(){
        textarea=document.querySelector('#typing_area');
        messaging_box_messages_area=document.querySelector('#messaging_box_messages_area');
        
        if (!textarea.value.trim() || textarea.value==''){
            return
        }

        fetch('api/send_message',{
                method:'POST',
                headers:{'Content-Type':'application/json'},
                body: JSON.stringify({
                    message_content:textarea.value, 
                    message_sent_to: document.querySelector('#contact_user_box_only_username').innerText
                })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success){
                console.log(`[${textarea.value}] sent to [${reciever}]`);

                //message_div_build_and_append
                message_div=document.createElement('div');
                message_div.id='message_div';
                message_div.className+='sent_message_div';

                messaging_box_messages_area.append(message_div);

                content=document.createElement('div')
                content.innerText=textarea.value
                content.id='message_text_div';

                message_div.append(content)

                time=document.createElement('div');
                time.id='time';
                time.innerText=data.timestamp;

                message_div.append(time);

                textarea.value='';

            }
            else{
                alert('Message not sent.');
            }
        })
    }
    send_message_button.addEventListener('click',send_message_handler);
}

function load_conversation_in_message_box(conversation, sender, reciever){
    
    messaging_box_messages_area=document.querySelector('#messaging_box_messages_area');
    messaging_box_messages_area.innerText='';

    conversation.forEach(message => {

        //message_div_build_and_append
        message_div=document.createElement('div');
        message_div.id='message_div';

        if (message.sender==sender){
            message_div.className+='sent_message_div';
        }
        else if (message.sender==reciever){
            message_div.className+='recieved_message_div';
        }
        
        messaging_box_messages_area.append(message_div);

        content=document.createElement('div')
        content.innerText=message.content
        content.id='message_text_div';

        message_div.append(content)

        time=document.createElement('div');
        time.id='time';
        time.innerText=message.time;

        message_div.append(time);

    });

}


let current_interval;
function user_card_selected(sender){

    all_user_cards=document.querySelectorAll('.user_card');

    reciever=document.querySelector('#contact_user_box_username').innerText;

    all_user_cards.forEach(element=>{

        if (element.innerText==reciever){

            element.style.backgroundColor='black';
            element.style.color='white';


            clearInterval(current_interval);

            if(element.style.backgroundColor=='black'){
                current_interval=setInterval(()=>{
                    
                    fetch(`api/get_conversation?contact_user=${reciever}`,{
                        method: 'GET',
                        headers: { 'Content-Type':'application/json'},
                    })
                    .then(response=>response.json())
                    .then(conversation=>{
                        load_conversation_in_message_box(conversation, sender, reciever);
                        console.log('Conversation fetched')
                    })
            
            
                }, 1000);
            }

        }
        else{

            element.style.backgroundColor='white';
            element.style.color='black';

        }

    })

}

