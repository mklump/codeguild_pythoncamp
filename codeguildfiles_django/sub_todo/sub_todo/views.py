from django.http import HttpResponse
from django.shortcuts import render
from . import logic

def render_index(request):
    lists = logic.get_all_lists()
    list_to_items = logic.create_dict_of_list_and_sub_items()

    template_args = {
        'lists': lists,
        'list_to_items': list_to_items,
    }
    return render(request, 'sub_todo/index.html', template_args)

def render_add_list(request):
    return render(request, 'sub_todo/add_list_form.html', {})

def render_add_list_ack(request):
    new_list = request.POST['name']

    logic.create_new_list(new_list)

    template_args = {
        'new_list': new_list,
    }
    return render(request, 'sub_todo/list_ack.html', template_args)

def render_list_add_item(request, list_id):
    indv_list = logic.get_list_by_id(list_id)

    template_args = {
        'indv_list': indv_list,
    }
    return render(request, 'sub_todo/add_item_form.html', template_args)

def render_add_item_ack(request, list_id):
    item = request.POST['item']
    indv_list = logic.get_list_by_id(list_id)
    logic.create_new_item_for_list(item, indv_list)

    template_args = {
        'item': item,
        'indv_list': indv_list,
    }
    return render(request, 'sub_todo/item_ack.html', template_args)

def render_delete_sub_item(request, list_id, item_id):
    logic.delete_sub_item(item_id)
    logic.delete_top_level_list(list_id)
    return render(request, 'sub_todo/index.html', {})
