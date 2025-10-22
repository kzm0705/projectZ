
document.querySelector('form').addEventListener('submit', function(event){

    event.preventDefault();

    const recipeNameInput = document.getElementById('recipe_name');
    const recipeNameValue = recipeNameInput.value.trim() //入力値の前後の空白削除
    const fileInput = document.getElementById('file-input')
    const errors = []
    const max_length = 50;

    if(recipeNameValue.length === 0){
        errors.push('料理名は必須です')
    }
   
    else if(recipeNameValue.length > max_length){
        errors.push('料理名は${max_length}字以内で入力してください')
    }
    const file = fileInput.files[0];
    const allowTypes = ['image/jpeg', 'image/png', 'image/gif'];
    const maxFileSize = 5242880; // 5MB


    if(fileInput.files.length === ""){
        errors.push("画像を選択してください")
    }
//    MIMEタイプの確認
    else if(!allowTypes.includes(file.type)){
        errors.push('許可されていない画像形式です。JPG, PNG, GIFのみ対応しています');
    

    // ファイルサイズのチェック
    if (file.size > maxFileSize) {
        const maxSizeMB = maxFileSize / (1024 * 1024);
        errors.push(`ファイルサイズが大きすぎます。${maxFileSize}MB以下のファイルをアップしてください`)
        }
    }

    if (errors.length > 0){
        // エラーメッセージを改行でつなげてまとめて表示
        alert('【入力エラー】\n' + '・' + errors.join('\n'));
        recipeNameInput.focus(); // 最初の入力欄にカーソルを戻す
        return; // 処理を中断
    }
    
    event.target.submit();
});