const ingredientsZone = document.querySelector('.ingredients-input');
const addIngredientBtn = document.getElementById('add-ingredient-btn');
const deleteIngredientBtn = document.getElementById('delete-ingredient-btn');

let ingredientCount = 0;

// 食材入力欄と量を追加する関数
function addIngredientField(){
    ingredientCount++;

    const div = document.createElement('div');
    div.classList.add('ingredient-input-group');

    const newIngredientInput = document.createElement('input');
    newIngredientInput.type = 'text';
    newIngredientInput.name = 'ingredient[]';
    newIngredientInput.id =  'ingredient' + ingredientCount;
    newIngredientInput.placeholder = '使う食材を入力してね'

    const amountIngredientInput = document.createElement('input');
    amountIngredientInput.type = 'text';
    amountIngredientInput.name = 'amount-ingredient[]';
    amountIngredientInput.id = 'amount-ingredient' + ingredientCount;
    amountIngredientInput.size = '10';
    amountIngredientInput.placeholder ='どれくらい必要？'

    div.appendChild(newIngredientInput);
    div.appendChild(amountIngredientInput);
    return div;
}

document.addEventListener('DOMContentLoaded', () =>{
    // デフォルトで三つの食材入力値と量を追加
    const label = ingredientsZone.querySelector('label');

    for( let i=1; i < 4; i++){
        const new_input = addIngredientField();

        ingredientsZone.appendChild(new_input);
    }
})

// 食材追加ボタンが押されたときの処理
addIngredientBtn.addEventListener('click', () =>{
    if (ingredientCount >= 30){return;}
    const new_input = addIngredientField();
    ingredientsZone.appendChild(new_input);})

// 食材削除ボタンが押されたと気の処理

deleteIngredientBtn.addEventListener('click', () =>{
    if (ingredientCount > 1){
        const lastInput = document.getElementById('ingredient' + ingredientCount);
        const lastAmountInput = document.getElementById('amount-ingredient' + ingredientCount);
        lastInput.remove();
        lastAmountInput.remove();
        ingredientCount--;
        console.log(ingredientCount);
    }
})


