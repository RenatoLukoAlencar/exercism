/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */
export function cookingStatus(timer=-1){
    let res = "You forgot to set the timer."
    
    if(timer>=0) res = (timer == 0 )?"Lasagna is done.": "Not done, please wait."
    
    return res
}


export function preparationTime(layers, prepTime=2){
    return prepTime * layers.length
}

export function quantities(layers=[]){
    const res = {
        noodles: 0, 
        sauce: 0.0
    }

    layers.forEach((item)=> {
        if(item == "noodles"){
            res.noodles += 50
        }else if(item == "sauce"){
            res.sauce += 0.2
        }
    })
    return res
}

export function addSecretIngredient(firstList, secondList ){
    secondList.push(firstList[firstList.length-1])
}

export function scaleRecipe(recipe, portions=2){
    if(portions == 2) return recipe
    const newRecipe={}

    Object.keys(recipe).forEach(elem=> {
        newRecipe[elem] = (recipe[elem] / 2) * portions
    })

    return newRecipe
}


