from flask_sqlalchemy import SQLAlchemy

from db import db, Ingredients_temp

def create_ingredient_recipe_query(id, ingre_array):
    Ingredients_temp.query.filter_by(recipe_id=id).delete()
    db.session.commit()

    ingredients = ingre_array.get('ingredient', [])
    amounts = ingre_array.get('amount-ingredient', [])
    for ingredient_name, amount in zip(ingredients, amounts):
        if ingredient_name.strip() and amount.strip():
            insert_ingredient_query = Ingredients_temp(
                recipe_id = id,
                ingredient_name = ingredient_name,
                amount = amount
            )
            db.session.add(insert_ingredient_query)

        else:print('食材か分量のどっちかが空欄でした。')

    db.session.commit()
