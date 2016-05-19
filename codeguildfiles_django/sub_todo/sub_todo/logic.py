from . import models

def create_new_list(name):
    new_list = models.List(name=name)
    new_list.save()

def create_new_item_for_list(item, parent_list):
    new_list_item = models.ListItem(
        item=item,
        parent_list=parent_list,
    )
    new_list_item.save()

def get_all_lists():
    return models.List.objects.all()

def get_list_by_id(id):
    return models.List.objects.get(id=id)

def get_item_by_id(id):
    return models.ListItem.objects.get(id=id)

def get_all_items_for_list(parent_list):
    print(parent_list)
    return models.ListItem.objects.filter(parent_list=parent_list)

def create_dict_of_list_and_sub_items():
    new_dict = {}
    list_of_objects = get_all_lists()

    for obj in list_of_objects:
        new_dict[obj] = get_all_items_for_list(obj)

    return new_dict

def delete_sub_item(id):
    sub_item = get_item_by_id(id)
    sub_item.delete()

def delete_top_level_list(list_id):
    parent_list = get_list_by_id(list_id)
    if len(get_all_items_for_list(parent_list)) == 0:
        parent_list.delete()
