from django.shortcuts import render

from .models import Photo

# 사진 목록 만들기
def photo_list(request): #함수형 뷰 (클래스형 뷰와는 달리 모든 기능을 직접 처리해야 함)
    photos = Photo.objects.all() #DB에 저장된 모든 객체 불러오기
    return render(request, 'photo/list.html', {'photos':photos}) #렌더링

from django.views.generic.edit import CreateView, DeleteView, UpdatedView
from django. shortcuts import redirect
class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.uer.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})