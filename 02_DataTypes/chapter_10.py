chai_order = dict(type='Chai', size='Large', sugar='No', milk='Yes',)
print(f"Chai Order: {chai_order}")

chai_recipe ={}
chai_recipe["base"] = "Black Tea Leaves"
chai_recipe["liquid"] = "milk"

print(f"Chai Recipe: {chai_recipe['base']}")
del chai_recipe["liquid"]
print(f"Chai Recipe: {chai_recipe}")

print(f"is sugar in the order?{'sugar' in chai_order}")

chai_order = dict(type='Chai', size='Large', sugar='1', milk='Yes',)

#print(f"Order detials(keys):{chai_order.keys()}")
#print(f"Order detials(values):{chai_order.values()}")
#print(f"Order detials(items):{chai_order.items()}")

last_item = chai_order.popitem()
print(f"Last item removed from the order: {last_item}")

chai_order.update({'sugar': '2'})
print(f"Updated Chai Order: {chai_order}")