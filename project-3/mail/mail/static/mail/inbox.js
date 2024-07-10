document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  //joelkacode
  document.querySelector('#submitbutton').addEventListener('click', send_email); 

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails);
      
      //joelkacode

      emails.forEach(element => {
        
        const temp = document.createElement('div');
        temp.style.border='1px solid black';
        temp.style.width='300px';
        temp.style.height='100px';
        temp.style.padding='10px';
        temp.style.margin='5px';
        temp.style.paddingLeft='50px';
        temp.onmouseover=()=>{temp.style.border='3px solid black'}
        temp.onmouseleave=()=>{temp.style.border='1px solid black'}
        if (element.read){
          temp.style.backgroundColor='lightgrey';
        }
        else{
          temp.style.backgroundColor='white';
        }
        
        temp.innerHTML = `
        <strong>${element.sender}</strong>
        <br/>
        ${element.subject}
        <br/>
        ${element.timestamp}
        `;
        temp.addEventListener('click', function() {
            console.log('This element has been clicked!')

            //joelkacode {email ko dekhna hai}

            fetch(`/emails/${element.id}`)
            .then(response => response.json())
            .then(email => {
                // Print email
                console.log(email);

                fetch(`/emails/${email.id}`, {
                  method: 'PUT',
                  body: JSON.stringify({
                      read: true
                  })
                })

                let lala = document.createElement('div');
                lala.innerHTML = `

                  <strong>From: </strong> ${email.sender}
                  <br/>
                  <strong>To: </strong> ${email.recipients}
                  <br/>
                  <strong>Subject: </strong> ${email.subject}
                  <br/>
                  <strong>Timestamp: </strong> ${email.timestamp}
                  <hr/>
                  <br/>
                  <strong>Body: </strong>
                  <br/>
                  ${email.body}
                  <br/>
                `;

                const archivebutton=document.createElement('button');
                const replybutton=document.createElement('button');
                archivebutton.style.marginTop='50px'
                archivebutton.style.marginBottom='3px'
                lala.append(archivebutton);
                lala.append(document.createElement('br'));
                lala.append(replybutton);

                if (mailbox==='inbox'){archivebutton.innerHTML='Archive'}
                else if (mailbox==='archive'){archivebutton.innerHTML='Unarchive'}
                else{archivebutton.style.display='none'}

                if (mailbox==='inbox'){replybutton.innerHTML='Reply'}
                else{replybutton.style.display='none'}
                
                archivebutton.addEventListener('click',()=>{

                  if (mailbox==='inbox'){

                    fetch(`/emails/${email.id}`, {
                      method: 'PUT',
                      body: JSON.stringify({
                          archived: true
                      })
                    })
                    

                  }
                  if (mailbox==='archive'){

                    fetch(`/emails/${email.id}`, {
                      method: 'PUT',
                      body: JSON.stringify({
                          archived: false
                      })
                    })
                    

                  }

                  load_mailbox('inbox');

                });
              
                replybutton.addEventListener('click',()=>{
                  
                  document.querySelector('#emails-view').style.display = 'none';
                  document.querySelector('#compose-view').style.display = 'block';

                  // Clear out composition fields
                  document.querySelector('#compose-recipients').value = email.sender;
                  document.querySelector('#compose-subject').value = `Re: ${email.subject}`;
                  document.querySelector('#compose-body').value = ` On ${email.timestamp} ${email.sender} wrote: ${email.body}`;

                })
                
                
                document.querySelector('#emails-view').innerHTML = ``;
                document.querySelector('#emails-view').append(lala);


                // ... do something else with email ...
            });


        });
        document.querySelector('#emails-view').append(temp);
      

      });
      

      // ... do something else with emails ...
  });



}

//joelkacode
function send_email(event){

  event.preventDefault();

  let recipient=document.querySelector('#compose-recipients').value;
  let subject=document.querySelector('#compose-subject').value;
  let body=document.querySelector('#compose-body').value;

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipient,
        subject: subject,
        body: body
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
  });

  load_mailbox('sent');

}