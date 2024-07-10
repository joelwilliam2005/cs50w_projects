document.addEventListener('DOMContentLoaded',()=>{
    document.querySelectorAll('.editPost').forEach(function(button){
        button.addEventListener('click',()=>{
            if (button.innerHTML==='Edit'){
                console.log(button.value)
                textArea=document.createElement('textarea');
                textArea.style.height='30px';
                textArea.style.width='100%';
                textArea.value=document.querySelector(`#content${button.value}`).innerHTML
                document.querySelector(`#content${button.value}`).innerHTML='';
                button.innerHTML='Save';
                document.querySelector(`#content${button.value}`).append(textArea)

                
            }
            else{
                // button.innerHTML='Edit';
                // document.querySelector(`#content${button.value}`).append(textArea.value)
                // textArea.remove()
                // console.log(document.querySelector(`#content${button.value}`))
                contentInTextArea=textArea.value
                fetch(`/savePost/${button.value}/`,{
                    method: 'POST',
                    headers: {'Content-Type':'application/json'},
                    body: JSON.stringify({content: contentInTextArea})
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success){
                        button.innerHTML='Edit';
                        document.querySelector(`#content${button.value}`).append(textArea.value)
                        textArea.remove()
                        console.log(document.querySelector(`#content${button.value}`))
                    }
                    else {
                        alert('Error saving post');
                    }
                })
            }
        });
    });

    document.querySelectorAll('.likePost').forEach(function(button){
        button.addEventListener('click', ()=>{

            likesValueInHTML=parseInt(document.querySelector(`#likes${button.value}`).innerHTML)

            if (button.innerHTML=='Like'){

                fetch(`/likePost/${button.value}/`,{
                    method: 'POST',
                    headers: {'Content-Type':'application/json'},
                    body: JSON.stringify({content: 'Like'})
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success){
                        button.innerHTML='Unlike';
                        likesValueInHTML+=1;
                        document.querySelector(`#likes${button.value}`).innerHTML=likesValueInHTML
                    }
                    else {
                        alert('Error liking post');
                    }
    
                })
            }
            else {

                fetch(`/likePost/${button.value}/`,{
                    method: 'POST',
                    headers: {'Content-Type':'application/json'},
                    body: JSON.stringify({content: 'Unlike'})
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success){
                        button.innerHTML='Like';
                        likesValueInHTML-=1;
                        document.querySelector(`#likes${button.value}`).innerHTML=likesValueInHTML
                    }
                    else {
                        alert('Error unliking post');
                    }
    
                })

            }
            
        })
    });
});
