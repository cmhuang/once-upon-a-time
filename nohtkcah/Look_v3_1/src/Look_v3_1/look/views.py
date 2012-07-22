# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.files.base import ContentFile
from django.template import RequestContext
from django.conf import settings
from cStringIO import StringIO
from PIL import Image
from Look_v3_1.look.models import Look, LookUploadForm, Item, ItemForm

def detail(request, look_id):
    look = get_object_or_404(Look, pk=look_id)
    if look:
        items = Item.objects.filter(belong_to_look = look)
    
    if request.method == 'GET':
        return render_to_response('looks/detail.html', {'look':look, 'items':items }, context_instance=RequestContext(request))
    elif request.method == 'POST':
        position = request.POST['position']
        form = ItemForm(request.POST)
        if form.is_valid():
            if look:
                item = form.save(commit=False)
                item.belong_to_look = look
                item.x_position_on_look = position.split(",")[0]
                item.y_position_on_look = position.split(",")[1]
                #(r,g,b) = detect_item_color(look.look_photo, position.split(","))
                item.save()
        return HttpResponseRedirect(reverse('Look_v3_1.look.views.detail', args=(look.id,)))

def index(request):
    looks = get_list_or_404(Look)
    return render_to_response('looks/index.html', {'looks':looks}, context_instance=RequestContext(request))



        
    