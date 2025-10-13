const recipeFlowZone = document.querySelector(".recipe-flow-item");
const addRecipeflow = document.getElementById("add-recipe-flow-btn");

let count = 1;

function getNextStepNumber(){
    const currentSteps = document.querySelectorAll('.recipe-flow-group').length
    return currentSteps + 1;
}

function add_recipe_field(){
    const stepNumber = getNextStepNumber()
    const div = document.createElement('div');
    div.classList.add('recipe-flow-group');

    const num = document.createElement('p')
    num.classList.add('step-number');
    num.innerHTML = stepNumber;

    const newInput = document.createElement('textarea');
    newInput.name = 'recipe-flow[]';
    newInput.className = 'recipe-item';
    newInput.rows = '4';
    newInput.cols = '27';
    newInput.placeholder = 'レシピの手順を入力してください。'

    div.appendChild(num);
    div.appendChild(newInput);
    return div
}

addRecipeflow.addEventListener('click', () => {
    
    if (count > 30){return;}
    const new_input = add_recipe_field()
    recipeFlowZone.appendChild(new_input);
    count++;
})

document.addEventListener("DOMContentLoaded", () =>{
    const new_input = add_recipe_field();
    recipeFlowZone.appendChild(new_input);
    count++;
})