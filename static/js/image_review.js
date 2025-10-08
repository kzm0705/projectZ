const file_input = document.getElementById('file-input');
const preview = document.getElementById('preview');

file_input.addEventListener('change' , function(event){
    const file = event.target.files[0];

    if(file){
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = function(e){
            const imageUrl = e.target.result;

            preview.src = imageUrl;
            preview.style.display = 'block';
            console.log(imageUrl);
        }
    }else{
        preview.src = '#';
        preview.style.display = 'none';
        console.log('no file selected');
    }
})