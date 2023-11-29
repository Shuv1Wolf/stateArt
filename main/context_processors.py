from .models import Main_menu_Model

def list_view_processor(request):
    list_objects = Main_menu_Model.objects.all()
    return {'list_objects': list_objects}
