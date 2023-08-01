function showPage(page){
    document.querySelectorAll('.doc').forEach(div =>{
        div.style.display= 'none';
    })
    document.querySelector(`#${page}`).style.display = 'block';

}
document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('button').forEach(button =>{
        button.onclick=function(){
            showPage(this.dataset.page);
        }
    });
});
   

function showSection(){
    fetch(`/section/${section}`)
    .then (response => response.text())
    .then(text =>{
        console.log (text);
        document.querySelector('#content').innerHTML = text;
    });
}
   




var persons = [
    {name: "alex", age: 22},
    {name: "maria", age:30},


]
for (var i =0; 1<= persons.length; i++){
    console.log (persons[i].name)
}