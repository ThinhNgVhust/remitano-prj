const regExp =/^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
document.addEventListener("DOMContentLoaded",()=>{
    buttonShareLink = document.querySelector("#btnShareLink");
    buttonShareLink.addEventListener("click",()=>{
        url = document.querySelector("#youtubeLink").value;
        match = url.match(regExp);
        if (match && match[2].length == 11) {
            linkId = match[2];
            //Call backend to insert 
            const body = {"link":linkId}
            fetch( "/insert",
                { method:"POST",
                  body:JSON.stringify(body)
                }
                )
                .then(respone=>respone.json())
                .then(data =>{
                  mess = data["message"];
                  console.log(mess);
                  title = data["title"];
                  description = data["description"];
                  creator_mail = data["creator"];
                  linkId = data["linkId"];
                  appendElement(title,description.creator_mail,linkId);
                  document.querySelector("#youtubeLink").value ="";
                  return false;
                })
                .finally(()=>$("#shareMovie").modal('hide'));
            
          } else {
            alert("Must be a youtube link");
          }
    })
})
function appendElement(title,description,creator_mail,linkId){
  parent = document.querySelector("#container");
  content = document.createElement("div");
  content.classList.add("media");
  content.innerHTML =`<br>
  <iframe width="420" height="315" src="https://www.youtube.com/embed/${linkId}">
  </iframe>   
  <div class="media-body">
      <div ><b>${title}</b></div>
      <div>Share by <b>${creator_mail}</b> </div>
      <div>Description:</div>
      <div><b>${description}</b></div>
  </div>`;
  parent.prepend(content);
}